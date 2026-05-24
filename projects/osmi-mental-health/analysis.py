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
current_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(current_dir, 'survey.csv'))
print(f"Dataset loaded: {df.shape[0]} records, {df.shape[1]} columns")

# --- Data Cleaning ---
# Normalize Gender
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender_Clean'] = df['Gender'].apply(lambda x:
    'Male' if x in ['male', 'm', 'man', 'cis male', 'cis man', 'male (cis)', 'mail', 'malr', 'msle', 'make'] else
    'Female' if x in ['female', 'f', 'woman', 'cis female', 'cis woman', 'female (cis)', 'femake', 'femail'] else
    'Non-binary / Other')

# Remove outlier ages
df = df[(df['Age'] >= 18) & (df['Age'] <= 70)]
print(f"After age cleaning: {df.shape[0]} records")

# Work interference score (numeric)
interfere_map = {'Never': 0, 'Rarely': 1, 'Sometimes': 2, 'Often': 3}
df['interfere_num'] = df['work_interfere'].map(interfere_map)

# Treatment binary
df['treatment_bin'] = (df['treatment'] == 'Yes').astype(int)

# Remote binary
df['remote_bin'] = (df['remote_work'] == 'Yes').astype(int)

# --- KEY STATS ---
total = len(df)
remote_pct = df['remote_work'].value_counts(normalize=True)['Yes'] * 100
treatment_pct = df['treatment_bin'].mean() * 100
no_benefits_pct = (df['benefits'] == 'No').mean() * 100

print(f"\nTotal respondents: {total}")
print(f"Remote workers: {remote_pct:.1f}%")
print(f"Sought treatment: {treatment_pct:.1f}%")
print(f"No mental health benefits: {no_benefits_pct:.1f}%")

# --- CHART 1: Work Interference by Remote Status ---
interference_order = ['Never', 'Rarely', 'Sometimes', 'Often']
remote_labels = {True: 'Remote', False: 'Non-Remote'}
df['Remote Label'] = df['remote_work'].map({'Yes': 'Remote', 'No': 'Non-Remote'})

ct = df[df['work_interfere'].notna()].groupby(['Remote Label', 'work_interfere']).size().reset_index(name='count')
ct_pct = ct.copy()
for label in ['Remote', 'Non-Remote']:
    total_label = ct_pct[ct_pct['Remote Label'] == label]['count'].sum()
    ct_pct.loc[ct_pct['Remote Label'] == label, 'pct'] = ct_pct.loc[ct_pct['Remote Label'] == label, 'count'] / total_label * 100

ct_pct['work_interfere'] = pd.Categorical(ct_pct['work_interfere'], categories=interference_order, ordered=True)
ct_pct = ct_pct.sort_values('work_interfere')

plt.figure(figsize=(10, 6))
ax = sns.barplot(data=ct_pct, x='work_interfere', y='pct', hue='Remote Label',
                 palette=['#2166ac', '#d6604d'], order=interference_order)
plt.title('Mental Health Work Interference: Remote vs Non-Remote Workers', fontsize=14, pad=15)
plt.xlabel('Frequency of Work Interference', fontsize=11)
plt.ylabel('% of Respondents', fontsize=11)
plt.legend(title='Work Location')
for container in ax.containers:
    ax.bar_label(container, fmt='%.1f%%', fontsize=8, padding=2)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_interference_remote.png'))
plt.close()
print("Chart 1 saved: chart_interference_remote.png")

# Print key stats for README
remote_often = ct_pct[(ct_pct['Remote Label']=='Remote') & (ct_pct['work_interfere']=='Often')]['pct'].values[0]
nonremote_often = ct_pct[(ct_pct['Remote Label']=='Non-Remote') & (ct_pct['work_interfere']=='Often')]['pct'].values[0]
print(f"  Remote 'Often' interference: {remote_often:.1f}%")
print(f"  Non-Remote 'Often' interference: {nonremote_often:.1f}%")

# --- CHART 2: Mental Health Benefits vs Work Interference ---
df_benefits = df[df['benefits'].isin(['Yes', 'No']) & df['work_interfere'].notna()]
ct2 = df_benefits.groupby(['benefits', 'work_interfere']).size().reset_index(name='count')
for b in ['Yes', 'No']:
    total_b = ct2[ct2['benefits'] == b]['count'].sum()
    ct2.loc[ct2['benefits'] == b, 'pct'] = ct2.loc[ct2['benefits'] == b, 'count'] / total_b * 100
ct2['work_interfere'] = pd.Categorical(ct2['work_interfere'], categories=interference_order, ordered=True)
ct2 = ct2.sort_values('work_interfere')

plt.figure(figsize=(10, 6))
ax2 = sns.barplot(data=ct2, x='work_interfere', y='pct', hue='benefits',
                  palette=['#4dac26', '#ca0020'], order=interference_order,
                  hue_order=['Yes', 'No'])
plt.title('Work Interference by Mental Health Benefits Provision', fontsize=14, pad=15)
plt.xlabel('Frequency of Work Interference', fontsize=11)
plt.ylabel('% of Respondents', fontsize=11)
plt.legend(title='MH Benefits Provided')
for container in ax2.containers:
    ax2.bar_label(container, fmt='%.1f%%', fontsize=8, padding=2)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_benefits_interference.png'))
plt.close()
print("Chart 2 saved: chart_benefits_interference.png")

benefits_often_yes = ct2[(ct2['benefits']=='Yes') & (ct2['work_interfere']=='Often')]['pct'].values[0]
benefits_often_no = ct2[(ct2['benefits']=='No') & (ct2['work_interfere']=='Often')]['pct'].values[0]
print(f"  'Often' interference WITH benefits: {benefits_often_yes:.1f}%")
print(f"  'Often' interference WITHOUT benefits: {benefits_often_no:.1f}%")

# --- CHART 3: Mental Health Leave Difficulty ---
leave_order = ['Very easy', 'Somewhat easy', "Don't know", 'Somewhat difficult', 'Very difficult']
leave_counts = df['leave'].value_counts()
leave_pct = (leave_counts / leave_counts.sum() * 100).reindex(leave_order).dropna()

colors = ['#2ca02c', '#98df8a', '#aec7e8', '#ffbb78', '#d62728']
plt.figure(figsize=(10, 6))
bars = plt.bar(leave_pct.index, leave_pct.values, color=colors, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, leave_pct.values):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=9)
plt.title('Ease of Taking Mental Health Leave in Tech Organizations', fontsize=14, pad=15)
plt.xlabel('Perceived Difficulty', fontsize=11)
plt.ylabel('% of Respondents', fontsize=11)
plt.xticks(rotation=20, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_leave_difficulty.png'))
plt.close()
print("Chart 3 saved: chart_leave_difficulty.png")
dontknow_pct = leave_pct["Don't know"]
print(f"  'Don't know' leave difficulty: {dontknow_pct:.1f}%")

# --- CHART 4: Supervisor Trust by Company Size ---
size_order = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
df_sup = df[df['supervisor'].isin(['Yes', 'No', 'Some of them']) & df['no_employees'].isin(size_order)]
ct4 = df_sup.groupby(['no_employees', 'supervisor']).size().reset_index(name='count')
for s in size_order:
    total_s = ct4[ct4['no_employees'] == s]['count'].sum()
    if total_s > 0:
        ct4.loc[ct4['no_employees'] == s, 'pct'] = ct4.loc[ct4['no_employees'] == s, 'count'] / total_s * 100
ct4['no_employees'] = pd.Categorical(ct4['no_employees'], categories=size_order, ordered=True)
ct4 = ct4.sort_values('no_employees')

plt.figure(figsize=(12, 6))
sns.barplot(data=ct4, x='no_employees', y='pct', hue='supervisor',
            palette=['#2166ac', '#d6604d', '#f4a582'],
            hue_order=['Yes', 'Some of them', 'No'])
plt.title('Comfort Discussing Mental Health with Supervisor by Company Size', fontsize=14, pad=15)
plt.xlabel('Number of Employees', fontsize=11)
plt.ylabel('% of Respondents', fontsize=11)
plt.legend(title='Open with Supervisor?')
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_supervisor_trust.png'))
plt.close()
print("Chart 4 saved: chart_supervisor_trust.png")

# --- CHART 5: Treatment Rates by Wellness Program ---
df_wellness = df[df['wellness_program'].isin(['Yes', 'No'])]
ct5 = df_wellness.groupby('wellness_program')['treatment_bin'].agg(['mean', 'count']).reset_index()
ct5['pct'] = ct5['mean'] * 100
ct5['wellness_label'] = ct5['wellness_program'].map({'Yes': 'Wellness\nProgram Exists', 'No': 'No Wellness\nProgram'})

plt.figure(figsize=(8, 6))
bars = plt.bar(ct5['wellness_label'], ct5['pct'],
               color=['#4dac26', '#ca0020'], width=0.5, edgecolor='white')
for bar, val in zip(bars, ct5['pct']):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             f'{val:.1f}%', ha='center', va='bottom', fontsize=12, fontweight='bold')
plt.title('Treatment-Seeking Rate by Wellness Program Availability', fontsize=14, pad=15)
plt.ylabel('% Seeking Mental Health Treatment', fontsize=11)
plt.ylim(0, 80)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_wellness_treatment.png'))
plt.close()
print("Chart 5 saved: chart_wellness_treatment.png")
wellness_yes = ct5[ct5['wellness_program']=='Yes']['pct'].values[0]
wellness_no = ct5[ct5['wellness_program']=='No']['pct'].values[0]
print(f"  Treatment WITH wellness program: {wellness_yes:.1f}%")
print(f"  Treatment WITHOUT wellness program: {wellness_no:.1f}%")

# --- CHART 6: Correlation Heatmap ---
df_corr = df.copy()
binary_maps = {
    'treatment': {'Yes': 1, 'No': 0},
    'remote_work': {'Yes': 1, 'No': 0},
    'self_employed': {'Yes': 1, 'No': 0},
    'family_history': {'Yes': 1, 'No': 0},
    'benefits': {'Yes': 1, "Don't know": 0.5, 'No': 0},
    'wellness_program': {'Yes': 1, "Don't know": 0.5, 'No': 0},
    'seek_help': {'Yes': 1, "Don't know": 0.5, 'No': 0},
    'obs_consequence': {'Yes': 1, 'No': 0},
    'mental_health_consequence': {'Yes': 1, 'Maybe': 0.5, 'No': 0},
    'supervisor': {'Yes': 1, 'Some of them': 0.5, 'No': 0},
    'coworkers': {'Yes': 1, 'Some of them': 0.5, 'No': 0},
    'mental_vs_physical': {'Yes': 1, "Don't know": 0.5, 'No': 0},
}
for col, mapping in binary_maps.items():
    df_corr[col + '_num'] = df_corr[col].map(mapping)

df_corr['work_interfere_num'] = df_corr['work_interfere'].map(interfere_map)
df_corr['tech_company_num'] = (df_corr['tech_company'] == 'Yes').astype(int)

numeric_cols = [c for c in df_corr.columns if c.endswith('_num')] + ['Age']
corr_matrix = df_corr[numeric_cols].corr()

labels = {
    'treatment_num': 'Treatment\nSeeking',
    'remote_work_num': 'Remote\nWork',
    'self_employed_num': 'Self\nEmployed',
    'family_history_num': 'Family\nHistory',
    'benefits_num': 'MH\nBenefits',
    'wellness_program_num': 'Wellness\nProgram',
    'seek_help_num': 'Seek Help\nResources',
    'obs_consequence_num': 'Observed\nConsequences',
    'mental_health_consequence_num': 'Fear MH\nConsequences',
    'supervisor_num': 'Supervisor\nTrust',
    'coworkers_num': 'Coworker\nTrust',
    'mental_vs_physical_num': 'MH=Physical\nHealth',
    'work_interfere_num': 'Work\nInterference',
    'tech_company_num': 'Tech\nCompany',
    'Age': 'Age'
}
corr_matrix = corr_matrix.rename(index=labels, columns=labels)

plt.figure(figsize=(14, 12))
sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            center=0, linewidths=0.5, linecolor='white', annot_kws={'size': 8})
plt.title('OSMI Mental Health in Tech — Correlation Heatmap', fontsize=15)
plt.tight_layout()
plt.savefig(os.path.join(output_folder, 'chart_correlation_heatmap.png'), dpi=150)
plt.close()
print("Chart 6 saved: chart_correlation_heatmap.png")

# --- SUMMARY STATS ---
print("\n=== SUMMARY FOR README ===")
print(f"Total respondents: {total}")
print(f"Remote workers: {remote_pct:.1f}%")
print(f"Sought treatment: {treatment_pct:.1f}%")
print(f"No mental health benefits: {no_benefits_pct:.1f}%")
print(f"Remote 'Often' interference: {remote_often:.1f}%")
print(f"Non-remote 'Often' interference: {nonremote_often:.1f}%")
print(f"'Don't know' leave policy: {dontknow_pct:.1f}%")
print(f"Treatment WITH wellness: {wellness_yes:.1f}%")
print(f"Treatment WITHOUT wellness: {wellness_no:.1f}%")
print(f"Benefits 'Often' interference: {benefits_often_yes:.1f}%")
print(f"No benefits 'Often' interference: {benefits_often_no:.1f}%")

# Supervisor trust overall
sup_yes = (df['supervisor'] == 'Yes').mean() * 100
sup_no = (df['supervisor'] == 'No').mean() * 100
print(f"Comfortable with supervisor (Yes): {sup_yes:.1f}%")
print(f"Not comfortable with supervisor (No): {sup_no:.1f}%")

# MH consequence fear
mh_consequence_yes = (df['mental_health_consequence'] == 'Yes').mean() * 100
mh_consequence_maybe = (df['mental_health_consequence'] == 'Maybe').mean() * 100
print(f"Fear MH consequences (Yes): {mh_consequence_yes:.1f}%")
print(f"Fear MH consequences (Maybe): {mh_consequence_maybe:.1f}%")

# obs consequence
obs_yes = (df['obs_consequence'] == 'Yes').mean() * 100
print(f"Witnessed negative MH consequences: {obs_yes:.1f}%")

print("\nAll charts generated successfully!")
