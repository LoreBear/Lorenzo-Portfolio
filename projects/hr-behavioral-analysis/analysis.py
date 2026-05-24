import kagglehub
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# 1. AUTOMATIC DATA DOWNLOAD FROM KAGGLE
# Downloads the latest version of the "rhuebner/human-resources-data-set"
path = kagglehub.dataset_download("rhuebner/human-resources-data-set")
print("Dataset downloaded to: " + path)

# Locate the CSV file in the downloaded folder
csv_path = os.path.join(path, "HRDataset_v14.csv")
df = pd.read_csv(csv_path)

# 2. DEFINE OUTPUT PATH (current project folder)
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts')

# Ensure the directory exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Professional graphical settings
sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 300

# --- CREATE BINARY ATTRITION COLUMN ---
df['Attrition_Num'] = df['Termd'].astype(int)

# --- ANALYSIS A: TERMINATION REASONS (Occupational Psychology) ---
plt.figure(figsize=(10, 8))
terminated = df[df['TermReason'] != 'N/A-StillEmployed']
sns.countplot(data=terminated, y='TermReason', order=terminated['TermReason'].value_counts().index, palette='magma')
plt.title('Deep Dive: Why are employees leaving the company?', fontsize=14)
plt.xlabel('Number of Employees')
plt.ylabel('Reason for Termination')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_termination_reasons.png'))
plt.close()

# --- ANALYSIS B: GENDER PAY EQUITY (DEI) ---
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Department', y='Salary', hue='Sex', palette='Set2')
plt.xticks(rotation=45)
plt.title('Salary Equity Analysis by Department & Gender', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_gender_pay_equity.png'))
plt.close()

# --- ANALYSIS C: ENGAGEMENT VS. ABSENTEEISM (Burnout Risk) ---
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='EngagementSurvey', y='Absences', hue='PerformanceScore', s=100)
plt.title('Correlation: Engagement Score vs. Absenteeism', fontsize=14)
plt.xlabel('Engagement Survey Score')
plt.ylabel('Number of Absences')
plt.legend(title='Performance Score', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_engagement_vs_absences.png'))
plt.close()

# --- ANALYSIS D: % ATTRITION BY JOB ROLE ---
attrition_by_role = df.groupby('Position')['Attrition_Num'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
attrition_by_role.plot(kind='bar', color='steelblue')
plt.title('% Attrition by Job Role', fontsize=14)
plt.ylabel('Attrition Rate')
plt.xlabel('Job Role')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'hr_attrition_by_jobrole.png'))
plt.close()

# 3. EXPORT CLEANED DATA FOR POWER BI
df['Sex'] = df['Sex'].str.strip()
df['Department'] = df['Department'].str.strip()
cleaned_csv_path = os.path.join(output_folder, "data_cleaned.csv")
df.to_csv(cleaned_csv_path, index=False)

print("\nAnalysis complete!")
print("Charts and cleaned CSV saved in: " + output_folder)