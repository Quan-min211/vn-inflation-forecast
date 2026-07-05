import os
import re

def fix_annotations_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tách văn bản thành các khối được bảo vệ (code, link) và văn bản thường
    # 1. Code blocks: ```...```
    # 2. Inline code: `...`
    # 3. Markdown links: [text](url)
    # 4. Math blocks: $$...$$
    pattern = re.compile(r'(```.*?```|`.*?`|\[.*?\]\(.*?\)|\$\$.*?\$\$)', flags=re.DOTALL)
    
    parts = pattern.split(content)
    
    # Các phần tử ở vị trí chẵn (0, 2, 4...) là văn bản thường
    # Các phần tử ở vị trí lẻ (1, 3, 5...) là các khối được bảo vệ
    for i in range(0, len(parts), 2):
        text = parts[i]
        
        # Thay thế " (nội dung)" thành " - nội dung"
        text = re.sub(r' \(([^)\n]+)\)', r' - \1', text)
        
        # Thay thế "(nội dung)" nằm sát chữ trước đó thành " - nội dung"
        # Tránh lỗi dính chữ như "Quán tính(Bệnh tự miễn)" -> "Quán tính - Bệnh tự miễn"
        text = re.sub(r'(?<=\S)\(([^)\n]+)\)', r' - \1', text)
        
        parts[i] = text

    new_content = "".join(parts)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"✅ Đã sửa file: {os.path.basename(filepath)}")
    else:
        print(f"➖ Không có thay đổi: {os.path.basename(filepath)}")

def main():
    directory = r"C:\HCMUTE\nam3ki2_2\da\vn-inflation-forecast\docs\report"
    print(f"Đang xử lý các file trong: {directory}\n")
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            fix_annotations_in_file(filepath)
    print("\n🎉 Hoàn tất!")

if __name__ == "__main__":
    main()
