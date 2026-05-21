# ============================================================
# Data Cleaning & Visualization Project
# Dataset: Titanic (from GitHub)
# Libraries: Pandas, Matplotlib, Seaborn
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# STEP 1: LOAD DATASET
# ============================================================

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print("=" * 50)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)
print(f"Shape: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# ============================================================
# STEP 2: DATA CLEANING
# ============================================================

print("\n" + "=" * 50)
print("STEP 2: DATA CLEANING")
print("=" * 50)

print("\nMissing Values BEFORE Cleaning:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"\nDuplicates Removed: {before - after}")

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['Age'] >= Q1 - 1.5 * IQR) & (df['Age'] <= Q3 + 1.5 * IQR)]

print("\nMissing Values AFTER Cleaning:")
print(df.isnull().sum())
print(f"\nFinal Dataset Shape: {df.shape}")

# ============================================================
# STEP 3: VISUALIZATIONS
# ============================================================

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle('Titanic Dataset - Data Visualization', fontsize=18, fontweight='bold', y=1.02)

# Plot 1: Survival Count
sns.countplot(x='Survived', data=df, palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('Survival Count', fontsize=13, pad=12)
axes[0, 0].set_xticklabels(['Not Survived (0)', 'Survived (1)'])
axes[0, 0].set_xlabel('Survival Status')
axes[0, 0].set_ylabel('Count')

# Plot 2: Age Distribution
sns.histplot(df['Age'], bins=30, kde=True, color='steelblue', ax=axes[0, 1])
axes[0, 1].set_title('Age Distribution', fontsize=13, pad=12)
axes[0, 1].set_xlabel('Age')
axes[0, 1].set_ylabel('Frequency')

# Plot 3: Survival by Gender
sns.countplot(x='Sex', hue='Survived', data=df, palette='Set1', ax=axes[0, 2])
axes[0, 2].set_title('Survival by Gender', fontsize=13, pad=12)
axes[0, 2].set_xlabel('Gender')
axes[0, 2].set_ylabel('Count')
axes[0, 2].legend(['Not Survived', 'Survived'])

# Plot 4: Passenger Class Distribution
sns.countplot(x='Pclass', data=df, palette='pastel', ax=axes[1, 0])
axes[1, 0].set_title('Passenger Class Distribution', fontsize=13, pad=12)
axes[1, 0].set_xlabel('Class')
axes[1, 0].set_ylabel('Count')

# Plot 5: Fare Boxplot by Class
sns.boxplot(x='Pclass', y='Fare', data=df, palette='coolwarm', ax=axes[1, 1])
axes[1, 1].set_title('Fare Distribution by Class', fontsize=13, pad=12)
axes[1, 1].set_xlabel('Passenger Class')
axes[1, 1].set_ylabel('Fare')

# Plot 6: Correlation Heatmap
corr = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1, 2])
axes[1, 2].set_title('Correlation Heatmap', fontsize=13, pad=12)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig('titanic_visualization.png', dpi=150, bbox_inches='tight')
plt.show()
print("\nVisualization saved as 'titanic_visualization.png'")

# ============================================================
# STEP 4: KEY INSIGHTS
# ============================================================

print("\n" + "=" * 50)
print("STEP 4: KEY INSIGHTS")
print("=" * 50)

survival_rate = df['Survived'].mean() * 100
print(f"Overall Survival Rate     : {survival_rate:.2f}%")

female_survival = df[df['Sex'] == 'female']['Survived'].mean() * 100
male_survival = df[df['Sex'] == 'male']['Survived'].mean() * 100
print(f"Female Survival Rate      : {female_survival:.2f}%")
print(f"Male Survival Rate        : {male_survival:.2f}%")

avg_age = df['Age'].mean()
print(f"Average Age of Passengers : {avg_age:.1f} years")

avg_fare = df['Fare'].mean()
print(f"Average Fare              : ${avg_fare:.2f}")

print("\n Project Complete!")
print("Output saved: titanic_visualization.png")