"""Tests for rewriting legacy eKYC links to the Zalo mini-app.

eKYC moved to a Zalo mini-app in 2026-07, but the old ``hitechcloud.vn/ekyc/`` URL
keeps resurfacing in outbound text — an MCP tool still returns it in
``ekyc_url``, or the session is holding an older copy of the skill. Rather
than chase every producer, the send path rewrites the link at the choke
point. A customer who follows a stale link lands on a dead page, so this is
customer-visible and belongs under test.

Same prefix-exec trick as ``test_outbound_scrub``: ``adapter.py`` pulls in
``gateway.*``, which only exists inside a Hermes install, and both constants
are defined above that import.
"""

import os
import unittest

_ADAPTER = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "adapter.py"
)
_CUTOFF = "from gateway.platforms.base import"


def _load_adapter_prefix():
    with open(_ADAPTER, encoding="utf-8") as f:
        src = f.read()
    ns: dict = {"__name__": "adapter_prefix"}
    exec(compile(src[: src.index(_CUTOFF)], _ADAPTER, "exec"), ns)
    return ns


_NS = _load_adapter_prefix()
_EKYC_OLD_RE = _NS["_EKYC_OLD_RE"]
_EKYC_NEW_BASE = _NS["_EKYC_NEW_BASE"]


def _rewrite(text: str) -> str:
    return _EKYC_OLD_RE.sub(_EKYC_NEW_BASE, text)


class TestEkycLinkRewrite(unittest.TestCase):
    def test_path_after_the_link_is_preserved(self):
        """The eKYC token lives in the path — dropping it breaks the flow."""
        self.assertEqual(
            _rewrite("Con vào https://tino.vn/ekyc/abc123 để định danh nha"),
            f"Con vào {_EKYC_NEW_BASE}abc123 để định danh nha",
        )

    def test_www_and_http_variants_are_rewritten(self):
        for url in (
            "https://api.hitechcloud.vn/api/vneidekyc/ekyc/x",
            "https://wwww.api.hitechcloud.vn/api/vneidekyc/ekyc/x",
            "https://my.hitechcloud.vn/api/vneidekyc/ekyc/x",
        ):
            with self.subTest(url=url):
                self.assertNotIn("api.hitechcloud.vn/api/vneidekyc/ekyc", _rewrite(url))

    def test_uppercase_host_is_rewritten(self):
        self.assertNotIn("API.HITECHCLOUD.VN/API/VNEIDEKYC/EKYC", _rewrite("HTTPS://API.HITECHCLOUD.VN/API/VNEID/EKYC/X"))

    def test_every_occurrence_is_rewritten(self):
        out = _rewrite("api.hitechcloud.vn/api/vneidekyc/ekyc/a rồi api.hitechcloud.vn/api/vneidekyc/ekyc/b")
        self.assertNotIn("api.hitechcloud.vn/api/vneidekyc/ekyc", out)
        self.assertEqual(out.count(_EKYC_NEW_BASE), 2)

    def test_unrelated_links_are_left_alone(self):
        """Only the eKYC path is redirected — nothing else on the domain."""
        for url in (
            "https://hitechcloud.vn/ekyc/",
            "https://ekyc.hitechcloud.vn/x/",
            "https://org.hitechcloud.vn/ekycheck/",
            "https://example.com/ekyc/x",
        ):
            with self.subTest(url=url):
                self.assertEqual(_rewrite(url), url)

    def test_rewrite_is_idempotent(self):
        """send() may run the scrub chain more than once on the same text."""
        once = _rewrite("https://tino.vn/ekyc/abc")
        self.assertEqual(_rewrite(once), once)

    def test_mini_app_target_is_a_zalo_link(self):
        self.assertTrue(_EKYC_NEW_BASE.startswith("https://zalo.me/"))
        self.assertTrue(_EKYC_NEW_BASE.endswith("/"), "must join cleanly onto the path")


if __name__ == "__main__":
    unittest.main()
