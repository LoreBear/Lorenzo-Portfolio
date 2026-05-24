import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts')
os.makedirs(output_folder, exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams['figure.dpi'] = 150

# --- Load REAL Dataset ---
df = pd.read_csv('real_dei_data.csv')
print(f"Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Cleaning & Preparation ---
# Ensure proper data types
df['hire_year'] = df['hire_year'].astype(int)
df['performance_rating'] = pd.to_numeric(df['performance_rating'])
df['salary'] = pd.to_numeric(df['salary'])
df['attrition'] = df['attrition'].astype(bool)

# Create demographic group identifiers for analysis
df['is_female'] = (df['gender'] == 'Female').astype(int)
df['is_ethnic_minority'] = (~df['ethnicity'].isin(['White'])).astype(int)  # Assuming White is majority
df['has_disability'] = (df['disability_status'] == 'Has disability').astype(int)
df['is_lgbtq'] = (df['lgbtq_status'] == 'LGBTQ+').astype(int)

# --- KEY STATS ---
total_employees = len(df)
female_pct = (df['gender'] == 'Female').mean() * 100
ethnic_minority_pct = (~df['ethnicity'].isin(['White'])).mean() * 100
disability_pct = (df['disability_status'] == 'Has disability').mean() * 100
lgbtq_pct = (df['lgbtq_status'] == 'LGBTQ+').mean() * 100

print(f"\nTotal Employees: {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}%")
print(f"Employees with Disability: {disability_pct:.1f}%")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}%")

# --- CHART 1: Gender Distribution by Division (instead of Region since we don't have region) ---
division_order = sorted(df['division'].unique())
gender_order = ['Female', 'Male', 'Non-binary', 'Transgender', 'Prefer not to say']

# Create crosstab for gender by division
gender_division = pd.crosstab(df['division'], df['gender'], normalize='index') * 100
gender_division = gender_division.reindex(division_order)  # Ensure order

plt.figure(figsize=(14, 8))
gender_division.plot(kind='bar', stacked=True)
plt.title('Gender Distribution by Division (%)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Division', fontsize=12)
plt.ylabel('% of Employees', fontsize=12)
plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars (only for segments > 5%)
for i, (division, row) in enumerate(gender_division.iterrows()):
    cumulative = 0
    for gender in gender_order:
        if gender in row.index:
            value = row[gender]
            if value > 5:  # Only show label if percentage > 5%
                plt.text(i, cumulative + value/2, f'{value:.0f}%',
                        ha='center', va='center', fontweight='bold',
                        color='white' if value > 30 else 'black')
            cumulative += value

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_gender_division.png'), bbox_inches='tight')
plt.close()
print("Chart 1 saved: chart_gender_division.png")

# --- CHART 2: Attrition by Demographic Group ---
# Calculate attrition rates
attrition_by_gender = df.groupby('gender')['attrition'].mean() * 100
attrition_by_ethnicity = df.groupby('ethnicity')['attrition'].mean() * 100
attrition_by_disability = df.groupby('disability_status')['attrition'].mean() * 100
attrition_by_lgbtq = df.groupby('lgbtq_status')['attrition'].mean() * 100

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

# Disability attrition
axes[1,0].bar(attrition_by_disability.index, attrition_by_disability.values,
              edgecolor='white', linewidth=0.8)
axes[1,0].set_title('Attrition Rate by Disability Status (%)', fontweight='bold', fontsize=14)
axes[1,0].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_disability.values):
    axes[1,0].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

# LGBTQ+ attrition
axes[1,1].bar(attrition_by_lgbtq.index, attrition_by_lgbtq.values,
              edgecolor='white', linewidth=0.8)
axes[1,1].set_title('Attrition Rate by LGBTQ+ Status (%)', fontweight='bold', fontsize=14)
axes[1,1].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_lgbtq.values):
    axes[1,1].text(i, v + 0.5, f'{v:.1f}%', ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_attrition_demographic.png'), bbox_inches='tight')
plt.close()
print("Chart 2 saved: chart_attrition_demographic.png")

# --- CHART 3: Representation Trends Over Years (Hire Years) ---
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
gender_order_for_box = ['Female', 'Male', 'Non-binary', 'Transgender', 'Prefer not to say']
gender_data = [df[df['gender'] == gender]['salary'].values for gender in gender_order_for_box if gender in df['gender'].unique()]
gender_labels = [gender for gender in gender_order_for_box if gender in df['gender'].unique()]

box_plot = plt.boxplot(gender_data, labels=gender_labels, patch_artist=True)
plt.title('Salary Distribution by Gender', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Salary (Currency Units)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Color boxes
colors = ['#ff7f0e', '#1f77b4', '#2ca02c', '#d62728', '#9467bd']
for patch, color in zip(box_plot['boxes'], colors[:len(box_plot['boxes'])]):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Add mean values as points
means = [df[df['gender'] == gender]['salary'].mean() for gender in gender_labels if gender in df['gender'].unique()]
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
print(f"Employees with Disability: {disability_pct:.1f}%")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}%")

# Attrition analysis
overall_attrition = df['attrition'].mean() * 100
female_attrition = df[df['gender'] == 'Female']['attrition'].mean() * 100
male_attrition = df[df['gender'] == 'Male']['attrition'].mean() * 100 if 'Male' in df['gender'].values else 0
print(f"\nOverall Attrition Rate: {overall_attrition:.1f}%")
if female_attrition > 0 and male_attrition > 0:
    print(f"Female Attrition Rate: {female_attrition:.1f}%")
    print(f"Male Attrition Rate: {male_attrition:.1f}%")
    print(f"Attrition Ratio (Female/Male): {female_attrition/male_attrition:.2f}")
else:
    print(f"Female Attrition Rate: {female_attrition:.1f}%")

# Salary analysis
if 'Female' in df['gender'].values and 'Male' in df['gender'].values:
    male_avg_salary = df[df['gender'] == 'Male']['salary'].mean()
    female_avg_salary = df[df['gender'] == 'Female']['salary'].mean()
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
    disability_change = yearly_trends.loc[last_year, 'has_disability'] - yearly_trends.loc[first_year, 'has_disability']
    lgbtq_change = yearly_trends.loc[last_year, 'is_lgbtq'] - yearly_trends.loc[first_year, 'is_lgbtq']
    print(f"\nRepresentation Change ({first_year} to {last_year}):")
    print(f"  Female: {female_change:+.1f} percentage points")
    print(f"  Ethnic Minority: {ethnic_change:+.1f} percentage points")
    print(f"  Disability: {disability_change:+.1f} percentage points")
    print(f"  LGBTQ+: {lgbtq_change:+.1f} percentage points")

print("\nAll charts generated successfully!")