import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset
df= pd.read_csv('data.csv')

#Data cleaning and preprocessing
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df = df.drop_duplicates() #it will remove the duplicate rows from the dataset


# Numerical Columns Cleaning
#print(df.info())
df['price'] = df["price"].astype(str).str.replace(",", "").astype(float)
df['area'] = df["area"].astype(str).str.replace(",", "").astype(int)
df['rate_per_sqft'] = df['rate_per_sqft'].astype(str).str.replace(",", "").astype(int)

# Categorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()

#1. Which is the costliest flat in the dataset?
costliest_flat = df.loc[df['price'].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK flat located in {costliest_flat['locality']} priced at {costliest_flat['price']/10000000} crores in {costliest_flat['society']} society.") 

#2. Which locality has the highest average price?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax() #groupby() is used to group the data by 'locality' and then calculate the mean price for each locality. idxmax() is used to find the index of the locality with the highest average price.
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

#3 Which society has the most number of flats listed?
most_listed_society = df['society'].value_counts().idxmax() 
print(f"The society with the most number of flats listed is {most_listed_society}.")

#4. Do ready-to-move properties cost more than under-construction properties?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
print(f"Average price of ready-to-move properties: {ready_to_move_avg_price/10000000:.2f} crores")
print(f"Average price of under-construction properties: {under_construction_avg_price/10000000:.2f} crores")
if ready_to_move_avg_price > under_construction_avg_price:
    print("Ready-to-move properties cost more on average than under-construction properties.")
else:
    print("Under-construction properties cost more on average than ready-to-move properties.")


#5. Which locality has the highest average price?
highest_avg_price_locality = df.groupby("locality")["price"].mean().sort_values(ascending=False).index[0]

#6. Do RERA-approved properties command a price premium?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
not_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > not_rera_approved_avg_price:
    print("RERA-approved properties command a price premium.")
else:   
    print("RERA-approved properties do not command a price premium.")

#7. How does area (sqft) impact property price?
sns.boxplot(data=df, x='area', y='price')
plt.title('Area vs Price')              
plt.xlabel('Area (sqft)')
plt.ylabel('Price (in crores)')
plt.show()

#8. Are larger homes more expensive per sqft?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
sns.regplot(data=df,
            x='area',
            y='rate_per_sqft',
            scatter=False,
            color='red')

plt.title('Area vs Rate per Sqft')
plt.xlabel('Area (sqft)')       
plt.ylabel('Rate per Sqft')
plt.show()

#9.Which property type is the costliest?
most_expensive_property_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")

#10. Which BHK configuration is most expensive based on per sqft rate?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration on average is {most_expensive_bhk} BHK.")

#11. How does the price distribution look across different localities?
plt.figure(figsize=(15, 6))
plt.title('Price Distribution Across Localities')
sns.boxplot(data=df, x='locality', y='price')
plt.xlabel('Locality')      
plt.ylabel('Price (in crores)')
plt.show()
