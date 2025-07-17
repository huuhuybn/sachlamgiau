#!/usr/bin/env python3
"""
Script tạo favicon từ SVG
Chuyển đổi favicon.svg thành các file PNG với kích thước khác nhau
"""

import os
import subprocess
import sys

def check_dependencies():
    """Kiểm tra các dependency cần thiết"""
    try:
        subprocess.run(['rsvg-convert', '--version'], capture_output=True, check=True)
        print("✅ rsvg-convert đã được cài đặt")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ rsvg-convert chưa được cài đặt")
        print("📦 Cài đặt trên macOS: brew install librsvg")
        print("📦 Cài đặt trên Ubuntu: sudo apt-get install librsvg2-bin")
        return False

def generate_favicon_png(input_svg, output_png, size):
    """Tạo file PNG từ SVG với kích thước cụ thể"""
    try:
        cmd = [
            'rsvg-convert',
            '--width', str(size),
            '--height', str(size),
            '--output', output_png,
            input_svg
        ]
        subprocess.run(cmd, check=True)
        print(f"✅ Đã tạo {output_png} ({size}x{size})")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Lỗi khi tạo {output_png}: {e}")
        return False

def create_placeholder_png(filename, size):
    """Tạo file PNG placeholder đơn giản"""
    try:
        # Sử dụng ImageMagick hoặc Pillow để tạo placeholder
        from PIL import Image, ImageDraw, ImageFont
        
        # Tạo hình ảnh mới
        img = Image.new('RGBA', (size, size), (102, 126, 234, 255))
        draw = ImageDraw.Draw(img)
        
        # Vẽ hình tròn
        margin = size // 8
        draw.ellipse([margin, margin, size - margin, size - margin], 
                    fill=(255, 215, 0, 255), outline=(139, 69, 19, 255), width=2)
        
        # Thêm text "S" (Sách)
        try:
            font_size = size // 4
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
        except:
            font = ImageFont.load_default()
        
        text = "S"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        x = (size - text_width) // 2
        y = (size - text_height) // 2
        draw.text((x, y), text, fill=(44, 62, 80, 255), font=font)
        
        img.save(filename)
        print(f"✅ Đã tạo {filename} ({size}x{size}) - placeholder")
        return True
        
    except ImportError:
        print(f"⚠️ Không thể tạo {filename} - Pillow chưa được cài đặt")
        return False
    except Exception as e:
        print(f"❌ Lỗi khi tạo {filename}: {e}")
        return False

def main():
    """Hàm chính"""
    print("🎨 TẠO FAVICON CHO WEBSITE")
    print("=" * 40)
    
    # Kiểm tra file SVG
    if not os.path.exists('favicon.svg'):
        print("❌ Không tìm thấy favicon.svg")
        return
    
    # Danh sách favicon cần tạo
    favicons = [
        ('favicon-16x16.png', 16),
        ('favicon-32x32.png', 32),
        ('apple-touch-icon.png', 180)
    ]
    
    success_count = 0
    
    for filename, size in favicons:
        if os.path.exists('favicon.svg'):
            # Thử convert từ SVG
            if generate_favicon_png('favicon.svg', filename, size):
                success_count += 1
            else:
                # Fallback: tạo placeholder
                if create_placeholder_png(filename, size):
                    success_count += 1
        else:
            # Tạo placeholder nếu không có SVG
            if create_placeholder_png(filename, size):
                success_count += 1
    
    print(f"\n📊 KẾT QUẢ: {success_count}/{len(favicons)} favicon đã được tạo")
    
    if success_count == len(favicons):
        print("🎉 Tất cả favicon đã được tạo thành công!")
    else:
        print("⚠️ Một số favicon chưa được tạo. Vui lòng kiểm tra lại.")

if __name__ == "__main__":
    main() 