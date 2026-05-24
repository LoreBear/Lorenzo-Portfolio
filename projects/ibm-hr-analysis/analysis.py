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
    
    # Salvataggio
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
plt.savefig(os.path.join(output_folder, 'chart_attrition_by_dept.png'))
plt.close()

print("\n--- Analisi completata! Controlla la cartella 'charts' ---")