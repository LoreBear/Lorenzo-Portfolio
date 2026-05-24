import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- 1. Setup paths ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts')
os.makedirs(output_folder, exist_ok=True)

# File paths for charts
heatmap_path = os.path.join(output_folder, 'chart_correlation_heatmap.png')
dept_path = os.path.join(output_folder, 'chart_attrition_by_dept.png')
income_path = os.path.join(output_folder, 'chart_income_impact.png')
overtime_path = os.path.join(output_folder, 'chart_overtime_impact.png')
satisfaction_path = os.path.join(output_folder, 'chart_satisfaction_impact.png')

# --- 2. Load dataset ---
try:
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("ERROR: CSV file not found. Ensure it is in the same directory.")
    exit()

# --- 3. Prepare numeric mapping for Attrition ---
df['Attrition_Num'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# --- 4. Correlation Heatmap ---
numeric_df = df.select_dtypes(include=[np.number]).copy()
numeric_df = numeric_df.loc[:, numeric_df.nunique() > 1]  # Remove constant columns

if numeric_df.shape[1] >= 2:
    corr_matrix = numeric_df.corr()
    plt.figure(figsize=(14, 12))
    sns.heatmap(
        corr_matrix,
        annot=True,
        fmt=".2f",
        cmap='coolwarm',
        center=0,
        linewidths=0.5,
        linecolor='white'
    )
    plt.title('IBM HR Correlation Heatmap', fontsize=16)
    plt.tight_layout()
    plt.savefig(heatmap_path, dpi=150)
    plt.show()
    plt.close()
    print(f"Heatmap saved at: {heatmap_path}")
else:
    print("Not enough numeric columns to generate heatmap.")

# --- 5. Attrition by Department ---
plt.figure(figsize=(10, 6))
sns.countplot(x='Department', hue='Attrition', data=df, palette='viridis')
plt.title('Attrition Distribution by Department')
plt.tight_layout()
plt.savefig(dept_path)
plt.close()
print(f"Attrition by Department chart saved at: {dept_path}")

# --- 6. Salary vs Attrition ---
plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df, palette='coolwarm')
plt.title('Impact of Monthly Income on Attrition')
plt.tight_layout()
plt.savefig(income_path)
plt.close()
print(f"Income vs Attrition chart saved at: {income_path}")

# --- 7. Overtime vs Attrition ---
plt.figure(figsize=(8, 5))
sns.barplot(x='OverTime', y='Attrition_Num', data=df, palette='magma')
plt.title('Attrition Probability: Overtime vs No Overtime')
plt.tight_layout()
plt.savefig(overtime_path)
plt.close()
print(f"Overtime Impact chart saved at: {overtime_path}")

# --- 8. Job Satisfaction vs Attrition ---
ct = pd.crosstab(df['JobSatisfaction'], df['Attrition'], normalize='index')
ct.plot(kind='bar', stacked=True, figsize=(10, 6), color=['#4daf4a', '#e41a1c'])
plt.title('Job Satisfaction Level vs Attrition')
plt.legend(title='Left Company?', loc='upper right')
plt.tight_layout()
plt.savefig(satisfaction_path)
plt.close()
print(f"Job Satisfaction chart saved at: {satisfaction_path}")

print("\n--- All charts generated and saved in the 'charts/' folder ---")
