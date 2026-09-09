from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.MARKDOWN,
    chunk_size= 300,
    chunk_overlap = 0
)

text = """
# 📘 Project Name: Smart Student Tracker

A simple Python-based project to manage and track student data,

---

## 🔍 Features

- Add new students with relevant info  
- View student details  
- Check if a student is passing  
- Easily extendable class-based design  

---

## ❌ Tech Stack

- Python 3.10+  
- No external dependencies  
"""
chunks = text_splitter.split_text(text)

print(len(chunks))
print(chunks[0])