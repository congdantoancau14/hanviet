const fs = require('fs');

// 1. Đọc file SQL
const sqlContent = fs.readFileSync('data.sql', 'utf8');

// 2. Trích xuất các giá trị trong câu lệnh INSERT INTO
const regex = /\((\d+),\s*'([^']+)',\s*'([^']*)'\)/g;
const records = [];
let match;

while ((match = regex.exec(sqlContent)) !== null) {
  records.push({
    stt: parseInt(match[1], 10),
    page: match[2],
    keyword: match[3]
  });
}

// 3. Ghi ra file db.js
const fileContent = `const database = ${JSON.stringify(records, null, 2)};\n\nexport default database;\n`;
fs.writeFileSync('db.js', fileContent, 'utf8');

console.log(`Thành công! Đã chuyển đổi ${records.length} bản ghi sang db.js.`);