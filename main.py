import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

# print(df.head())
# print(df.columns.tolist())

# print(df.info())

# # Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')
# print(df.columns.tolist())

# # Check for duplicate rows
# print(df.duplicated().sum())
# print("Before:", df.shape)
# df = df.drop_duplicates()
# print("After:", df.shape)

# # Check unique values
# print(df["property_type"].unique())
# print(df["furnished"].unique())

# #Validate Data
# print(df[df["price"] <= 0])
# print(df[df["area"] <= 0])

# df = df[df["property_type"] != "Studio Apartment"]
# print(df["property_type"].value_counts())
# print(df[df["bedroom_num"] <= 0])


# print(df[df["bathroom_num"] <= 0])

# print(df["price"].describe())
# print(df["area"].describe())
# print(df["price_per_sqft"].describe())

# print(df["title"].isnull().sum())
# print((df["title"] == "").sum())
# print((df["title"].str.strip() == "").sum())

# df["title"] = df["title"].replace(r'^\s*$', "Unknown Property", regex=True)
# print((df["title"].str.strip() == "").sum())

## saving the cleaned data to a new CSV file
# df.to_csv("data.csv", index=False)


#Questions to answer:
# 1. Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat in Mumbai is located at {costliest_flat['locality']} with a price of {costliest_flat['price']} and has {costliest_flat['bedroom_num']} bedrooms and {costliest_flat['bathroom_num']} bathrooms.")

# 2. Which locality has the highest average price?
print(f"The Locality with the highest average price is {df.groupby('locality')['price'].mean().idxmax()} with an average price of {df.groupby('locality')['price'].mean().max()/10000000} Crores.")

# 3. Which Locality has the highest rate per square foot(Expensive)?
print(f"The Locality with the highest rate per square foot is {df.groupby('locality')['price_per_sqft'].mean().idxmax()} with an average rate of {df.groupby('locality')['price_per_sqft'].mean().max()} per sq ft.")

# 4. Which Locality has the highest number of properties listed?
print(f"The locality with the highest numbers of properties listed is {df['locality'].value_counts().idxmax()} with {df['locality'].value_counts().max()} proprties listed.")

# 5. Which Locality has the highest number of furnished properties listed?
print(f"The locality with the highest numbers of furnished properties listed is {df[df['furnished'].isin(['Furnished','Semi-Furnished'])]['locality'].value_counts().idxmax()} with {df[df['furnished'].isin(['Furnished','Semi-Furnished'])]['locality'].value_counts().max()} furnished properties listed.")

# 6. Which Locality has the highest number of 1BHK properties listed?
print(f"The locality with the highest numbers of 1BHK properties listed is {df[df['bedroom_num'] == 1]['locality'].value_counts().idxmax()} with {df[df['bedroom_num'] == 1]['locality'].value_counts().max()} 1BHK properties listed.")

# 7. Which Locality has the highest number of 2BHK properties listed?
print(f"The locality with the highest numbers of 2BHK properties listed is {df[df['bedroom_num'] == 2]['locality'].value_counts().idxmax()} with {df[df['bedroom_num'] == 2]['locality'].value_counts().max()} 2BHK properties listed.")

# 8. Which locality have the lowest average price per square foot(Value for Money)?
print(f"The Locality with the lowest average price per square foot is {df.groupby('locality')['price_per_sqft'].mean().idxmin()} with an average rate of {df.groupby('locality')['price_per_sqft'].mean().min()} per sq ft.")

# 9. How much does furnishing affect property prices?
print(f"The average price of furnished properties is {df[df['furnished'].isin(['Furnished','Semi-Furnished'])]['price'].mean()/10000000} Crores, while the average price of unfurnished properties is {df[df['furnished'] == 'Unfurnished']['price'].mean()/10000000} Crores. This indicates that furnished properties are generally more expensive than unfurnished ones.")

# 10. Which localities have the highest concentration of luxury properties?
print(f"The locality with the highest concentration of luxury properties (price > 5 Crores) is {df[df['price'] > 50000000]['locality'].value_counts().idxmax()} with {df[df['price'] > 50000000]['locality'].value_counts().max()} luxury properties listed.")

# 11. Which property type provides the most space for the money?
print(f"The property type that provides the most space for the money (lowest price per square foot) is {df.groupby('property_type')['price_per_sqft'].mean().idxmin()} with an average rate of {df.groupby('property_type')['price_per_sqft'].mean().min()} per sq ft.")

# 12. How does area impact price?
sns.scatterplot(data=df, x='area',y='price')
plt.show()

#13. 


