---
    title: "Lập trình Python Cơ bản 1.4 - Sử dụng Terminal để chạy script Python"
    sidebar: python_course_sidebar
    permalink: /python-basic-1-4-su-dung-terminal-de-chay-script-python.html
    folder: python-basic-free
---
## 1. Tạo file .py chứa code

### Bước 1: Trước tiên, bạn hãy tạo 1 folder để lưu giữ code của mình
Công việc lập trình luôn luôn có nhiều thử thách cho dù bạn là người mới hay đã nhiều năm kinh nghiệm. Chính vì vậy, hãy tập cho mình thói quen ngăn nắp để lưu giữ kiến thích, tiết kiệm thời gian lần mò.

1. Để bắt đầu khóa học này, mỗi người hãy tạo cho mình 1 folder để lưu giữ code của khóa học.
2. Mở VSCode -> Open Folder... -> Trỏ đến Folder bạn vừa tạo -> Click Open.

### Bước 2: Tạo file .py
Trong giao diện của VSCode, bấm vào New File để tạo 1 file Python mới.
Tạo file có tên _python_1_4-su-dung-terminal-de-chay-script.py_
Sau đó hãy thêm đoạn code này:
```python
print('Python 1-4: Hello World! From Dien tu va Lap Trinh!')
```
Bạn học tạm thời chưa cần biết ý nghĩa của đoạn code.
Hãy nhấn Ctrl + S để lưu file lại (bước này rất quan trọng).

### Bước 3: Sử dụng Terminal sẵn có của VSCode để chạy Python
1. Kiếm tra xem VSCode đã bật sẵn Terminal chưa. ( Góc dưới )
![Terminal on VSCode](/images/python-basic-course/python-basic-1-4-terminal-python-VSCode.png)

2. Gõ lệnh:
Nếu Terminal chưa được bật, hãy vào Terminal -> New Terminal (phím tắt Ctrl + Shift + `) để bật Terminal mới trong VSCode nhé.

## 2. Chạy file .py

Từ Terminal.
Gõ lệnh:
```bash
python3 <tên_file>
```
Ví dụ:
```bash
python3 python_1_4-su-dung-terminal-de-chay-script.py
```
Kết quả, sẽ có dòng chữ in ra trên Terminal như sau:
```bash
Python 1-4: Hello World! From Dien tu va Lap Trinh!
```
Đến đây, bạn đã biết dùng Python để ra lệnh được cho máy tính in ra dòng chữ mình muốn. Chúc mừng bạn đã chạy được dòng lệnh Python đầu tiên.