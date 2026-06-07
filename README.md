# Hermes Zalo Plugin (Personal Account)

🇻🇳 **Tiếng Việt**

Plugin kết nối **tài khoản Zalo cá nhân** vào Hermes Agent thông qua một **sidecar Node.js** sử dụng thư viện `zca-js` (Zalo Web API không chính thức).

> ⚠️ **CẢNH BÁO QUAN TRỌNG**
>
> * Đây là API Zalo **không chính thức**.
> * **Khuyến nghị sử dụng tài khoản phụ**, không dùng tài khoản Zalo chính.
> * Gửi lời mời kết bạn hoặc tin nhắn hàng loạt có thể khiến tài khoản bị hạn chế hoặc khóa.
> * Người dùng tự chịu trách nhiệm khi sử dụng phần mềm này.
> * Luôn tuân thủ Điều khoản sử dụng của Zalo và các quy định pháp luật liên quan.

## Tính năng

* Nhận và gửi tin nhắn Zalo cá nhân và nhóm.
* Gửi hình ảnh, tập tin, sticker, reaction và trạng thái "đang nhập".
* Quét thành viên nhóm từ liên kết `zalo.me/g/...` (nếu nhóm cho phép xem thành viên).
* Tự động xây dựng phễu marketing:

  * Thu thập lead.
  * Gửi lời mời kết bạn.
  * Nhắn tin tự động bằng nội dung AI cá nhân hóa.
  * Đồng bộ CRM.
* Tự động chấp nhận lời mời kết bạn.
* Tra cứu UID Zalo từ số điện thoại.
* Gửi nhiều ảnh cùng lúc.
* Tạo và gửi file HTML, PDF, PowerPoint và Excel.
* Hỗ trợ Google Sheets để lưu trữ và quản lý lead.

## Yêu cầu

* Hermes Agent đang hoạt động.
* Node.js 18 trở lên.
* (Tùy chọn) Python packages:

  * google-api-python-client
  * google-auth
* (Khuyến nghị) Proxy dân cư cùng quốc gia với tài khoản Zalo.

## Cài đặt

1. Sao chép thư mục plugin vào thư mục plugins của Hermes.
2. Cài đặt dependencies:

```bash
cd plugins/zalo-personal/sidecar
npm install
```

3. Cấu hình biến môi trường trong `.env`.
4. Khởi động Hermes.
5. Đăng nhập Zalo bằng QR Code lần đầu.
6. Thiết lập `ZALO_PERSONAL_OWNER_UID`.

## An toàn sử dụng

* Sử dụng tài khoản Zalo phụ.
* Giới hạn số lượng lời mời và tin nhắn mỗi ngày.
* Luôn gửi nhỏ giọt và có khoảng nghỉ ngẫu nhiên.
* Hạn chế nhắn tin tới người lạ.

## Miễn trừ trách nhiệm

Phần mềm được cung cấp theo nguyên trạng ("AS IS"), không có bất kỳ cam kết hay bảo hành nào. Việc sử dụng API Zalo không chính thức có thể dẫn đến việc tài khoản bị hạn chế hoặc khóa.

---

🇺🇸 **English**

Hermes Zalo Plugin connects a **personal Zalo account** to Hermes Agent through a lightweight **Node.js sidecar** powered by `zca-js` (an unofficial Zalo Web API library).

> ⚠️ **IMPORTANT DISCLAIMER**
>
> * This project uses an **unofficial Zalo API**.
> * It is strongly recommended to use a **secondary Zalo account**, not your primary account.
> * Excessive friend requests or bulk messaging may result in account restrictions or bans.
> * Users are solely responsible for how they use this software.
> * Always comply with Zalo's Terms of Service and applicable privacy regulations.

## Features

* Send and receive Zalo direct and group messages.
* Support for images, files, stickers, reactions, and typing indicators.
* Group member discovery from `zalo.me/g/...` links (when member visibility is allowed).
* Semi-automated marketing funnel:

  * Lead collection.
  * Friend requests.
  * AI-generated personalized outreach.
  * CRM integration.
* Auto-accept friend requests.
* Phone number to Zalo UID lookup.
* Multi-image messaging.
* Generate and send HTML, PDF, PowerPoint, and Excel files.
* Optional Google Sheets integration for lead management.

## Requirements

* Hermes Agent.
* Node.js 18+.
* Optional Python packages:

  * google-api-python-client
  * google-auth
* Residential proxy recommended.

## Installation

1. Copy the plugin into the Hermes plugins directory.
2. Install sidecar dependencies:

```bash
cd plugins/zalo-personal/sidecar
npm install
```

3. Configure environment variables.
4. Start Hermes Agent.
5. Authenticate using the QR code.
6. Configure `ZALO_PERSONAL_OWNER_UID`.

## Safety Recommendations

* Use a secondary account.
* Keep daily friend requests and messages low.
* Use randomized delays and rate limits.
* Avoid aggressive outreach to non-friends.

## Project Structure

```text
zalo-personal/
├── __init__.py
├── adapter.py
├── marketing.py
├── plugin.yaml
├── .env.example
└── sidecar/
    ├── server.js
    └── package.json
```

## License & Disclaimer

This software is provided "AS IS" without warranty of any kind. Using unofficial Zalo APIs carries a risk of account limitation or suspension. The authors are not responsible for any damages, account restrictions, legal issues, or losses resulting from the use of this software.
