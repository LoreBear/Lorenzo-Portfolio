import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# --- 1. Setup Percorsi (Sempre all'inizio!) ---
current_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(current_dir, 'charts')
os.makedirs(output_folder, exist_ok=True)

path_heatmap = os.path.join(output_folder, 'chart_correlation_heatmap.png')

# Stile grafici
sns.set(style="whitegrid")

# --- 2. Caricamento Dataset ---
try:
    # Assicurati che il CSV sia nella stessa cartella dello script
    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")
    print("Dataset caricato con successo!")
except FileNotFoundError:
    print("ERRORE: File CSV non trovato. Controlla il nome del file.")
    exit()

# --- 3. Preparazione Dati per Heatmap ---
# Convertiamo Attrition in numero per vederlo nella mappa
df_numeric = df.copy()
df_numeric['Attrition'] = df_numeric['Attrition'].map({'Yes': 1, 'No': 0})

# Selezioniamo solo i numeri e rimuoviamo colonne inutili (costanti)
df_corr = df_numeric.select_dtypes(include=[np.number]).copy()
df_corr = df_corr.loc[:, df_corr.nunique() > 1]

# --- 4. Generazione Heatmap ---
if df_corr.shape[1] >= 2:
    print("\n--- Generazione Correlation Heatmap ---")
    corr_matrix = df_corr.corr()

    plt.figure(figsize=(14, 12))
    sns.heatmap(
        corr_matrix,
        annot=False, # Metti True se vuoi vedere i numeri (diventa molto affollato)
        fmt=".2f",
        cmap='coolwarm',
        center=0,
        linewidths=0.5,
        linecolor='white'
    )
    plt.title('IBM HR Correlation Heatmap', fontsize=15)
    plt.tight_layout()
    
    # Salvataggio - rimuovi attributo di sola lettura se presente
    if os.path.exists(path_heatmap):
        os.chmod(path_heatmap, 0o666)  # Rendi il file scrivibile
    plt.savefig(path_heatmap, dpi=150)
    print(f"Heatmap salvata in: {path_heatmap}")
    plt.show() # Mostra a video
    plt.close()
else:
    print("Dati insufficienti per la heatmap.")

# --- 5. Altri Grafici (Esempio Attrition by Department) ---
plt.figure(figsize=(10, 6))
sns.countplot(x='Department', hue='Attrition', data=df, palette='viridis')
plt.title('Attrition Distribution by Department')
path_attrition_dept = os.path.join(output_folder, 'chart_attrition_by_dept.png')
if os.path.exists(path_attrition_dept):
    os.chmod(path_attrition_dept, 0o666)  # Rendi il file scrivibile
plt.savefig(path_attrition_dept)
plt.close()

# --- 6. Print Summary for README ---
print("\n=== SUMMARY FOR README ===")
print(f"Total employees: {len(df)}")
print(f"Overall attrition rate: {df['Attrition'].value_counts(normalize=True)['Yes']*100:.1f}%")
print(f"Average age: {df['Age'].mean():.1f} years")
print(f"Average monthly income: ${df['MonthlyIncome'].mean():.0f}")
print(f"Average years at company: {df['YearsAtCompany'].mean():.1f} years")
print("\nOvertime analysis:")
overtime_yes = df[df['OverTime'] == 'Yes']
overtime_no = df[df['OverTime'] == 'No']
overtime_attrition_yes = len(overtime_yes[overtime_yes['Attrition'] == 'Yes']) / len(overtime_yes) * 100
overtime_attrition_no = len(overtime_no[overtime_no['Attrition'] == 'Yes']) / len(overtime_no) * 100
print(f"  With overtime: {len(overtime_yes)} employees, {overtime_attrition_yes:.1f}% attrition rate")
print(f"  Without overtime: {len(overtime_no)} employees, {overtime_attrition_no:.1f}% attrition rate")
print(f"  Overtime attrition ratio: {overtime_attrition_yes/overtime_attrition_no:.1f} ({overtime_attrition_yes:.1f}%/{overtime_attrition_no:.1f}%)")
print("\nJob satisfaction analysis:")
for i in range(1, 5):
    sat_level = df[df['JobSatisfaction'] == i]
    if len(sat_level) > 0:
        sat_attrition = len(sat_level[sat_level['Attrition'] == 'Yes']) / len(sat_level) * 100
        print(f"  Satisfaction {i}: {sat_attrition:.1f}% attrition")
print("\nTenure analysis:")
tenure_groups = [
    ("<1 year", df[df['YearsAtCompany'] < 1]),
    ("1-2 years", df[(df['YearsAtCompany'] >= 1) & (df['YearsAtCompany'] < 2)]),
    ("2-5 years", df[(df['YearsAtCompany'] >= 2) & (df['YearsAtCompany'] < 5)]),
    (">5 years", df[df['YearsAtCompany'] >= 5])
]
for label, group in tenure_groups:
    if len(group) > 0:
        attrition_rate = len(group[group['Attrition'] == 'Yes']) / len(group) * 100
        print(f"  {label}: {len(group)} employees, {attrition_rate:.1f}% attrition")
if len(df[df['YearsAtCompany'] < 1]) > 0 and len(df[df['YearsAtCompany'] >= 5]) > 0:
    lt1_rate = len(df[(df['YearsAtCompany'] < 1) & (df['Attrition'] == 'Yes')]) / len(df[df['YearsAtCompany'] < 1]) * 100
    gt5_rate = len(df[(df['YearsAtCompany'] >= 5) & (df['Attrition'] == 'Yes')]) / len(df[df['YearsAtCompany'] >= 5]) * 100
    print(f"  Tenure attrition ratio (<1yr vs >5yr): {lt1_rate/gt5_rate:.1f} ({lt1_rate:.1f}%/{gt5_rate:.1f}%)")
print("\n--- Analisi completata! Controlla la cartella 'charts' ---")