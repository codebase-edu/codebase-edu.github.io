---
title:  "C++ và Hungarian Notation: Quy tắc đặt tên chuyên nghiệp"
summary: "Trong lập trình nâng cao, việc tuân thủ theo các quy tắc lập trình là bắt buộc để có 1 bộ source đẹp và dễ dàng đọc hiểu bởi nhiều developer. Hungarian notation là một quy ước đặt tên biến nhằm đến mục đích như vậy. Xin mời các bạn đọc tiếp để hiểu thêm về Hungarian Notation nhé."
# date: 2024-12-01 23:05:00
# date:   2024-12-01 20:05:00
toc: True
tags: [C++, CodingConvention]
keywords: C++, embedded, coding-convention
permalink: coding-convention-dăt-ten-bien-theo-hungarian-notation.html
categories: C++-Advance
# sidebar: python_course_sidebar
# sc_project: 11213301
# sc_security: 8d50f6a5
img: /assets/cpp/cpp-programming-400x250.png
---

# Hungarian Notation là gì

Có thế đây là lần đầu tiên bạn nghe nói về Hungarian notation. Đây là một quy ước đặt tên biến trong lập trình, được thiết kế để cung cấp thông tin về kiểu dữ liệu hoặc mục đích sử dụng của biến thông qua các tiền tố (prefix). Kỹ thuật này giúp lập trình viên dễ dàng nhận diện và tránh những lỗi liên quan đến kiểu dữ liệu.
Hungarian notation có thế áp dụng ở bất kì ngôn ngữ lập trình nào. Ở Microsoft, ban đầu nó được áp dụng rộng rãi trong các dự án sử dụng ngôn ngữ C, sau đó mở rộng sang C++.

## 1. Lịch sử và nguồn gốc
Hungarian notation được **Charles Simonyi**, một kỹ sư tại Microsoft, giới thiệu. Tên gọi "Hungarian" bắt nguồn từ việc quy ước này tạo ra những tên biến với cấu trúc trông giống các từ trong tiếng Hungary.



## 2. Cấu trúc của Hungarian notation
Tên biến trong Hungarian notation thường có dạng sau:

```cpp
<prefix><baseName>

```


- **`prefix`**: Biểu thị kiểu dữ liệu hoặc mục đích của biến.
- **`baseName`**: Tên biến mô tả ý nghĩa hoặc nội dung.

Ví dụ:

| Tên Biến     | Giải Thích                                   |
|--------------|----------------------------------------------|
| `iCount`     | `i`: integer, `Count`: đếm số lượng.         |
| `szName`     | `sz`: string terminated by null, `Name`: tên.|
| `pData`      | `p`: pointer, `Data`: dữ liệu.               |
| `fIsReady`   | `f`: boolean/flag, `IsReady`: đã sẵn sàng?.  |



## 3. Các tiền tố thường dùng

### Kiểu dữ liệu cơ bản

| Tiền Tố  | Kiểu Dữ Liệu          | Ví Dụ         |
|----------|-----------------------|---------------|
| `i`      | Integer (số nguyên)   | `iCount`      |
| `f`      | Float (số thực)       | `fRate`       |
| `d`      | Double                | `dDistance`   |
| `b`      | Boolean (đúng/sai)    | `bIsValid`    |
| `c`      | Char (kí tự)          | `cInitial`    |

### Kiểu dữ liệu phức tạp

| Tiền Tố  | Kiểu Dữ Liệu          | Ví Dụ         |
|----------|-----------------------|---------------|
| `p`      | Pointer               | `pNode`       |
| `lp`     | Long Pointer          | `lpBuffer`    |
| `sz`     | String (null-terminated) | `szName`   |
| `h`      | Handle                | `hFile`       |

### Mục đích sử dụng

| Tiền Tố  | Ý Nghĩa               | Ví Dụ         |
|----------|-----------------------|---------------|
| `n`      | Count (số lượng)      | `nItems`      |
| `m`      | Member variable       | `m_nID`       |
| `g`      | Global variable       | `g_fConfig`   |
| `k`      | Constant              | `kPi`         |

Trong C++, quy tắc này đôi khi được mở rộng để bao gồm phạm vi (scope) của biến, tùy chọn được phân tách bằng dấu gạch dưới. Phần mở rộng này thường được sử dụng mà không cần chỉ định kiểu Hungarian:

| Tiền Tố  | Ý Nghĩa                                      	| Ví Dụ         |
|----------|------------------------------------------------|---------------|
| `g`      | Biến toàn cục, kiểu số nguyên      				| `g_nWheels`   |
| `m`      | Biến trong struc / clas, kiểu số nguyên      	| `m_nWheels`   |
| `s`      | Biến tĩnh (static) của 1 class       			| `s_wheels`   	|
| `c`      | Biến tĩnh (static) của 1 hàm              		| `c_wheels`    |



## 4. Ưu điểm
- **Tăng khả năng đọc code**: Giúp lập trình viên hiểu rõ kiểu dữ liệu hoặc mục đích của biến mà không cần kiểm tra định nghĩa.
- **Hỗ trợ debug hiệu quả**: Dễ dàng xác định lỗi liên quan đến kiểu dữ liệu.
- **Thống nhất trong nhóm**: Khi sử dụng đồng bộ, quy tắc này tạo sự nhất quán trong codebase.



## 5. Nhược điểm
- **Giảm tính linh hoạt**: Khi kiểu dữ liệu thay đổi, bạn phải đổi lại tên biến, gây phiền toái và dễ bỏ sót.
- **Khó duy trì với code phức tạp**: Với các dự án lớn, việc quản lý quy tắc Hungarian notation trở nên rối rắm.
- **Lỗi thời**: Với các ngôn ngữ hiện đại như C++, C#, Java, hoặc Python, công cụ IDE và type inference (suy luận kiểu) đã làm giảm tính hữu ích của Hungarian notation.



## 6. Khi nào nên dùng?
Hungarian notation phù hợp với:
1. **Ngôn ngữ không có kiểm tra kiểu mạnh** (e.g., C).
2. **Code legacy**: Các dự án cũ đã sử dụng quy tắc này.
3. **Trường hợp cần nhanh chóng nhận diện kiểu dữ liệu** trong codebase phức tạp.



## 7. Ví dụ

```cpp
// Code không dùng Hungarian notation
int count = 10;
float rate = 5.5;
bool isReady = true;


// Code dùng Hungarian notation
int iCount = 10;
float fRate = 5.5f;
bool bIsReady = true;

```
Đối với code dùng Hungarian Notation, người dev có thể nắm bắt ngay kiểu dữ liệu từ lúc đọc tên biến, không cần phải chuyển đổi qua lại giữa file header và source code.

Hungarian notation từng là tiêu chuẩn hữu ích trong lập trình, đặc biệt khi công cụ hỗ trợ còn hạn chế. Tuy nhiên, với sự tiến bộ của IDE và khả năng suy luận kiểu, việc sử dụng nó trở thành tùy chọn thay vì bắt buộc. Quy tắc này có thể được áp dụng linh hoạt dựa trên yêu cầu dự án hoặc sở thích cá nhân.

_Bài tiếp theo sẽ là: Google C++ Style Guide, mời các bạn đón đọc._

## Tham khảo:

[1] [CS245](https://www.cse.iitk.ac.in/users/dsrkg/cs245/html/Guide.htm ){:target="_blank"}

[2] [Wikipedia](https://en.wikipedia.org/wiki/Hungarian_notation){:target="_blank"}

