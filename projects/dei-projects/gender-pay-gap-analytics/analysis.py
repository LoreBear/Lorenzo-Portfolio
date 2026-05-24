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
df = pd.read_csv('CurrentPopulationSurvey.csv')
print(f"Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Cleaning & Preparation ---
# Filter for employed individuals with wage income
df = df[(df['empstat'].isin([10, 11, 12])) & (df['incwage'] >= 0)]  # Employed and non-negative income
print(f"After filtering employed: {df.shape[0]} records")

# Create gender identifier (sex: 1=male, 2=female)
df['is_female'] = (df['sex'] == 2).astype(int)

# Create ethnicity identifier (combining race and hispanic)
# Following CPS categorization: White, Black, Hispanic, Other
df['ethnicity_group'] = 'Other'
df.loc[df['hispan'] == 1, 'ethnicity_group'] = 'Hispanic'
df.loc[(df['hispan'] != 1) & (df['race'] == 2), 'ethnicity_group'] = 'Black'
df.loc[(df['hispan'] != 1) & (df['race'] == 1), 'ethnicity_group'] = 'White'
# Note: race codes: 1=White, 2=Black, 3=American Indian/Alaskan Native, 4=Asian/Pacific Islander

df['is_ethnic_minority'] = (~df['ethnicity_group'].isin(['White'])).astype(int)

# Note: Disability and LGBTQ status not available in CPS
df['has_disability'] = 0  # Placeholder - not in dataset
df['is_lgbtq'] = 0        # Placeholder - not in dataset

# Calculate hourly wage (incwage / hrswork) for full-time workers
# Only calculate for those who worked hours and have wage income
df['hourly_wage'] = np.where(
    (df['hrswork'] > 0) & (df['incwage'] >= 0),
    df['incwage'] / df['hrswork'],
    np.nan
)

# Education levels
df['has_bachelors'] = (df['educ99'] >= 39).astype(int)  # Bachelor's degree or higher
df['has_less_hs'] = (df['educ99'] < 31).astype(int)     # Less than high school

# --- KEY STATS ---
total_employees = len(df)
female_pct = df['is_female'].mean() * 100
ethnic_minority_pct = df['is_ethnic_minority'].mean() * 100
disability_pct = 0  # Not available in dataset
lgbtq_pct = 0       # Not available in dataset

print(f"\nTotal Employees (Employed): {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}%")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# --- CHART 1: Gender Distribution by Major Occupation Groups ---
# Simplify occupation categories for visualization
def simplify_occupation(occ_code):
    if pd.isna(occ_code):
        return 'Unknown'
    occ_code = int(occ_code)
    if occ_code in range(0, 200):      return 'Management, Business, Science'
    elif occ_code in range(200, 400):  return 'Service'
    elif occ_code in range(400, 600):  return 'Sales and Office'
    elif occ_code in range(600, 800):  return 'Natural Resources, Construction, Maintenance'
    elif occ_code in range(800, 1000): return 'Production, Transportation, Material Moving'
    else:                              return 'Other/Unknown'

df['occupation_group'] = df['occ'].apply(simplify_occupation)

# Create crosstab for gender by occupation group
occupation_order = sorted(df['occupation_group'].unique())
gender_order = ['Female', 'Male']

gender_occ = pd.crosstab(df['occupation_group'], df['is_female'], normalize='index') * 100
gender_occ = gender_occ.reindex(occupation_order)
gender_occ = gender_occ.rename(columns={0: 'Male', 1: 'Female'})[['Female', 'Male']]

plt.figure(figsize=(14, 8))
gender_occ.plot(kind='bar', stacked=True)
plt.title('Gender Distribution by Occupation Group (%)', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Occupation Group', fontsize=12)
plt.ylabel('% of Employees', fontsize=12)
plt.legend(title='Gender', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')

# Add value labels on bars (only for segments > 5%)
for i, (occ, row) in enumerate(gender_occ.iterrows()):
    cumulative = 0
    for gender in ['Female', 'Male']:
        if gender in row.index:
            value = row[gender]
            if value > 5:  # Only show label if percentage > 5%
                plt.text(i, cumulative + value/2, f'{value:.0f}%',
                        ha='center', va='center', fontweight='bold',
                        color='white' if value > 30 else 'black')
            cumulative += value

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_gender_occupation.png'), bbox_inches='tight')
plt.close()
print("Chart 1 saved: chart_gender_occupation.png")

# --- CHART 2: Wage Analysis by Demographic Group ---
# Calculate median hourly wage by group (excluding NaN)
wage_data = df.dropna(subset=['hourly_wage'])

median_wage_by_gender = wage_data.groupby('is_female')['hourly_wage'].median()
median_wage_by_ethnicity = wage_data.groupby('ethnicity_group')['hourly_wage'].median()
# Placeholder for disability and LGBTQ (not available)
median_wage_by_disability = pd.Series([0, 0], index=['No disability', 'Has disability'])
median_wage_by_lgbtq = pd.Series([0, 0], index=['Not LGBTQ+', 'LGBTQ+'])

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Gender wage
gender_labels = ['Male', 'Female']
gender_values = [median_wage_by_gender.get(0, 0), median_wage_by_gender.get(1, 0)]
axes[0,0].bar(gender_labels, gender_values, edgecolor='white', linewidth=0.8)
axes[0,0].set_title('Median Hourly Wage by Gender ($)', fontweight='bold', fontsize=14)
axes[0,0].set_ylabel('Median Hourly Wage ($)', fontsize=12)
for i, v in enumerate(gender_values):
    axes[0,0].text(i, v + max(gender_values)*0.01, f'${v:.2f}', ha='center', fontweight='bold', fontsize=10)

# Ethnicity wage (top 5 groups for readability)
ethnic_groups = median_wage_by_ethnicity.index.tolist()
ethnic_values = median_wage_by_ethnicity.values.tolist()
# Sort by wage value for better visualization
ethnic_pairs = list(zip(ethnic_groups, ethnic_values))
ethnic_pairs.sort(key=lambda x: x[1], reverse=True)
top_ethnic = ethnic_pairs[:5]  # Top 5
ethnic_labels, ethnic_values = zip(*top_ethnic) if top_ethnic else ([], [])
axes[0,1].bar(range(len(ethnic_labels)), ethnic_values, edgecolor='white', linewidth=0.8)
axes[0,1].set_title('Median Hourly Wage by Ethnicity (Top 5) ($)', fontweight='bold', fontsize=14)
axes[0,1].set_ylabel('Median Hourly Wage ($)', fontsize=12)
axes[0,1].set_xticks(range(len(ethnic_labels)))
axes[0,1].set_xticklabels(ethnic_labels, rotation=45, ha='right')
for i, v in enumerate(ethnic_values):
    axes[0,1].text(i, v + max(ethnic_values)*0.01 if len(ethnic_values) > 0 else 0, f'${v:.2f}',
                   ha='center', fontweight='bold', fontsize=10)

# Disability wage (placeholder)
axes[1,0].bar(['No disability', 'Has disability'], median_wage_by_disability.values,
              edgecolor='white', linewidth=0.8)
axes[1,0].set_title('Median Hourly Wage by Disability Status ($) (Data Not Available)', fontweight='bold', fontsize=14)
axes[1,0].set_ylabel('Median Hourly Wage ($)', fontsize=12)
for i, v in enumerate(median_wage_by_disability.values):
    axes[1,0].text(i, v + max(median_wage_by_disability.values)*0.01, f'${v:.2f}',
                   ha='center', fontweight='bold', fontsize=10)

# LGBTQ+ wage (placeholder)
axes[1,1].bar(['Not LGBTQ+', 'LGBTQ+'], median_wage_by_lgbtq.values,
              edgecolor='white', linewidth=0.8)
axes[1,1].set_title('Median Hourly Wage by LGBTQ+ Status ($) (Data Not Available)', fontweight='bold', fontsize=14)
axes[1,1].set_ylabel('Median Hourly Wage ($)', fontsize=12)
for i, v in enumerate(median_wage_by_lgbtq.values):
    axes[1,1].text(i, v + max(median_wage_by_lgbtq.values)*0.01, f'${v:.2f}',
                   ha='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_wage_demographic.png'), bbox_inches='tight')
plt.close()
print("Chart 2 saved: chart_wage_demographic.png")

# --- CHART 3: Wage Trends Over Years ---
# Calculate yearly median wage trends for underrepresented groups
yearly_trends = wage_data.groupby('year').agg({
    'is_female': lambda x: (wage_data.loc[x.index, 'is_female'] * wage_data.loc[x.index, 'hourly_wage']).sum() /
                           (wage_data.loc[x.index, 'is_female'].sum()) if wage_data.loc[x.index, 'is_female'].sum() > 0 else 0,
    'is_ethnic_minority': lambda x: (wage_data.loc[x.index, 'is_ethnic_minority'] * wage_data.loc[x.index, 'hourly_wage']).sum() /
                                    (wage_data.loc[x.index, 'is_ethnic_minority'].sum()) if wage_data.loc[x.index, 'is_ethnic_minority'].sum() > 0 else 0,
    'has_disability': lambda x: 0,  # Placeholder
    'is_lgbtq': lambda x: 0         # Placeholder
})

# Actually calculate properly - median wage by group per year
female_median_by_year = wage_data[wage_data['is_female'] == 1].groupby('year')['hourly_wage'].median()
male_median_by_year = wage_data[wage_data['is_female'] == 0].groupby('year')['hourly_wage'].median()
minority_median_by_year = wage_data[wage_data['is_ethnic_minority'] == 1].groupby('year')['hourly_wage'].median()
white_median_by_year = wage_data[wage_data['is_ethnic_minority'] == 0].groupby('year')['hourly_wage'].median()

# Create DataFrame for plotting
trends_df = pd.DataFrame({
    'Female': female_median_by_year,
    'Male': male_median_by_year,
    'Ethnic Minority': minority_median_by_year,
    'White (Non-Hispanic)': white_median_by_year
}).fillna(0)

plt.figure(figsize=(12, 6))
for column in trends_df.columns:
    plt.plot(trends_df.index, trends_df[column], marker='o', linewidth=2.5, markersize=8, label=column)
plt.title('Median Hourly Wage Trends Over Years', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Median Hourly Wage ($)', fontsize=12)
plt.legend(title='Demographic Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_wage_trends.png'), bbox_inches='tight')
plt.close()
print("Chart 3 saved: chart_wage_trends.png")

# --- CHART 4: Wage Distribution by Gender and Education ---
plt.figure(figsize=(14, 8))

# Prepare data for wage boxplot by gender and education level
education_levels = ['Less than HS', 'HS Diploma', 'Some College', 'Bachelors+']
gender_labels = ['Male', 'Female']

# Create subsets for each education level
box_data = []
box_labels = []
for i, edu_level in enumerate(['has_less_hs', 'educ99_between', 'has_some_college', 'has_bachelors']):
    if edu_level == 'has_less_hs':
        subset = wage_data[wage_data['has_less_hs'] == 1]
        edu_label = 'Less than HS'
    elif edu_level == 'has_bachelors':
        subset = wage_data[wage_data['has_bachelors'] == 1]
        edu_label = 'Bachelors+'
    else:
        # Simplified: HS diploma and some college combined for space
        subset = wage_data[(wage_data['has_less_hs'] == 0) & (wage_data['has_bachelors'] == 0)]
        if i == 1:
            edu_label = 'HS Diploma'
        else:
            edu_label = 'Some College'

    for j, gender in enumerate([0, 1]):  # 0=Male, 1=Female
        gender_str = 'Male' if j == 0 else 'Female'
        gender_subset = subset[subset['is_female'] == j]
        if len(gender_subset) > 0:
            box_data.append(gender_subset['hourly_wage'].values)
            box_labels.append(f'{edu_label}\n{gender_str}')

# Create box plot
box_plot = plt.boxplot(box_data, labels=box_labels, patch_artist=True, showfliers=False)
plt.title('Wage Distribution by Education and Gender', fontsize=16, pad=20, fontweight='bold')
plt.xlabel('Education Level and Gender', fontsize=12)
plt.ylabel('Hourly Wage ($)', fontsize=12)

# Color boxes by gender
colors = ['#1f77b4', '#ff7f0e']  # Blue for Male, Orange for Female
for i, patch in enumerate(box_plot['boxes']):
    gender_idx = i % 2  # Alternate between male/female
    patch.set_facecolor(colors[gender_idx])
    patch.set_alpha(0.7)

# Add mean values as points
means = []
positions = []
for i, data in enumerate(box_data):
    if len(data) > 0:
        means.append(np.mean(data))
        positions.append(i+1)

plt.scatter(positions, means, color='black', marker='D', s=60, zorder=3)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_wage_education_gender.png'), bbox_inches='tight')
plt.close()
print("Chart 4 saved: chart_wage_education_gender.png")

# --- SUMMARY STATS ---
print("\n=== SUMMARY FOR README ===")
print(f"Total Employees (Employed): {total_employees}")
print(f"Female Representation: {female_pct:.1f}%")
print(f"Ethnic Minority Representation: {ethnic_minority_pct:.1f}%")
print(f"Employees with Disability: {disability_pct:.1f}% (data not available)")
print(f"LGBTQ+ Representation: {lgbtq_pct:.1f}% (data not available)")

# Wage analysis
if not wage_data.empty:
    male_median_wage = wage_data[wage_data['is_female'] == 0]['hourly_wage'].median()
    female_median_wage = wage_data[wage_data['is_female'] == 1]['hourly_wage'].median()
    if not pd.isna(male_median_wage) and not pd.isna(female_median_wage):
        wage_gap = male_median_wage - female_median_wage
        wage_gap_pct = (wage_gap / male_median_wage) * 100 if male_median_wage > 0 else 0
        print(f"\nMedian Male Hourly Wage: ${male_median_wage:.2f}")
        print(f"Median Female Hourly Wage: ${female_median_wage:.2f}")
        print(f"Gender Wage Gap: ${wage_gap:.2f} per hour")
        print(f"Gender Wage Gap Percentage: {wage_gap_pct:.1f}%")
    else:
        print("\nWage data not available for gender comparison")
else:
    print("\nNo wage data available after filtering")

# Education and wage correlation
if not wage_data.empty and 'has_bachelors' in wage_data.columns:
    ba_wage = wage_data[wage_data['has_bachelors'] == 1]['hourly_wage'].median()
    no_ba_wage = wage_data[wage_data['has_bachelors'] == 0]['hourly_wage'].median()
    if not pd.isna(ba_wage) and not pd.isna(no_ba_wage):
        ba_premium = ba_wage - no_ba_wage
        ba_premium_pct = (ba_premium / no_ba_wage) * 100 if no_ba_wage > 0 else 0
        print(f"\nBachelor's Degree Wage Premium: ${ba_premium:.2f} per hour ({ba_premium_pct:.1f}%)")

# Trends over years
if len(yearly_trends) >= 2:
    years = sorted(wage_data['year'].unique())
    if len(years) >= 2:
        first_year = years[0]
        last_year = years[-1]
        # Calculate change in female-to-male wage ratio
        first_year_data = wage_data[wage_data['year'] == first_year]
        last_year_data = wage_data[wage_data['year'] == last_year]

        if not first_year_data.empty and not last_year_data.empty:
            first_female_wage = first_year_data[first_year_data['is_female'] == 1]['hourly_wage'].median()
            first_male_wage = first_year_data[first_year_data['is_female'] == 0]['hourly_wage'].median()
            last_female_wage = last_year_data[last_year_data['is_female'] == 1]['hourly_wage'].median()
            last_male_wage = last_year_data[last_year_data['is_female'] == 0]['hourly_wage'].median()

            if not pd.isna(first_female_wage) and not pd.isna(first_male_wage) and first_male_wage > 0:
                first_ratio = first_female_wage / first_male_wage
            else:
                first_ratio = 0

            if not pd.isna(last_female_wage) and not pd.isna(last_male_wage) and last_male_wage > 0:
                last_ratio = last_female_wage / last_male_wage
            else:
                last_ratio = 0

            ratio_change = (last_ratio - first_ratio) * 100  # Change in percentage points
            print(f"\nFemale-to-Male Wage Ratio Change ({first_year} to {last_year}): {ratio_change:+.1f} percentage points")
            print(f"  (Ratio: {first_year}: {first_ratio:.2f} -> {last_year}: {last_ratio:.2f})")

print("\nAll charts generated successfully!")