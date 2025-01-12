---
    title: "Lập trình Python Cơ bản 1.4 - Sử dụng Terminal để chạy script Python"
    sidebar: python_course_sidebar
    permalink: /python-basic-1-4-su-dung-terminal-de-chay-script-python.html
    folder: python-basic-free
---
# Hướng dẫn cài đặt Python trên Windows, macOS và Ubuntu

## 1. Cài đặt Python trên Windows

### Bước 1: Tải Python
1. Truy cập trang web chính thức của Python: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Nhấn vào nút **Download** phù hợp với phiên bản Windows (thường là bản mặc định cho hệ thống của bạn).

### Bước 2: Cài đặt Python
1. Chạy tệp `.exe` vừa tải về.
2. Đánh dấu **Add Python to PATH** (rất quan trọng, nếu không bạn sẽ phải cấu hình PATH thủ công).
3. Nhấn **Customize Installation** nếu cần tùy chỉnh (tùy chọn), hoặc nhấn **Install Now** để cài đặt ngay.
4. Chờ quá trình cài đặt hoàn tất, sau đó nhấn **Close**.

### Bước 3: Kiểm tra cài đặt
1. Mở **Command Prompt** (cmd).
2. Gõ lệnh:
```bash
    python --version
```
    Hoặc

    ```bash
    python3 --version
    ```
    Nếu Python được cài đặt thành công, phiên bản sẽ hiển thị như sau.
    ![Python version](/images/python-basic-course/python_1_3_version.png)

## 2. Cài đặt Python trên macOS
### Bước 1: Kiểm tra Python có sẵn trên máy
Mở Terminal.
Gõ lệnh:
```bash
python3 --version
```
Nếu đã có Python (phiên bản 3.x), bạn không cần cài đặt thêm. Nếu chưa có hoặc muốn nâng cấp, tiếp tục các bước dưới đây.

### Bước 2: Cài đặt Python qua Homebrew
1. Cài đặt Homebrew (nếu chưa có):
```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Cài đặt Python:
    ```bash
    brew install python
    ```

### Bước 3: Kiểm tra cài đặt
Gõ lệnh sau để chắc chắn là Python đã được cài:

```bash
    python3 --version
```

Nếu Python được cài đặt thành công, phiên bản sẽ hiển thị như sau.
    ![Python version](/images/python-basic-course/python_1_3_version.png)

## 3. Cài đặt Python trên Ubuntu
### Bước 1: Kiểm tra phiên bản Python hiện có
Mở Terminal.
Gõ lệnh:
```bash
    python3 --version
```
Hầu hết các bản Ubuntu mới đã có sẵn Python 3.x. Nếu muốn cài đặt hoặc nâng cấp, tiếp tục các bước dưới đây.

### Bước 2: Cài đặt hoặc nâng cấp Python
1. Cập nhật danh sách các gói có sẵn:
    ```bash
    sudo apt update
    ```

    Cài đặt Python:
    ```bash
    sudo apt install python3
    ```

    Cài đặt công cụ quản lý gói pip (nếu cần):
    ```bash
    sudo apt install python3-pip
    ```
### Bước 3: Kiểm tra cài đặt
Gõ lệnh:
```bash
python3 --version
```
Phiên bản Python sẽ hiển thị nếu cài đặt thành công.

## Cấu hình thêm (nếu cần)
### Cài đặt thư viện: Sử dụng pip để cài đặt các gói thư viện cần thiết:

Câu lệnh:
```bash
pip install <tên-thư-viện>
```

IDE gợi ý: Bạn có thể sử dụng Visual Studio Code, PyCharm, hoặc Jupyter Notebook để viết và chạy mã Python. Tùy thuộc công cụ nào bạn quen thuộc. Nếu chưa từng làm việc với bất kì IDE nào, có thể sử dụng VSCode.