import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime

# --- Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts')
os.makedirs(output_folder, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 150

# --- Load Dataset ---
df = pd.read_csv('HRDataset_v14.csv')
print(f"Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Cleaning & Preparation ---
# Calculate age from DOB
df['DOB'] = pd.to_datetime(df['DOB'], format='%m/%d/%y')
df['age'] = (datetime.now() - df['DOB']).dt.days // 365.25
df['age'] = df['age'].astype(int)

# Create gender identifier (using Sex column)
df['is_female'] = (df['Sex'].str.strip() == 'F').astype(int)

# Create ethnicity identifier (combining HispanicLatino and RaceDesc)
df['is_ethnic_minority'] = (
    (df['HispanicLatino'].str.strip() == 'Yes') |
    (~df['RaceDesc'].str.strip().isin(['White']))
).astype(int)

# Note: Disability and LGBTQ status not available in this dataset
df['has_disability'] = 0  # Placeholder - not in dataset
df['is_lgbtq'] = 0        # Placeholder - not in dataset

# Create attrition identifier (using EmploymentStatus)
df['attrition_bool'] = (df['EmploymentStatus'].str.strip() == 'Voluntarily Terminated').astype(int)

# Ensure proper numeric types - handle non-numeric values gracefully
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')
# For categorical scores, we'll keep them as strings for now or convert to numeric ratings if needed
# PerformanceScore, EngagementSurvey, EmpSatisfaction contain text like "Exceeds", "Fully Meets", etc.
# We'll leave them as categorical for now, but could map to numeric values if needed for analysis

# --- KEY STATS ---
total_employees = len(df)
female_pct = df['is_female'].mean() * 100
ethnic_minority_pct = df['is_ethnic_minority'].mean() * 100
disability_pct = 0  # Not available in dataset
lgbtq_pct = 0       # Not available in dataset

print(f"\nTotal Employees: {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}%")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# --- CHART 1: Gender Distribution by Department ---
dept_order = sorted(df['Department'].unique())
gender_order = ['Female', 'Male']

# Create crosstab for gender by department
gender_dept = pd.crosstab(df['Department'], df['Sex'].str.strip(), normalize='index') * 100
gender_dept = gender_dept.reindex(dept_order)  # Ensure order
gender_dept = gender_dept.reindex(columns=['F', 'M'])  # Ensure gender order

plt.figure(figsize=(14, 8))
gender_dept.plot(kind='bar', stacked=True)
plt.title('Gender Distribution by Department (%)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('% of Employees', fontsize=12)
plt.legend(title='Gender', labels=['Female', 'Male'], bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars (only for segments > 5%)
for i, (dept, row) in enumerate(gender_dept.iterrows()):
    cumulative = 0
    for j, gender in enumerate(['F', 'M']):
        if gender in row.index:
            value = row[gender]
            if value > 5:  # Only show label if percentage > 5%
                plt.text(i, cumulative + value/2, f'{value:.0f}%',
                        ha='center', va='center', fontweight='bold',
                        color='white' if value > 30 else 'black')
            cumulative += value

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_gender_department.png'), bbox_inches='tight')
plt.close()
print("Chart 1 saved: chart_gender_department.png")

# --- CHART 2: Attrition by Demographic Group ---
# Calculate attrition rates
attrition_by_gender = df.groupby('Sex')['attrition_bool'].mean() * 100
attrition_by_ethnicity = df.groupby('RaceDesc')['attrition_bool'].mean() * 100
attrition_by_disability = pd.Series([0, 0], index=['No disability', 'Has disability']) * 100  # Placeholder
attrition_by_lgbtq = pd.Series([0, 0], index=['Not LGBTQ+', 'LGBTQ+']) * 100  # Placeholder

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gender attrition
# Sort by attrition rate for better visualization
attrition_by_gender_sorted = attrition_by_gender.sort_values(ascending=False)
axes[0,0].bar(attrition_by_gender_sorted.index, attrition_by_gender_sorted.values,
              edgecolor='white', linewidth=0.8)
axes[0,0].set_title('Attrition Rate by Gender (%)', fontweight='bold', fontsize=14)
axes[0,0].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_gender_sorted.values):
    axes[0,0].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

# Ethnicity attrition (top 8 ethnicities for readability)
top_ethnicities = attrition_by_ethnicity.nlargest(8).index
attrition_by_ethnicity_top = attrition_by_ethnicity[top_ethnicities]
axes[0,1].bar(range(len(attrition_by_ethnicity_top)), attrition_by_ethnicity_top.values,
              edgecolor='white', linewidth=0.8)
axes[0,1].set_title('Attrition Rate by Ethnicity (Top 8) (%)', fontweight='bold', fontsize=14)
axes[0,1].set_ylabel('Attrition Rate (%)', fontsize=12)
axes[0,1].set_xticks(range(len(attrition_by_ethnicity_top)))
axes[0,1].set_xticklabels(attrition_by_ethnicity_top.index, rotation=45, ha='right')
for i, v in enumerate(attrition_by_ethnicity_top.values):
    axes[0,1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

# Disability attrition (placeholder)
axes[1,0].bar(['No disability', 'Has disability'], attrition_by_disability.values,
              edgecolor='white', linewidth=0.8)
axes[1,0].set_title('Attrition Rate by Disability Status (%) (Data Not Available)', fontweight='bold', fontsize=14)
axes[1,0].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_disability.values):
    axes[1,0].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

# LGBTQ+ attrition (placeholder)
axes[1,1].bar(['Not LGBTQ+', 'LGBTQ+'], attrition_by_lgbtq.values,
              edgecolor='white', linewidth=0.8)
axes[1,1].set_title('Attrition Rate by LGBTQ+ Status (%) (Data Not Available)', fontweight='bold', fontsize=14)
axes[1,1].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_lgbtq.values):
    axes[1,1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_attrition_demographic.png'), bbox_inches='tight')
plt.close()
print("Chart 2 saved: chart_attrition_demographic.png")

# --- CHART 3: Representation Trends Over Years (Hire Years) ---
# Calculate hire year from DateofHire
df['DateofHire'] = pd.to_datetime(df['DateofHire'], format='%m/%d/%Y')
df['hire_year'] = df['DateofHire'].dt.year

# Calculate yearly hiring trends for underrepresented groups
yearly_trends = df.groupby('hire_year').agg({
    'is_female': 'mean',
    'is_ethnic_minority': 'mean',
    'has_disability': 'mean',
    'is_lgbtq': 'mean',
}) * 100

yearly_trends = yearly_trends.round(2)

plt.figure(figsize=(12, 6))
yearly_trends.plot(kind='line', marker='o', linewidth=2.5, markersize=8)
plt.title('Representation Trends Over Hire Years', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Hire Year', fontsize=12)
plt.ylabel('Representation (%)', fontsize=12)
plt.legend(title='Demographic Group', labels=['Female', 'Ethnic Minority', 'Has Disability', 'LGBTQ+'],
           bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_representation_trends.png'), bbox_inches='tight')
plt.close()
print("Chart 3 saved: chart_representation_trends.png")

# --- CHART 4: Salary Analysis by Gender and Ethnicity ---
plt.figure(figsize=(14, 8))

# Prepare data for salary boxplot by gender
gender_order_for_box = ['F', 'M']  # Female, Male
gender_data = [df[df['Sex'].str.strip() == gender]['Salary'].values for gender in gender_order_for_box if gender in df['Sex'].str.strip().unique()]
gender_labels = ['Female' if g == 'F' else 'Male' for g in gender_order_for_box if g in df['Sex'].str.strip().unique()]

box_plot = plt.boxplot(gender_data, labels=gender_labels, patch_artist=True)
plt.title('Salary Distribution by Gender', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Salary (Currency Units)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Color boxes
colors = ['#ff7f0e', '#1f77b4']
for patch, color in zip(box_plot['boxes'], colors[:len(box_plot['boxes'])]):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Add mean values as points
means = [df[df['Sex'].str.strip() == gender]['Salary'].mean() for gender in gender_order_for_box if gender in df['Sex'].str.strip().unique()]
for i, mean in enumerate(means):
    plt.plot(i+1, mean, 'D', color='black', markersize=8)

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_salary_gender.png'), bbox_inches='tight')
plt.close()
print("Chart 4 saved: chart_salary_gender.png")

# --- SUMMARY STATS ---
print("\n=== SUMMARY FOR README ===")
print(f"Total Employees: {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}%")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# Attrition analysis
overall_attrition = df['attrition_bool'].mean() * 100
female_attrition = df[df['Sex'].str.strip() == 'F']['attrition_bool'].mean() * 100 if 'F' in df['Sex'].str.strip().values else 0
male_attrition = df[df['Sex'].str.strip() == 'M']['attrition_bool'].mean() * 100 if 'M' in df['Sex'].str.strip().values else 0
print(f"\nOverall Attrition Rate: {overall_attrition:.1f}%")
if female_attrition > 0 and male_attrition > 0:
    print(f"Female Attrition Rate: {female_attrition:.1f}%")
    print(f"Male Attrition Rate: {male_attrition:.1f}%")
    print(f"Attrition Ratio (Female/Male): {female_attrition/male_attrition:.2f}")
else:
    print(f"Female Attrition Rate: {female_attrition:.1f}%")

# Salary analysis
if 'F' in df['Sex'].str.strip().values and 'M' in df['Sex'].str.strip().values:
    male_avg_salary = df[df['Sex'].str.strip() == 'M']['Salary'].mean()
    female_avg_salary = df[df['Sex'].str.strip() == 'F']['Salary'].mean()
    gender_pay_gap = male_avg_salary - female_avg_salary
    gender_pay_gap_pct = (gender_pay_gap / male_avg_salary) * 100 if male_avg_salary > 0 else 0
    print(f"\nAverage Male Salary: {male_avg_salary:.0f}")
    print(f"Average Female Salary: {female_avg_salary:.0f}")
    print(f"Gender Pay Gap: {gender_pay_gap:.0f} currency units")
    print(f"Gender Pay Gap Percentage: {gender_pay_gap_pct:.1f}%")
else:
    print("\nGender salary comparison not available (missing Female or Male data)")

# Representation trends
if len(yearly_trends) >= 2:
    years = sorted(yearly_trends.index)
    first_year = years[0]
    last_year = years[-1]
    female_change = yearly_trends.loc[last_year, 'is_female'] - yearly_trends.loc[first_year, 'is_female']
    ethnic_change = yearly_trends.loc[last_year, 'is_ethnic_minority'] - yearly_trends.loc[first_year, 'is_ethnic_minority']
    disability_change = 0  # Not available
    lgbtq_change = 0       # Not available
    print(f"\nRepresentation Change ({first_year} to {last_year}):")
    print(f"  Female: {female_change:+.1f} percentage points")
    print(f"  Ethnic Minority: {ethnic_change:+.1f} percentage points")
    print(f"  Disability: {disability_change:+.1f} percentage points (data not available)")
    print(f"  LGBTQ+: {lgbtq_change:+.1f} percentage points (data not available)")

print("\nAll charts generated successfully!")