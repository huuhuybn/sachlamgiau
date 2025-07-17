#!/bin/bash

# Script tự động deploy lên GitHub Pages
# Tác giả: Nguyễn Hữu Huy - Dotplays.com

echo "🚀 Bắt đầu deploy cuốn sách lên GitHub Pages..."

# Kiểm tra xem có phải là Git repository không
if [ ! -d ".git" ]; then
    echo "📁 Khởi tạo Git repository..."
    git init
fi

# Chạy script chuyển đổi Markdown sang HTML
echo "📝 Chuyển đổi Markdown sang HTML..."
python3 convert_to_html.py

# Thêm tất cả file vào staging area
echo "📦 Thêm file vào staging area..."
git add .

# Commit thay đổi
echo "💾 Commit thay đổi..."
git commit -m "Update: Cập nhật nội dung cuốn sách $(date '+%Y-%m-%d %H:%M:%S')"

# Push lên GitHub
echo "⬆️ Push lên GitHub..."
git push origin main

echo "✅ Hoàn thành deploy!"
echo ""
echo "📖 Website sẽ có sẵn tại: https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
echo "⏰ Có thể mất vài phút để GitHub Pages cập nhật"
echo ""
echo "🔗 Để kiểm tra deployment:"
echo "   1. Vào repository trên GitHub"
echo "   2. Vào tab 'Actions' để xem log"
echo "   3. Vào Settings > Pages để xem URL"
echo ""
echo "📞 Nếu gặp vấn đề, hãy kiểm tra:"
echo "   - Repository có public không"
echo "   - GitHub Pages đã được kích hoạt chưa"
echo "   - File index.html có trong root directory không" 