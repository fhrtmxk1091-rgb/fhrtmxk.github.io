---
title: "오늘의 배움: 데이터 베이스와 python 연동하기"
date: 2026-03-17 00:00:00 +0900
categories: [TIL, 데이터베이스]
tags: [database, security]
---

## 오늘 배운 내용
- python을 설치함
- GitHub Pages와 Jekyll을 연동했다.
- python 설치와 연동을 배웠다.



```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fhrtmxk7517~",
    database="python_db"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM users WHERE id =1")
conn.commit()


cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor.close()
conn.close()
```

