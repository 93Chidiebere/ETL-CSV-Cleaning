Dirty E-Commerce ETL Project
📌 Overview

This project is an ETL (Extract, Transform, Load) pipeline built in Python to clean and prepare e-commerce datasets before loading them into a SQL Server database for downstream analytics and visualization in Power BI.

The dataset contains 21 raw CSV files with product and pricing information. These files were dirty and inconsistent, making them a great candidate for demonstrating a full ETL workflow.

🔧 Key Steps in the Project
1. Extract

Read in 21 raw .csv files from a local folder.

Used pandas for flexible and efficient data handling.

2. Transform

Applied several cleaning operations across all files:

Dropped unnecessary column: goods-title-link--jumphref.

Standardized and cleaned the price column:

Removed $ symbols.

Converted values from string → float.

Checked and reported missing values per dataset.

Ensured consistent schema across all files.

3. Load (Planned)

Prepared cleaned DataFrames for loading into SQL Server using SQLAlchemy + pyodbc.

Next steps: connect Power BI to SQL for reporting & visualization.

📂 Project Structure
Dirty-Ecommerce-ETL/
│
├── Dirty E-Commerce ETL Project.ipynb   # Jupyter Notebook with full ETL process
├── DataSource/                          # Folder containing raw CSV files (not uploaded to GitHub)
├── .gitignore                           # Ignores raw CSVs and unnecessary files
└── README.md                            # Project documentation

🛠️ Tech Stack

Python 🐍

pandas (data wrangling)

os & pathlib (file handling)

sqlalchemy + pyodbc (SQL Server integration)

SQL Server 🗄️ (target database)

Power BI 📊 (visualization layer – upcoming)

GitHub 🌍 (version control & collaboration)

🚀 How to Run

Clone this repository:

git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name


Install dependencies:

pip install pandas sqlalchemy pyodbc


Open the Jupyter notebook:

jupyter notebook "Dirty E-Commerce ETL Project.ipynb"


Run through the cells to clean all CSV files.

📊 Next Steps

Finalize SQL Server loading script.

Connect Power BI directly to SQL database.

Build dashboards to analyze pricing trends, product categories, and missing data patterns.

✨ Why This Project Matters

Real-world data is almost never clean. This project demonstrates:

Handling multiple dirty datasets efficiently.

Applying consistent cleaning transformations.

Automating reporting (missing values, schema consistency).

Preparing data for downstream analytics & BI integration.