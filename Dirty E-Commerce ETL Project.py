#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


Path = "C:/Users/DELL/OneDrive/Documents/ETL/DataSource"


# ### 1. Data Extraction

# In[3]:


# Data Extraction
def data_extract(data_dir = Path):
    dfs = []
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            path = os.path.join(data_dir, file)
            
            # Read csv file
            df = pd.read_csv(path)

            # Extract Category from filename
            category = file.split("-")[2] if "-" in file else "unknown"
            df["category"] = category
            df["source_file"] = file
            dfs.append(df)
            
    return dfs

dfs = data_extract()
print(f"extracted {len(dfs)} files")


# ### 2. Data Transformation

# > Before we begin transforming, let's randomly look at just 3 of the 21 datasets

# In[4]:


# Display 3 of the 21 files
file1 = "C:/Users/DELL/OneDrive/Documents/ETL/DataSource/us-shein-appliances-3987.csv"
file2 = "C:/Users/DELL/OneDrive/Documents/ETL/DataSource/us-shein-automotive-4110.csv"
file3 = "C:/Users/DELL/OneDrive/Documents/ETL/DataSource/us-shein-baby_and_maternity-4433.csv"

# Load the 3 files
df1 = pd.read_csv(file1, low_memory = False)
df2 = pd.read_csv(file2, low_memory = False)
df3 = pd.read_csv(file3, low_memory = False)

# Display shape (rows and columns)
print("appliances", df1.shape)
print("automotive", df2.shape)
print("baby_and_maternity", df3.shape)


# #### Displaying first 2 rows

# In[5]:


print("Sample from appliances:")
print(df1.head(2))

print("Sample from automotive:")
print(df2.head(2))


# In[6]:


# Checking for missing values

print("Missing values from appliances:")
print(df1.isnull().sum())
print()
print("Missing values from automotive:")
print(df2.isnull().sum())


# ## Findings
# ### Duplicate Columns
# >> The columns "goods-title-link--jump", "goods-title-link--jump href" and "goods-title-link" all contain the same information per row. 
# ### Missing Values
# >>The rows with missing values in "goods-title-link--jump" have its correct values in "goods-title-link" and vice versa. The "goods-title-link--jump" column will be filled up, and then the other two will be deleted for all the datasets.
# ### Miscellaneous
# >> The column titles will be standardized and made uniform across all datasets
# >> The "price" column is of string type and has "dollar" symbol, this will be removed & converted to float. 

# In[7]:


def clean_df(df):
    # Standardize column names
    df.columns = [c.strip().lower().replace(" ", (_)) for c in df.columns]
    
    # if both columns exist, merge them
    if "goods-title-link--jump" in df.columns and "goods-title-link" in df.columns:
        df["goods-title-link--jump"] = df["goods-title-link--jump"].fillna(df["goods-title-link"])
        
    elif "goods-title-link" in df.columns and "goods-title-link--jump" not in df.columns:
        # Rename "goods-title-link" to "goods-title-link--jump" for consistency
        df = df.rename(columns = {"goods-title-link":"goods-title-link--jump"})
        
    # Drop any complete empty columns
    df = df.dropna(axis = 1, how = "all")
    # Drop "goods-title-link--jump href"
    cols_to_drop = ["goods-title-link--jump href", "goods-title-link--jumphref", "goods-title-link"]
    df = df.drop(columns = [ col for col in cols_to_drop if col in df.columns], errors = "ignore")
    
    # Drop "$" symbol on price column and convert value from string to float
    if "price" in df.columns:
        df["price"] = (
            df["price"]
            .astype(str) # to ensure type string
            .str.replace(r"[\$,]", "", regex = True) # replace "$" and ","
            .replace("", None) # handle empty string
            .astype(float)
        
        )
        
    return df


# In[8]:


# Print missing values
def missing_values(df, name):
    print(f"missing values from {name}:")
    print(df.isnull().sum())
    print("\n" + "="*50 + "\n")
    
    # Loop through the 21 csv files, clean and print missing values
    
all_dataframes = {}

files = [f for f in os.listdir(Path) if f.endswith(".csv")]
print(f"Found {len(files)} CSV files\n")
for idx, file in enumerate(files, start = 1):
    file_path = os.path.join(Path, file)

    # Load CSV
    df = pd.read_csv(file_path, low_memory = False)
            
    # Clean the CSV
    df_clean = clean_df(df)
            
    # Save in dictionary for later SQL loading
    name = os.path.splitext(file)[0] # [0] filename without extension  
    all_dataframes[name] = df_clean
            
    # Print missing values report
    print(f"processing files {idx}/{len(files)}: {file}")
    missing_values(df_clean, name)
        


# In[ ]:




