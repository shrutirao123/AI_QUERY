# 🤖 AI Data Query Assistant – Natural Language to SQL Converter

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey?logo=flask)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Ollama](https://img.shields.io/badge/AI%20Model-LLaMA3-green?logo=meta)
![Bootstrap](https://img.shields.io/badge/UI-Bootstrap%205-blueviolet?logo=bootstrap)

---

### 🔍 Overview
**AI Data Query Assistant** is an intelligent Flask web app that converts **natural language questions into SQL queries** and executes them on your **MySQL database** — instantly displaying the results in a clean, tabular format.

The app supports multiple datasets such as:
- Retail Sales Data  
- Purchase Data  
- Purchase Documents (DIPL)  
- Sales Documents (DIPL)  

It even **auto-joins `company_masters`** with purchase/sales documents to show company names dynamically.

---

### 🚀 Features
✅ Convert **English questions → SQL Queries** using Ollama (LLaMA3 model)  
✅ Execute queries directly on **MySQL database**  
✅ Display tabular results beautifully  
✅ **Dropdown** to select database tables dynamically  
✅ **Copy SQL Query** button like ChatGPT  
✅ **Export Results to Excel (.xlsx)**  
✅ **Query History Sidebar** + Clear History Button  
✅ Automatically joins **company_masters** for company name resolution  
✅ **Modern Bootstrap 5 UI** with sidebar and loader animation  

---

### 🧩 Tech Stack
| Component | Technology Used |
|------------|----------------|
| **Backend** | Python (Flask) |
| **Frontend** | HTML, CSS, Bootstrap 5, JS |
| **AI Model** | Ollama – LLaMA3 |
| **Database** | MySQL |
| **Excel Export** | OpenPyXL |
| **Others** | Subprocess, Regex, Flask Sessions |

---

### ⚙️ Installation & Setup

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/yourusername/AI-Data-Query-Assistant.git
cd \AI DATA QUERY ASSI


2️⃣ Create Virtual Environment
python -m venv nlp_sql_env
# Activate environment
nlp_sql_env\Scripts\activate   # for Windows
source nlp_sql_env/bin/activate  # for Mac/Linux

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Setup MySQL Database
CREATE DATABASE retail_db;


Now import the following datasets into your phpMyAdmin or MySQL Workbench:

Dataset	Table Name
Retail Sales	retail_sales_dataset
Purchase Data	purchase_data_exe
Purchase Documents	purchase_documents
Sales Documents	sales_documents
Company Master	


5️⃣ Run Ollama (LLaMA3 Model)
Make sure Ollama is installed.
Then run:
ollama run llama3


6️⃣ Run Flask Server
python backend/app.py
Visit 👉 http://127.0.0.1:5000


📸 UI Features

🧭 Sidebar:
Dropdown for table selection
“Last Asked Questions” list
“Clear History” button


💻 Main Panel:

Shows user query
SQL generated (copyable)
Result table (exportable to Excel)
Error + loading spinner feedback


🧾 Folder Structure
AI DATA QUERY ASSI/
│
├── backend/
│   ├── app.py
│   ├── db.py
│   ├── ollama_utils.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── (custom CSS/JS files)
│
├── requirements.txt
└── README.md

**🧠 Future Enhancements**

---📈 Add Data Visualization (Charts)

---🔐 Add Login System for Personalized History

---🗣️ Integrate Voice Query Input

---⚡ Optimize Model Response Speed

---🧩 Add support for PostgreSQL / SQLite


👩‍💻 Developed By
Shruti Bhalerao
🎓 B.E. in Computer Engineering
💬 Python | Flask | AI | MySQL | Web Development
📍 Mumbai, India

🏷️ License
This project is open-source and available under the MIT License.

🚀 “Ask data in plain English — get instant insights with SQL power.”
