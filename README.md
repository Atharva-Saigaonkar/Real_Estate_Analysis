# 🏠 Mumbai Real Estate Market Analysis

## 📌 Project Overview

The **Mumbai Real Estate Market Analysis** project focuses on exploring residential property data to understand housing prices, property characteristics, and locality-wise market trends across Mumbai.

Using Python, Pandas, and Matplotlib, this project involves data cleaning, exploratory data analysis (EDA), and data visualization to transform raw property listings into meaningful insights.

The analysis explores factors such as property prices, area, price per square foot, number of bedrooms and bathrooms, furnishing status, property age, and location.

This project demonstrates practical data analytics skills, including data preprocessing, data quality checks, statistical analysis, and visual storytelling.

## 🎯 Project Objectives

- Clean and prepare raw real estate data for analysis.
- Identify and handle duplicate records and missing values.
- Analyze property prices and price per square foot.
- Explore the relationship between property size and price.
- Compare property prices across different localities.
- Understand how property characteristics influence pricing.
- Create visualizations to communicate market trends.
- Generate insights that can support data-driven real estate decisions.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Jupyter Notebook | Interactive analysis and documentation |

## 📂 Dataset Description

The project uses a Mumbai real estate dataset containing property listing information.

The dataset includes the following attributes:

| Column | Description |
|---|---|
| `title` | Property listing title |
| `price` | Listed property price |
| `area` | Property area |
| `price_per_sqft` | Price per square foot |
| `locality` | Property locality |
| `city` | City associated with the listing |
| `property_type` | Type of property |
| `bedroom_num` | Number of bedrooms |
| `bathroom_num` | Number of bathrooms |
| `balcony_num` | Number of balconies |
| `furnished` | Furnishing status |
| `age` | Property age |
| `total_floors` | Total floors in the building |
| `latitude` | Geographic latitude |
| `longitude` | Geographic longitude |

These attributes enable analysis of property pricing, housing characteristics, and geographic differences across the market.

## 🔄 Project Workflow

### 1. Data Loading

The dataset is imported into a Pandas DataFrame for inspection and analysis.

Typical tasks include:
- Loading the source CSV file.
- Inspecting the first and last records.
- Checking dataset dimensions.
- Reviewing column names and data types.
- Examining summary statistics.

### 2. Data Cleaning

Data cleaning is an important step because incomplete or inconsistent records can affect the accuracy of the analysis.

The cleaning process includes:

- Standardizing column names.
- Checking for duplicate records.
- Removing duplicate entries where appropriate.
- Identifying missing values.
- Inspecting blank or whitespace-only text fields.
- Checking data types and numeric columns.
- Investigating unusually high or low property prices.
- Preparing the dataset for exploratory analysis.

Missing values should be handled according to the meaning of each column rather than automatically replacing every missing value.

### 3. Exploratory Data Analysis (EDA)

Exploratory data analysis helps uncover patterns, distributions, and relationships in the dataset.

Key areas of investigation include:

**Property price analysis**
- Distribution of property prices.
- Average and median property prices.
- Identification of unusually expensive or inexpensive listings.

**Area and pricing analysis**
- Relationship between property area and listed price.
- Comparison of price per square foot.
- Identification of differences between smaller and larger properties.

**Locality analysis**
- Comparison of property prices across localities.
- Identification of localities with relatively high or low listing prices.
- Exploration of geographic variation in the housing market.

**Property characteristics**
- Analysis by property type.
- Comparison by bedroom and bathroom counts.
- Examination of furnishing status and property age.

### 4. Data Visualization

Matplotlib is used to present patterns in an understandable visual format.

Potential visualizations include:

- Histograms for property price distributions.
- Bar charts for locality-wise price comparisons.
- Scatter plots for property area versus price.
- Box plots for comparing prices and identifying outliers.
- Bar charts for property type distributions.
- Correlation plots for selected numerical variables.

The final visualizations should be based on the analyses actually completed in the notebook.

## 📊 Key Analytical Questions

The project can help answer questions such as:

1. What is the typical listed price of a residential property?
2. How does property area relate to listed price?
3. Which localities have comparatively high property prices?
4. How does price per square foot vary across localities?
5. How are property prices distributed across the dataset?
6. Which property types are most common?
7. How do bedroom and bathroom counts relate to pricing?
8. How do furnishing status and property age vary across listings?
9. Are there extreme values or potential outliers in property prices?
10. What data quality issues need to be considered before drawing conclusions?

## 💡 Data Quality Considerations

Real estate datasets can contain incomplete listings, inconsistent measurements, duplicate records, and extreme prices.

During analysis, it is important to:

- Distinguish missing values from blank strings.
- Validate numerical columns before calculating statistics.
- Investigate extreme values before removing them.
- Check whether area measurements use consistent units.
- Avoid assuming that every listed price represents a completed transaction.
- Interpret locality comparisons in the context of sample sizes and property characteristics.

These checks help make the final findings more reliable and transparent.

## 🚀 Getting Started

### Prerequisites

Install Python 3 and the required libraries.

### Step 1: Clone the Repository

```bash
git clone https://github.com/Atharva-Saigaonkar/Real_Estate_Analysis.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Real_Estate_Analysis
```

### Step 3: Install Dependencies

```bash
pip install pandas numpy matplotlib jupyter
```

If the repository includes a `requirements.txt` file, you can instead install its listed dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Launch Jupyter Notebook

```bash
jupyter notebook
```

Open the project's notebook and execute the cells in order.

### Step 5: Load the Dataset

Ensure that the source CSV file is available at the path referenced in the notebook. Update the file path if necessary.

Example:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("your_dataset.csv")

print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
```

Replace `your_dataset.csv` with the actual dataset filename.

## 📈 Expected Outcomes

The analysis aims to produce:

- A cleaner and more consistent real estate dataset.
- A better understanding of property price distributions.
- Comparisons of listing prices and price per square foot.
- Insights into differences between localities.
- Visual exploration of property characteristics.
- A foundation for further real estate analytics and reporting.

Actual numerical findings should be added after validating the final cleaned dataset and visualizations.

## 🔮 Future Enhancements

Possible extensions include:

- Building an interactive dashboard using Power BI or Tableau.
- Adding geographic maps of property prices.
- Comparing locality-level price distributions.
- Developing a house price prediction model using machine learning.
- Creating automated data quality reports.
- Adding SQL-based analysis to complement Python.
- Publishing the analysis as an interactive Streamlit application.

## 🧠 Key Learnings

This project provides practical experience in:

- Python-based data analysis.
- Data cleaning and preprocessing.
- Pandas DataFrame operations.
- Missing-value and duplicate handling.
- Descriptive statistics.
- Exploratory data analysis.
- Data visualization with Matplotlib.
- Interpreting real-world property listing data.
- Communicating analytical findings.

## 👨‍💻 Author

**Atharva Saigaonkar**

Computer Engineering Graduate | Aspiring Data Analyst

- GitHub: [Atharva-Saigaonkar](https://github.com/Atharva-Saigaonkar)
- Project Repository: [Mumbai Real Estate Market Analysis](https://github.com/Atharva-Saigaonkar/Real_Estate_Analysis)

---

⭐ If you find this project useful, feel free to explore the repository and share feedback.
