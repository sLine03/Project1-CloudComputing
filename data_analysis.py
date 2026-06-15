import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

# Load the dataset

df = pd.read_csv('All_Diets.csv')

# Handle missing data (fill missing values with mean)

numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Calculate the average macronutrient content for each diet type

avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()

# Find the top 5 protein-rich recipes for each diet type

top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)

# Add new metrics (Protein-to-Carbs ratio and Carbs-to-Fat ratio)

df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)']

df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)']


# Bar chart for average macronutrients

sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'])

plt.title('Average Protein by Diet Type')

plt.ylabel('Average Protein (g)')

plt.show()
# Bar chart for average protein
plt.figure(figsize=(10, 6))

sns.barplot(x=avg_macros.index, y=avg_macros["Protein(g)"])

plt.title("Average Protein by Diet Type")
plt.xlabel("Diet Type")
plt.ylabel("Average Protein (g)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("average_protein_by_diet.png")

print("Data analysis completed successfully.")
print("\nAverage Macronutrients by Diet Type:")
print(avg_macros)

print("\nTop 5 Protein-Rich Recipes by Diet Type:")
print(top_protein[["Diet_type", "Recipe_name", "Protein(g)"]])

print("\nChart saved as average_protein_by_diet.png")