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

# --- Load Dataset ---
df = pd.read_csv('HR_Dataset.csv')
print(f"Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Cleaning & Preparation ---
# Ensure proper data types
df['Age'] = pd.to_numeric(df['Age'])
df['Monthly_Income'] = pd.to_numeric(df['Monthly_Income'])
df['Years_At_Company'] = pd.to_numeric(df['Years_At_Company'])
df['Years_In_Current_Role'] = pd.to_numeric(df['Years_In_Current_Role'])
df['Job_Satisfaction'] = pd.to_numeric(df['Job_Satisfaction'])
df['Performance_Rating'] = pd.to_numeric(df['Performance_Rating'])
df['Work_Life_Balance'] = pd.to_numeric(df['Work_Life_Balance'])
df['Training_Hours_Last_Year'] = pd.to_numeric(df['Training_Hours_Last_Year'])
df['Last_Promotion_Years_Ago'] = pd.to_numeric(df['Last_Promotion_Years_Ago'])
df['Distance_From_Home'] = pd.to_numeric(df['Distance_From_Home'])
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})  # Convert to boolean
df['Stock_Option_Level'] = pd.to_numeric(df['Stock_Option_Level'])

# Create gender identifier
df['is_female'] = (df['Gender'] == 'Female').astype(int)
df['is_male'] = (df['Gender'] == 'Male').astype(int)
df['is_non_binary'] = (df['Gender'] == 'Non-binary').astype(int)

# Create ethnicity identifier (not available in this dataset)
# Using proxy: could infer from other fields but not reliable
df['is_ethnic_minority'] = 0  # Placeholder - not in dataset

# Create disability identifier (not available in this dataset)
df['has_disability'] = 0  # Placeholder - not in dataset

# Create LGBTQ identifier (not available in this dataset)
df['is_lgbtq'] = 0  # Placeholder - not in dataset

# Calculate years since last promotion (handle 0 values - means never promoted or promoted this year)
df['Years_Since_Promotion'] = df['Last_Promotion_Years_Ago'].copy()
df.loc[df['Years_Since_Promotion'] == 0, 'Years_Since_Promotion'] = df.loc[df['Last_Promotion_Years_Ago'] == 0, 'Years_At_Company'].values  # If 0, use years at company

# --- KEY STATS ---
total_employees = len(df)
female_pct = df['is_female'].mean() * 100
male_pct = df['is_male'].mean() * 100
non_binary_pct = df['is_non_binary'].mean() * 100
ethnic_minority_pct = 0  # Not available
disability_pct = 0       # Not available
lgbtq_pct = 0            # Not available

print(f"\nTotal Employees: {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Male Representation: {male_pct:.1f}%")
print(f"Non-binary Representation: {non_binary_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}% (data not available)")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# --- CHART 1: Gender Distribution by Department ---
dept_order = sorted(df['Department'].unique())
gender_cats = ['Female', 'Male', 'Non-binary']

# Create crosstab for gender by department
gender_dept = pd.crosstab(df['Department'], df['Gender'], normalize='index') * 100
# Ensure all gender categories are present
for cat in gender_cats:
    if cat not in gender_dept.columns:
        gender_dept[cat] = 0
gender_dept = gender_dept[gender_cats]  # Reorder columns
gender_dept = gender_dept.reindex(dept_order)  # Ensure order

plt.figure(figsize=(14, 8))
gender_dept.plot(kind='bar', stacked=True)
plt.title('Gender Distribution by Department (%)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('% of Employees', fontsize=12)
plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars (only for segments > 5%)
for i, (dept, row) in enumerate(gender_dept.iterrows()):
    cumulative = 0
    for gender in gender_cats:
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
attrition_by_gender = df.groupby('Gender')['Attrition'].mean() * 100
# For ethnicity, disability, LGBTQ - placeholders since not in dataset
attrition_by_ethnicity = pd.Series([0], index=['Unknown']) * 100  # Placeholder
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

# Ethnicity attrition (placeholder)
axes[0,1].bar(['Data Not Available'], attrition_by_ethnicity.values,
              edgecolor='white', linewidth=0.8)
axes[0,1].set_title('Attrition Rate by Ethnicity (%) (Data Not Available)', fontweight='bold', fontsize=14)
axes[0,1].set_ylabel('Attrition Rate (%)', fontsize=12)
for i, v in enumerate(attrition_by_ethnicity.values):
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

# --- CHART 3: Representation Trends Over Years (Years at Company as proxy) ---
# Calculate yearly hiring trends using Years_At_Company as proxy for hire cohort
# We'll create hire year estimate: current year - years_at_company
# For simplicity, we'll use Years_At_Company cohorts directly
df['hire_year_estimate'] = 2024 - df['Years_At_Company']  # Assuming 2024 as current year
df['hire_year_estimate'] = df['hire_year_estimate'].clip(lower=2000)  # reasonable minimum

# Calculate yearly hiring trends for underrepresented groups
yearly_trends = df.groupby('hire_year_estimate').agg({
    'is_female': 'mean',
    'is_male': 'mean',
    'is_non_binary': 'mean',
    'is_ethnic_minority': 'mean',
    'has_disability': 'mean',
    'is_lgbtq': 'mean',
}) * 100

yearly_trends = yearly_trends.round(2)

plt.figure(figsize=(12, 6))
yearly_trends[['is_female', 'is_male', 'is_non_binary']].plot(kind='line', marker='o', linewidth=2.5, markersize=8)
plt.title('Gender Representation Trends Over Hire Years (Estimated)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Hire Year Estimate', fontsize=12)
plt.ylabel('Representation (%)', fontsize=12)
plt.legend(title='Gender', labels=['Female', 'Male', 'Non-binary'],
           bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_representation_trends.png'), bbox_inches='tight')
plt.close()
print("Chart 3 saved: chart_representation_trends.png")

# --- CHART 4: Income Analysis by Gender and Job Role ---
plt.figure(figsize=(14, 8))

# Prepare data for income boxplot by gender
gender_order_for_box = ['Female', 'Male', 'Non-binary']
gender_data = [df[df['Gender'] == gender]['Monthly_Income'].values for gender in gender_order_for_box if gender in df['Gender'].unique()]
gender_labels = [gender for gender in gender_order_for_box if gender in df['Gender'].unique()]

box_plot = plt.boxplot(gender_data, labels=gender_labels, patch_artist=True)
plt.title('Monthly Income Distribution by Gender', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Monthly Income (Currency Units)', fontsize=12)
plt.xticks(rotation=45, ha='right')

# Color boxes
colors = ['#ff7f0e', '#1f77b4', '#2ca02c']
for patch, color in zip(box_plot['boxes'], colors[:len(box_plot['boxes'])]):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

# Add mean values as points
means = [df[df['Gender'] == gender]['Monthly_Income'].mean() for gender in gender_labels if gender in df['Gender'].unique()]
for i, mean in enumerate(means):
    plt.plot(i+1, mean, 'D', color='black', markersize=8)

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_income_gender.png'), bbox_inches='tight')
plt.close()
print("Chart 4 saved: chart_income_gender.png")

# --- SUMMARY STATS ---
print("\n=== SUMMARY FOR README ===")
print(f"Total Employees: {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Male Representation: {male_pct:.1f}%")
print(f"Non-binary Representation: {non_binary_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}% (data not available)")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# Attrition analysis
overall_attrition = df['Attrition'].mean() * 100
female_attrition = df[df['Gender'] == 'Female']['Attrition'].mean() * 100 if 'Female' in df['Gender'].values else 0
male_attrition = df[df['Gender'] == 'Male']['Attrition'].mean() * 100 if 'Male' in df['Gender'].values else 0
non_binary_attrition = df[df['Gender'] == 'Non-binary']['Attrition'].mean() * 100 if 'Non-binary' in df['Gender'].values else 0
print(f"\nOverall Attrition Rate: {overall_attrition:.1f}%")
print(f"Female Attrition Rate: {female_attrition:.1f}%")
print(f"Male Attrition Rate: {male_attrition:.1f}%")
print(f"Non-binary Attrition Rate: {non_binary_attrition:.1f}%")
if female_attrition > 0 and male_attrition > 0:
    print(f"Attrition Ratio (Female/Male): {female_attrition/male_attrition:.2f}")

# Income analysis
if 'Female' in df['Gender'].values and 'Male' in df['Gender'].values:
    male_avg_income = df[df['Gender'] == 'Male']['Monthly_Income'].mean()
    female_avg_income = df[df['Gender'] == 'Female']['Monthly_Income'].mean()
    income_gap = male_avg_income - female_avg_income
    income_gap_pct = (income_gap / male_avg_income) * 100 if male_avg_income > 0 else 0
    print(f"\nAverage Male Monthly Income: {male_avg_income:.0f}")
    print(f"Average Female Monthly Income: {female_avg_income:.0f}")
    print(f"Gender Income Gap: {income_gap:.0f} currency units")
    print(f"Gender Income Gap Percentage: {income_gap_pct:.1f}%")
else:
    print("\nGender income comparison not available (missing Female or Male data)")

# Job satisfaction analysis
avg_job_satisfaction = df['Job_Satisfaction'].mean()
avg_work_life_balance = df['Work_Life_Balance'].mean()
avg_performance_rating = df['Performance_Rating'].mean()
print(f"\nAverage Job Satisfaction: {avg_job_satisfaction:.2f}/4")
print(f"Average Work-Life Balance: {avg_work_life_balance:.2f}/4")
print(f"Average Performance Rating: {avg_performance_rating:.2f}/5")

# Years at company analysis
avg_years_company = df['Years_At_Company'].mean()
avg_years_role = df['Years_In_Current_Role'].mean()
print(f"\nAverage Years at Company: {avg_years_company:.1f}")
print(f"Average Years in Current Role: {avg_years_role:.1f}")

# Training and promotion analysis
avg_training_hours = df['Training_Hours_Last_Year'].mean()
avg_years_since_promotion = df['Years_Since_Promotion'].mean()
print(f"\nAverage Training Hours Last Year: {avg_training_hours:.1f}")
print(f"Average Years Since Last Promotion: {avg_years_since_promotion:.1f}")

print("\nAll charts generated successfully!")