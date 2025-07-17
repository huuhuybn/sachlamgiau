# 🚀 HƯỚNG DẪN PUBLISH LÊN GITHUB PAGES

## 📋 Bước 1: Tạo Repository trên GitHub

1. **Đăng nhập vào GitHub**
   - Truy cập [github.com](https://github.com)
   - Đăng nhập vào tài khoản của bạn

2. **Tạo repository mới**
   - Click vào nút "New" hoặc "+" ở góc trên bên phải
   - Đặt tên repository: `con-duong-den-giau-co` (hoặc tên bạn muốn)
   - Chọn "Public" (để có thể sử dụng GitHub Pages miễn phí)
   - **KHÔNG** check vào "Add a README file" (vì chúng ta đã có sẵn)
   - Click "Create repository"

## 📋 Bước 2: Push code lên GitHub

Mở Terminal/Command Prompt và chạy các lệnh sau:

```bash
# 1. Khởi tạo Git repository (nếu chưa có)
git init

# 2. Thêm tất cả file vào staging area
git add .

# 3. Commit lần đầu
git commit -m "Initial commit: Cuốn sách Con Đường Đến Giàu Có"

# 4. Thêm remote repository (thay YOUR_USERNAME bằng username GitHub của bạn)
git remote add origin https://github.com/YOUR_USERNAME/con-duong-den-giau-co.git

# 5. Push lên GitHub
git branch -M main
git push -u origin main
```

## 📋 Bước 3: Kích hoạt GitHub Pages

1. **Vào repository trên GitHub**
   - Truy cập repository vừa tạo

2. **Vào Settings**
   - Click vào tab "Settings" (cạnh tab "Code")

3. **Kích hoạt GitHub Pages**
   - Scroll xuống phần "Pages" (hoặc click vào "Pages" trong sidebar bên trái)
   - Ở phần "Source", chọn "Deploy from a branch"
   - Chọn branch "main"
   - Chọn folder "/ (root)"
   - Click "Save"

4. **Chờ deployment**
   - GitHub sẽ mất vài phút để deploy
   - Bạn sẽ thấy URL của GitHub Pages (thường là `https://YOUR_USERNAME.github.io/con-duong-den-giau-co`)

## 📋 Bước 4: Kiểm tra và tùy chỉnh

### Kiểm tra website:
- Truy cập URL GitHub Pages để xem website
- Kiểm tra tất cả các link và chức năng

### Tùy chỉnh (nếu cần):

1. **Thay đổi URL trong README-GitHub.md:**
   - Mở file `README-GitHub.md`
   - Thay `your-username` và `your-repo-name` bằng thông tin thực tế
   - Commit và push lại

2. **Thêm custom domain (tùy chọn):**
   - Trong Settings > Pages
   - Thêm custom domain nếu có

## 📋 Bước 5: Cập nhật nội dung

Khi muốn cập nhật nội dung:

```bash
# 1. Chỉnh sửa file
# 2. Chạy script chuyển đổi (nếu cần)
python3 convert_to_html.py

# 3. Commit và push
git add .
git commit -m "Cập nhật nội dung chương X"
git push
```

## 🔧 Troubleshooting

### Lỗi thường gặp:

1. **"Repository not found"**
   - Kiểm tra URL repository có đúng không
   - Đảm bảo repository là public

2. **"Page not found"**
   - Đảm bảo file `index.html` có trong root directory
   - Kiểm tra GitHub Pages đã được kích hoạt chưa

3. **"Build failed"**
   - Kiểm tra file `index.html` có lỗi syntax không
   - Đảm bảo tất cả file HTML đều có encoding UTF-8

### Kiểm tra deployment:
- Vào tab "Actions" trong repository để xem log deployment
- Nếu có lỗi, sẽ hiển thị chi tiết ở đây

## 📱 Tính năng của website

✅ **Responsive Design** - Tương thích với mọi thiết bị  
✅ **Navigation** - Điều hướng dễ dàng giữa các chương  
✅ **Modern UI** - Giao diện đẹp, chuyên nghiệp  
✅ **Fast Loading** - Tải trang nhanh  
✅ **SEO Friendly** - Tối ưu cho tìm kiếm  

## 🌟 Kết quả

Sau khi hoàn thành, bạn sẽ có:
- Website chuyên nghiệp tại `https://YOUR_USERNAME.github.io/con-duong-den-giau-co`
- Cuốn sách có thể đọc online từ mọi thiết bị
- Repository GitHub với đầy đủ source code
- Khả năng cập nhật nội dung dễ dàng

## 📞 Hỗ trợ

Nếu gặp vấn đề, hãy:
1. Kiểm tra log trong tab "Actions"
2. Đảm bảo tất cả file đã được push lên GitHub
3. Kiểm tra cài đặt GitHub Pages trong Settings

---

**Chúc bạn thành công với việc publish cuốn sách lên GitHub Pages!** 🎉

**Nguyễn Hữu Huy - Dotplays.com** 