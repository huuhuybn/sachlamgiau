#!/bin/bash

echo "🚀 SCRIPT PUSH LÊN GITHUB PAGES"
echo "=================================="
echo ""

# Kiểm tra xem đã có remote chưa
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ Chưa có remote repository!"
    echo ""
    echo "📋 HƯỚNG DẪN NHANH:"
    echo "1. Tạo repository trên GitHub:"
    echo "   - Truy cập: https://github.com/new"
    echo "   - Đặt tên: con-duong-den-giau-co"
    echo "   - Chọn Public"
    echo "   - KHÔNG check 'Add README'"
    echo "   - Click 'Create repository'"
    echo ""
    echo "2. Copy URL repository (sẽ hiển thị sau khi tạo)"
    echo "   Ví dụ: https://github.com/YOUR_USERNAME/con-duong-den-giau-co.git"
    echo ""
    echo "3. Chạy lệnh sau (thay YOUR_USERNAME và YOUR_REPO_NAME):"
    echo "   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    echo "4. Kích hoạt GitHub Pages:"
    echo "   - Vào Settings > Pages"
    echo "   - Source: Deploy from a branch"
    echo "   - Branch: main"
    echo "   - Folder: / (root)"
    echo "   - Save"
    echo ""
    echo "5. Website sẽ có tại: https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
    echo ""
    echo "🎯 Tất cả file đã sẵn sàng! Chỉ cần làm theo hướng dẫn trên."
    exit 1
fi

# Nếu đã có remote, push lên
echo "✅ Đã có remote repository!"
echo "⬆️ Pushing lên GitHub..."
git push origin main

echo ""
echo "🎉 HOÀN THÀNH!"
echo "📖 Website sẽ có tại: https://YOUR_USERNAME.github.io/YOUR_REPO_NAME"
echo "⏰ Có thể mất 5-10 phút để GitHub Pages cập nhật"
echo ""
echo "🔗 Để kiểm tra:"
echo "   - Vào repository trên GitHub"
echo "   - Vào Settings > Pages"
echo "   - Xem URL được cung cấp" 