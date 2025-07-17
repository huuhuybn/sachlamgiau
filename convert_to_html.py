#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from pathlib import Path

def markdown_to_html(markdown_content):
    """Chuyển đổi Markdown thành HTML với styling đẹp"""
    
    # HTML template
    html_template = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}

        .content {{
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}

        h1 {{
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}

        h2 {{
            font-size: 2rem;
            color: #34495e;
            margin: 30px 0 20px 0;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}

        h3 {{
            font-size: 1.5rem;
            color: #2c3e50;
            margin: 25px 0 15px 0;
        }}

        h4 {{
            font-size: 1.2rem;
            color: #34495e;
            margin: 20px 0 10px 0;
        }}

        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}

        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}

        li {{
            margin-bottom: 8px;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #7f8c8d;
        }}

        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}

        em {{
            color: #7f8c8d;
        }}

        .navigation {{
            text-align: center;
            margin: 30px 0;
        }}

        .nav-button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 0 10px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s ease;
        }}

        .nav-button:hover {{
            background: #2980b9;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }}

        .footer a {{
            color: #3498db;
            text-decoration: none;
            font-weight: 600;
        }}

        .footer a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            {content}
        </div>
        
        <div class="navigation">
            <a href="index.html" class="nav-button">← Về trang chủ</a>
            {prev_button}
            {next_button}
        </div>
        
        <div class="footer">
            <p>© 2024 Nguyễn Hữu Huy - <a href="https://dotplays.com" target="_blank">Dotplays.com</a></p>
            <p>"Nơi kiến thức gặp gỡ sự sáng tạo"</p>
        </div>
    </div>
</body>
</html>"""

    # Chuyển đổi Markdown thành HTML
    html_content = markdown_content
    
    # Headers
    html_content = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    
    # Bold và Italic
    html_content = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html_content)
    
    # Lists
    html_content = re.sub(r'^- (.*?)$', r'<li>\1</li>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'(\n<li>.*?</li>\n)+', r'<ul>\g<0></ul>', html_content, flags=re.DOTALL)
    
    # Paragraphs
    html_content = re.sub(r'^([^<].*?)$', r'<p>\1</p>', html_content, flags=re.MULTILINE)
    
    # Clean up empty paragraphs
    html_content = re.sub(r'<p></p>', '', html_content)
    
    # Remove duplicate paragraph tags
    html_content = re.sub(r'<p><p>', '<p>', html_content)
    html_content = re.sub(r'</p></p>', '</p>', html_content)
    
    return html_content

def create_navigation_buttons(current_file, files_list):
    """Tạo nút điều hướng"""
    current_index = files_list.index(current_file) if current_file in files_list else -1
    
    prev_button = ""
    next_button = ""
    
    if current_index > 0:
        prev_file = files_list[current_index - 1]
        prev_button = f'<a href="{prev_file}" class="nav-button">← Chương trước</a>'
    
    if current_index < len(files_list) - 1:
        next_file = files_list[current_index + 1]
        next_button = f'<a href="{next_file}" class="nav-button">Chương tiếp →</a>'
    
    return prev_button, next_button

def main():
    """Chuyển đổi tất cả file Markdown thành HTML"""
    
    # Danh sách file theo thứ tự
    files_order = [
        'trang-bia.md',
        'muc-luc.md', 
        'loi-gioi-thieu.md',
        'chuong-1-thanh-lap-va-kien-tri.md',
        'chuong-2-chien-luoc-va-lap-ke-hoach.md',
        'chuong-3-quan-ly-tai-chinh-thong-minh.md',
        'chuong-4-xay-dung-moi-quan-he.md',
        'chuong-5-doi-moi-va-thich-nghi.md',
        'chuong-6-quan-ly-nhan-su.md',
        'chuong-7-mo-rong-thi-truong.md',
        'chuong-8-quan-ly-khung-hoang.md',
        'chuong-9-xay-dung-thuong-hieu.md',
        'chuong-10-di-san-va-tuong-lai.md',
        'ket-luan.md'
    ]
    
    # Tên file HTML tương ứng
    html_files = [
        'trang-bia.html',
        'muc-luc.html',
        'loi-gioi-thieu.html',
        'chuong-1-thanh-lap-va-kien-tri.html',
        'chuong-2-chien-luoc-va-lap-ke-hoach.html',
        'chuong-3-quan-ly-tai-chinh-thong-minh.html',
        'chuong-4-xay-dung-moi-quan-he.html',
        'chuong-5-doi-moi-va-thich-nghi.html',
        'chuong-6-quan-ly-nhan-su.html',
        'chuong-7-mo-rong-thi-truong.html',
        'chuong-8-quan-ly-khung-hoang.html',
        'chuong-9-xay-dung-thuong-hieu.html',
        'chuong-10-di-san-va-tuong-lai.html',
        'ket-luan.html'
    ]
    
    for md_file, html_file in zip(files_order, html_files):
        if os.path.exists(md_file):
            print(f"Đang chuyển đổi {md_file}...")
            
            # Đọc nội dung Markdown
            with open(md_file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
            
            # Chuyển đổi thành HTML
            html_content = markdown_to_html(markdown_content)
            
            # Tạo nút điều hướng
            prev_button, next_button = create_navigation_buttons(html_file, html_files)
            
            # Tạo title
            title = md_file.replace('.md', '').replace('-', ' ').title()
            
            # Tạo HTML hoàn chỉnh
            full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }}

        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}

        .content {{
            background: rgba(255, 255, 255, 0.95);
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}

        h1 {{
            font-size: 2.5rem;
            color: #2c3e50;
            margin-bottom: 20px;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}

        h2 {{
            font-size: 2rem;
            color: #34495e;
            margin: 30px 0 20px 0;
            border-left: 4px solid #3498db;
            padding-left: 15px;
        }}

        h3 {{
            font-size: 1.5rem;
            color: #2c3e50;
            margin: 25px 0 15px 0;
        }}

        h4 {{
            font-size: 1.2rem;
            color: #34495e;
            margin: 20px 0 10px 0;
        }}

        p {{
            margin-bottom: 15px;
            text-align: justify;
        }}

        ul, ol {{
            margin: 15px 0;
            padding-left: 30px;
        }}

        li {{
            margin-bottom: 8px;
        }}

        blockquote {{
            border-left: 4px solid #3498db;
            padding-left: 20px;
            margin: 20px 0;
            font-style: italic;
            color: #7f8c8d;
        }}

        strong {{
            color: #2c3e50;
            font-weight: 600;
        }}

        em {{
            color: #7f8c8d;
        }}

        .navigation {{
            text-align: center;
            margin: 30px 0;
        }}

        .nav-button {{
            display: inline-block;
            padding: 10px 20px;
            margin: 0 10px;
            background: #3498db;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            transition: background 0.3s ease;
        }}

        .nav-button:hover {{
            background: #2980b9;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }}

        .footer a {{
            color: #3498db;
            text-decoration: none;
            font-weight: 600;
        }}

        .footer a:hover {{
            text-decoration: underline;
        }}

        @media (max-width: 768px) {{
            .container {{
                padding: 10px;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            h1 {{
                font-size: 2rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="content">
            {html_content}
        </div>
        
        <div class="navigation">
            <a href="index.html" class="nav-button">← Về trang chủ</a>
            {prev_button}
            {next_button}
        </div>
        
        <div class="footer">
            <p>© 2024 Nguyễn Hữu Huy - <a href="https://dotplays.com" target="_blank">Dotplays.com</a></p>
            <p>"Nơi kiến thức gặp gỡ sự sáng tạo"</p>
        </div>
    </div>
</body>
</html>"""
            
            # Ghi file HTML
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(full_html)
            
            print(f"Đã tạo {html_file}")
        else:
            print(f"Không tìm thấy file {md_file}")

if __name__ == "__main__":
    main()
    print("Hoàn thành chuyển đổi tất cả file!") 