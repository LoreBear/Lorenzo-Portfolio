"""
Inclusive Leadership Workshop Analytics - Real Data Version
Analyzes real HR employee data to assess leadership competencies and workshop effectiveness
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import os

# --- Setup ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts_real')
os.makedirs(output_folder, exist_ok=True)

plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# --- Load Real HR Data ---
df = pd.read_csv('HR_Dataset.csv')
print(f"Real HR dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Preparation ---
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
df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})
df['Stock_Option_Level'] = pd.to_numeric(df['Stock_Option_Level'])

# Create leadership competency proxies from available data
# Based on organizational psychology, we can infer leadership competencies from:
# 1. Job Satisfaction -> Self-Awareness & Engagement
# 2. Performance Rating -> Decision-Making & Results Orientation
# 3. Work Life Balance -> Psychological Safety & Empathy
# 4. Training Hours -> Development & Growth Mindset
# 5. Years in Current Role -> Experience & Stability
# 6. Attrition (reverse) -> Retention & Psychological Safety

print("\n=== Creating Leadership Competency Proxies ===")

# Normalize scores to 1-5 scale for consistency with original workshop framework
def normalize_to_1_5(series, reverse=False):
    """Normalize a series to 1-5 scale"""
    if series.max() == series.min():
        return pd.Series([3.0] * len(series), index=series.index)
    normalized = 1 + 4 * (series - series.min()) / (series.max() - series.min())
    if reverse:
        normalized = 6 - normalized  # Reverse scale
    return normalized

# Create leadership dimension scores based on available HR metrics
df['Self_Awareness_Engagement'] = normalize_to_1_5(df['Job_Satisfaction'])
df['Decision_Making_Results'] = normalize_to_1_5(df['Performance_Rating'])
df['Psychological_Safety'] = normalize_to_1_5(df['Work_Life_Balance'])
df['Development_Growth'] = normalize_to_1_5(df['Training_Hours_Last_Year'])
# For Experience: moderate years in role is optimal (not too little, not too much)
# We'll create an inverted U-shape where 5-10 years is optimal
years_optimal = np.abs(df['Years_In_Current_Role'] - 7.5)  # Distance from 7.5 years
df['Experience_Stability'] = normalize_to_1_5(years_optimal, reverse=True)
# Retention proxy (inverse of attrition)
df['Retention_Safety'] = normalize_to_1_5(1 - df['Attrition'])

leadership_dimensions = [
    'Self_Awareness_Engagement',
    'Decision_Making_Results',
    'Psychological_Safety',
    'Development_Growth',
    'Experience_Stability',
    'Retention_Safety'
]

dimension_labels = {
    'Self_Awareness_Engagement': 'Self-Awareness & Engagement',
    'Decision_Making_Results': 'Decision-Making & Results Orientation',
    'Psychological_Safety': 'Psychological Safety & Well-being',
    'Development_Growth': 'Development & Growth Mindset',
    'Experience_Stability': 'Experience & Role Stability',
    'Retention_Safety': 'Retention & Psychological Safety'
}

print("Leadership competency proxies created from HR data:")
for dim in leadership_dimensions:
    print(f"  {dimension_labels[dim]}: Mean = {df[dim].mean():.2f}")

# --- Demographic Analysis ---
print("\n=== Demographic Analysis ===")
print(f"Gender Distribution:")
gender_counts = df['Gender'].value_counts()
for gender, count in gender_counts.items():
    print(f"  {gender}: {count} ({count/len(df)*100:.1f}%)")

print(f"\nDepartment Distribution (Top 5):")
dept_counts = df['Department'].value_counts().head()
for dept, count in dept_counts.items():
    print(f"  {dept}: {count} ({count/len(df)*100:.1f}%)")

print(f"\nEducation Level Distribution:")
edu_counts = df['Education_Level'].value_counts()
for edu, count in edu_counts.head().items():
    print(f"  {edu}: {count} ({count/len(df)*100:.1f}%)")

# --- Leadership Analysis by Demographics ---
print("\n=== Leadership Competency Analysis by Demographics ===")

# Gender differences
gender_analysis = df.groupby('Gender')[leadership_dimensions].mean()
print("\nLeadership Competency Scores by Gender:")
for gender in gender_analysis.index:
    print(f"  {gender}:")
    for dim in leadership_dimensions:
        print(f"    {dimension_labels[dim]}: {gender_analysis.loc[gender, dim]:.2f}")

# Department differences (top 4 departments)
top_depts = df['Department'].value_counts().head(4).index
dept_analysis = df[df['Department'].isin(top_depts)].groupby('Department')[leadership_dimensions].mean()
print(f"\nLeadership Competency Scores by Department (Top 4):")
for dept in dept_analysis.index:
    print(f"  {dept}:")
    for dim in leadership_dimensions:
        print(f"    {dimension_labels[dim]}: {dept_analysis.loc[dept, dim]:.2f}")

# --- Correlation Analysis ---
print("\n=== Correlation Analysis ===")
# Correlate leadership competencies with key HR outcomes
outcome_vars = ['Job_Satisfaction', 'Performance_Rating', 'Work_Life_Balance',
                'Training_Hours_Last_Year', 'Years_At_Company', 'Attrition']
outcome_labels = {
    'Job_Satisfaction': 'Job Satisfaction',
    'Performance_Rating': 'Performance Rating',
    'Work_Life_Balance': 'Work-Life Balance',
    'Training_Hours_Last_Year': 'Training Hours',
    'Years_At_Company': 'Years at Company',
    'Attrition': 'Attrition Risk (reverse)'
}

# Calculate correlations
correlations = {}
for outcome in outcome_vars:
    if outcome == 'Attrition':
        # For attrition, we expect negative correlation with positive leadership traits
        corr_data = df[leadership_dimensions].corrwith(df[outcome]) * -1  # Reverse for positive interpretation
    else:
        corr_data = df[leadership_dimensions].corrwith(df[outcome])
    correlations[outcome] = corr_data

print("Correlations between Leadership Competencies and HR Outcomes:")
for outcome in outcome_vars:
    print(f"\n  {outcome_labels[outcome]}:")
    for dim in leadership_dimensions:
        corr = correlations[outcome][dim]
        print(f"    {dimension_labels[dim]}: {corr:.3f}")

# --- Key Insights Summary ---
print("\n=== KEY INSIGHTS FOR WORKSHOP EFFECTIVENESS ===")

# 1. Overall Leadership Competency Levels
overall_leadership = df[leadership_dimensions].mean().mean()
print(f"\n1. Overall Leadership Competency Level: {overall_leadership:.2f}/5.0")

# 2. Strengths and Areas for Development
dim_means = df[leadership_dimensions].mean()
sorted_dims = dim_means.sort_values(ascending=False)
print(f"\n2. Leadership Competency Ranking:")
for i, (dim, score) in enumerate(sorted_dims.items(), 1):
    print(f"   {i}. {dimension_labels[dim]}: {score:.2f}/5.0")

# 3. Demographic Disparities
print(f"\n3. Gender Disparities in Leadership Competencies:")
gender_diff = gender_analysis.loc['Female'] - gender_analysis.loc['Male'] if 'Female' in gender_analysis.index and 'Male' in gender_analysis.index else None
if gender_diff is not None:
    for dim in leadership_dimensions:
        diff = gender_diff[dim]
        direction = "higher" if diff > 0 else "lower"
        print(f"   {dimension_labels[dim]}: Females score {abs(diff):.2f} points {direction} than Males")

# 4. Predictive Power for Retention
retention_corr = correlations['Attrition']
strongest_predictor = retention_corr.idxmax()
strongest_corr = retention_corr.max()
print(f"\n4. Strongest Predictor of Retention:")
print(f"   {dimension_labels[strongest_predictor]}: {strongest_corr:.3f} correlation with retention")

# 5. Development Opportunities
lowest_competency = sorted_dims.index[0]  # Lowest score
highest_competency = sorted_dims.index[-1]  # Highest score
print(f"\n5. Targeted Development Opportunities:")
print(f"   Lowest: {dimension_labels[lowest_competency]} ({df[lowest_competency].mean():.2f}/5.0)")
print(f"   Highest: {dimension_labels[highest_competency]} ({df[highest_competency].mean():.2f}/5.0)")
print(f"   Development Gap: {df[highest_competency].mean() - df[lowest_competency].mean():.2f} points")

# --- Generate Visualizations ---
print("\n=== Generating Visualizations ===")

# Chart 1: Leadership Competency Overview (Radar Chart)
plt.figure(figsize=(10, 8))
# Number of variables
categories = [dimension_labels[dim] for dim in leadership_dimensions]
N = len(categories)

# What will be the angle of each axis in the plot
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Initialize the spider plot
ax = plt.subplot(111, projection='polar')

# Plot data
values = df[leadership_dimensions].mean().values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, 'o-', linewidth=2, label='Current Workforce', color='#1f77b4')
ax.fill(angles, values, alpha=0.25, color='#1f77b4')

# Add target/excellent level (4.0) for comparison
target_values = [4.0] * N
target_values += target_values[:1]
ax.plot(angles, target_values, 'o--', linewidth=2, label='Target Level (4.0)', color='#ff7f0e', alpha=0.8)

ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_ylim(0, 5)
ax.set_title('Leadership Competency Profile: Current vs Target', fontweight='bold', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_leadership_profile.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Chart 1 saved: chart_leadership_profile.png")

# Chart 2: Leadership Competencies by Gender
plt.figure(figsize=(12, 6))
gender_means = df.groupby('Gender')[leadership_dimensions].mean()
x = np.arange(len(leadership_dimensions))
width = 0.35

for i, gender in enumerate(gender_means.index):
    offset = width * (i - 0.5) if len(gender_means.index) == 2 else width * (i - 1)
    plt.bar(x + offset, gender_means.loc[gender], width, label=gender, alpha=0.8)

plt.xlabel('Leadership Competencies', fontsize=12, fontweight='bold')
plt.ylabel('Average Score (1-5 Scale)', fontsize=12, fontweight='bold')
plt.title('Leadership Competency Scores by Gender', fontsize=16, fontweight='bold', pad=20)
plt.xticks(x, [dimension_labels[dim] for dim in leadership_dimensions], rotation=15, ha='right')
plt.legend()
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_leadership_by_gender.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Chart 2 saved: chart_leadership_by_gender.png")

# Chart 3: Correlation Heatmap
plt.figure(figsize=(10, 8))
# Prepare correlation matrix for heatmap
corr_data = []
for outcome in outcome_vars:
    if outcome != 'Attrition':  # Skip attrition for cleaner visualization (or use reversed)
        corr_data.append(correlations[outcome].values)

corr_matrix = np.array(corr_data)
outcome_labels_clean = [outcome_labels[outcome] for outcome in outcome_vars if outcome != 'Attrition']
dimension_label_list = [dimension_labels[dim] for dim in leadership_dimensions]

sns.heatmap(corr_matrix,
            annot=True,
            fmt='.2f',
            cmap='RdBu_r',
            center=0,
            square=True,
            linewidths=0.5,
            cbar_kws={"shrink": .8},
            xticklabels=dimension_label_list,
            yticklabels=outcome_labels_clean)
plt.title('Correlations: Leadership Competencies vs HR Outcomes', fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_correlations_heatmap.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Chart 3 saved: chart_correlations_heatmap.png")

# Chart 4: Department Comparison (Top 4)
plt.figure(figsize=(14, 8))
dept_means = df[df['Department'].isin(top_depts)].groupby('Department')[leadership_dimensions].mean()
x = np.arange(len(leadership_dimensions))
width = 0.2

for i, dept in enumerate(dept_means.index):
    offset = width * (i - 1.5)
    plt.bar(x + offset, dept_means.loc[dept], width, label=dept, alpha=0.8)

plt.xlabel('Leadership Competencies', fontsize=12, fontweight='bold')
plt.ylabel('Average Score (1-5 Scale)', fontsize=12, fontweight='bold')
plt.title('Leadership Competency Scores by Department (Top 4)', fontsize=16, fontweight='bold', pad=20)
plt.xticks(x, [dimension_labels[dim] for dim in leadership_dimensions], rotation=15, ha='right')
plt.legend()
plt.ylim(0, 5)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_leadership_by_dept.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Chart 4 saved: chart_leadership_by_dept.png")

# --- Summary Statistics for Reporting ---
print("\n=== SUMMARY FOR REPORTING ===")
print(f"Total Employees Analyzed: {len(df)}")
print(f"Overall Leadership Competency: {overall_leadership:.2f}/5.0")
print(f"Gender Balance: {gender_counts.get('Female', 0)/len(df)*100:.1f}% Female, {gender_counts.get('Male', 0)/len(df)*100:.1f}% Male")
print(f"Top Leadership Strength: {dimension_labels[highest_competency]} ({df[highest_competency].mean():.2f}/5.0)")
print(f"Key Development Area: {dimension_labels[lowest_competency]} ({df[lowest_competency].mean():.2f}/5.0)")
print(f"Strongest Retention Predictor: {dimension_labels[strongest_predictor]} ({strongest_corr:.3f} correlation)")

print(f"\nAll charts generated successfully in '{output_folder}' folder!")

# Create a simple summary report
summary_report = f"""
INCLUSIVE LEADERSHIP WORKSHOP ANALYSIS - REAL DATA
==================================================

Dataset: HR Employee Data (Kaggle justinlimyin/hr-employee-dataset)
Sample Size: {len(df)} employees
Analysis Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}

KEY FINDINGS:
-------------
1. Overall Leadership Competency Level: {overall_leadership:.2f}/5.0
2. Gender Balance: {gender_counts.get('Female', 0)/len(df)*100:.1f}% Female, {gender_counts.get('Male', 0)/len(df)*100:.1f}% Male
3. Top Leadership Strength: {dimension_labels[highest_competency]} ({df[highest_competency].mean():.2f}/5.0)
4. Key Development Area: {dimension_labels[lowest_competency]} ({df[lowest_competency].mean():.2f}/5.0)
5. Strongest Retention Predictor: {dimension_labels[strongest_predictor]} ({strongest_corr:.3f} correlation with retention)

LEADERSHIP COMPETENCY RANKING:
------------------------------
"""
for i, (dim, score) in enumerate(sorted_dims.items(), 1):
    summary_report += f"{i}. {dimension_labels[dim]}: {score:.2f}/5.0\n"

summary_report += f"""
GENDER DIFFERENCES:
-------------------
"""
if gender_diff is not None:
    for dim in leadership_dimensions:
        diff = gender_diff[dim]
        direction = "higher" if diff > 0 else "lower"
        summary_report += f"{dimension_labels[dim]}: Females score {abs(diff):.2f} points {direction} than Males\n"

summary_report += f"""
DEVELOPMENT PRIORITIES:
----------------------
1. Focus on improving: {dimension_labels[lowest_competency]}
2. Leverage strength in: {dimension_labels[highest_competency]}
3. Address gender gaps in: {[dimension_labels[dim] for dim in leadership_dimensions if abs(gender_diff[dim]) > 0.2]}
4. Enhance retention through: {dimension_labels[strongest_predictor]} development

RECOMMENDATIONS FOR WORKSHOP DESIGN:
------------------------------------
1. Tailor content to address identified competency gaps
2. Create gender-inclusive examples and case studies
3. Develop department-specific breakout sessions
4. Focus on practical skill-building in lowest scoring areas
5. Measure impact through pre/post comparison of these exact metrics
"""

with open(os.path.join(current_dir, 'workshop_real_data_summary.txt'), 'w') as f:
    f.write(summary_report)

print(f"\nSummary report saved: workshop_real_data_summary.txt")