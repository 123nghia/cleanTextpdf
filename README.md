# 📘 Tool Ẩn/Xóa Số điện thoại & Email trong PDF

## 1. 🛠 Cài đặt môi trường

### 1.1. Yêu cầu
- Python 3.10+ (khuyến nghị Python 3.12)  
- pip & venv  
- Postman (tùy chọn, để test API trực tiếp)

### 1.2. Cài đặt thư viện
```bash
pip install fastapi uvicorn pymupdf jinja2 python-multipart
```

---

## 2. 🚀 Chạy server
```bash
uvicorn main:app --reload --port 9898
```
- Server chạy tại: [http://127.0.0.1:9898](http://127.0.0.1:9898)  
- Giao diện web upload: [http://127.0.0.1:9898/](http://127.0.0.1:9898/)

---

## 3. 📡 API Endpoints

| Endpoint | Method | Body (form-data) | Mô tả | Response |
|----------|--------|-----------------|-------|----------|
| `/api/status` | GET | – | Kiểm tra tình trạng server | ```json {"status": "running","uptime": "123s"} ``` |
| `/api/single-process` | POST | `file`: file PDF<br>`mode`: `"mask"` hoặc `"remove"` | Xử lý 1 file PDF, ẩn hoặc xóa số điện thoại & email | PDF đã xử lý (Content-Type: application/pdf) |
| `/api/multi-process` | POST | `files`: nhiều file PDF<br>`mode`: `"mask"` hoặc `"remove"` | Xử lý nhiều file PDF cùng lúc | File `.zip` chứa PDF đã xử lý (Content-Type: application/zip) |

### Ghi chú:
- `mask` → ẩn thông tin nhạy cảm (ví dụ che dấu bằng `***`)  
- `remove` → xóa hoàn toàn thông tin nhạy cảm

---

## 4. 🧪 Test API bằng Postman

### 4.1. `/api/single-process`
- Method: `POST`  
- URL: `http://127.0.0.1:9898/api/single-process`  
- Body → form-data → chọn 1 file PDF và `mode`  
- Kết quả: tải file PDF đã xử lý

### 4.2. `/api/multi-process`
- Method: `POST`  
- URL: `http://127.0.0.1:9898/api/multi-process`  
- Body → form-data → chọn nhiều file PDF và `mode`  
- Kết quả: nhận file `.zip` chứa PDF đã xử lý

### 4.3. `/api/status`
- Method: `GET`  
- URL: `http://127.0.0.1:9898/api/status`  
- Response ví dụ:
```json
{
  "status": "running",
  "uptime": "123s"
}
```

---

