# 🛍️ Dirty E-Commerce ETL Project

This project demonstrates a full **ETL (Extract, Transform, Load) pipeline** using Python, SQL Server, and Power BI on a dirty e-commerce dataset from Kaggle.  
The goal is to showcase the ability to **clean raw data, store it in SQL Server, and prepare it for visualization** using BI tools.

---

## 📂 Project Workflow

### 1. Extract
- Loaded **21 messy `.csv` files** from a Kaggle dataset.  
- Added metadata columns such as `category` (from file name) and `source_file`.

### 2. Transform
- Standardized column names (lowercase, replaced spaces with underscores).
- Cleaned overlapping columns:
  - Merged `goods-title-link` and `goods-title-link--jump` into one.
  - Removed unnecessary columns like `goods-title-link--jump href`.
- Cleaned price columns:
  - Removed the **`$` symbol**.
  - Converted values from string → float.
- Dropped empty columns and handled missing values.

### 3. Load
- Prepared cleaned data for loading into **Microsoft SQL Server**.
- Will connect Power BI to SQL Server for reporting and visualization.

---

## 🛠️ Tools & Technologies
- **Python** (Pandas, SQLAlchemy, pyodbc)  
- **SQL Server** (Data storage)  
- **Power BI** (Data visualization)  
- **Git & GitHub** (Version control)  
- **Jupyter Notebook / VS Code** (Development environment)  

---

## 📊 Next Steps
- Finalize SQL Server schema and load the cleaned dataset.  
- Build **Power BI dashboards** for insights into product pricing, categories, and missing data patterns.  

---

## 🚀 Key Learnings
- How to structure a real-world **ETL pipeline**.  
- Cleaning messy real-world data (multiple CSVs with inconsistent columns).  
- Integrating Python with **SQL Server** and **Power BI**.  
- Using GitHub for version control and collaboration.  

---

## 📌 Repository Contents
- `Dirty E-Commerce ETL Project.ipynb` → Jupyter Notebook with ETL pipeline.  
- (Future) SQL scripts and Power BI reports.  

---

## 🤝 Contribution
Feel free to fork this repository, suggest improvements, or use it as a learning resource for your own ETL projects!

## How to Run
- Clone this repository: git clone https://github.com/YourUsername/your-repo-name.git
cd (https://github.com/93Chidiebere/ETL-CSV-Cleaning)
- Install dependencies
pip install pandas sqlalchemy pyodbc
- Open Jupyter notebook
jupyter notebook "Dirty E-Commerce ETL Project.ipynb"
- Data Source: https://www.kaggle.com/datasets/oleksiimartusiuk/e-commerce-data-shein?resource=download



