import re
import json

# 1. Tên file SQL chính xác theo thư mục của bạn
sql_file_path = 'db_trichdan.sql'
js_file_path = 'db.js'

# 2. Đọc file SQL
with open(sql_file_path, 'r', encoding='utf-8') as f:
    sql_content = f.read()

# 3. Regex tìm cấu trúc: (stt, 'page', 'keyword')
pattern = r"\(\s*(\d+)\s*,\s*'([^']*)'\s*,\s*'([^']*)'\s*\)"
matches = re.findall(pattern, sql_content)

# 4. Trích xuất dữ liệu
data = []
for match in matches:
    data.append({
        "stt": int(match[0]),       # match[0] mới là số stt
        "page": match[1],      # match[1] là tên trang (tr0001.png)
        "keyword": match[2]   # match[2] là từ khóa
    })

# 5. Xuất ra file JS
js_content = f"const database = {json.dumps(data, ensure_ascii=False, indent=2)};\n\nexport default database;\n"

with open(js_file_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Thành công! Đã chuyển đổi {len(data)} bản ghi sang file {js_file_path}.")