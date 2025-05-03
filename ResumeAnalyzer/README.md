# 📄 ResumeAnalyzer

**ResumeAnalyzer** is a FastAPI-based backend application that helps analyze resumes by extracting key information, matching them against job descriptions, and offering insights to improve job fit. This project showcases skills in Python, FastAPI, file handling, and NLP.

---

## 🚀 Features

- 📤 Upload resumes (PDF, DOCX)
- 🧠 Extract key details (name, email, phone, education, skills, etc.)
- 🔍 Upload job descriptions and compare them with resumes
- 📊 Match scoring based on skill overlap
- 📝 Feedback and suggestions for improvement (coming soon)

---

## 🧱 Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python 3.8+
- **Libraries**: `pdfplumber`, `python-docx`, `spaCy`, `scikit-learn` (planned)
- **API Docs**: Swagger UI (auto-generated)

---

## 🏗 Project Structure

```
├── ResumeAnalyzer
├── .gitignore
├── README.md
├── app
│   ├── api
│   ├── config.py
│   ├── main.py
│   ├── models
│   ├── services
│   └── utils
├── requirements.txt
├── temp
└── tests
```
