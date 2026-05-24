# DEI Dashboard EMEA: Diversity, Equity & Inclusion Analytics
### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-DEI%20Analytics-purple)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Jupyter-blueviolet)
![Region](https://img.shields.io/badge/Region-EMEA-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🎯 Project Goal
**To develop an evidence-based DEI analytics framework that enables HR professionals to measure, analyze, and drive actionable diversity, equity, and inclusion initiatives using real organizational data.**

This project demonstrates how HR Analytics specialists can leverages organizational psychology principles and advanced data analysis to transform DEI from compliance-driven reporting into strategic business intelligence that drives measurable improvements in workplace equity and inclusion.

---

## 📋 Executive Summary

This project analyzes real-world HR data from Kaggle DEI datasets to create a comprehensive Diversity, Equity & Inclusion analytics dashboard. Using organizational psychology principles and advanced analytics, the dashboard identifies key DEI metrics, representation trends, compensation equity, and provides actionable insights for HR leaders.

### 🔑 Key Findings from Real Data Analysis
- **Gender Representation**: 33.9% female representation in the dataset
- **Ethnic Diversity**: 29.1% ethnic minority representation  
- **Attrition Disparity**: Female employees show 33% higher voluntary turnover than male employees (Attrition Ratio: 1.33)
- **Compensation Equity**: Significant gender pay gap favoring men (7.9% higher average salary for males)
- **Representation Trends**: Slight declines in female and ethnic minority representation in recent hiring cohorts (2020-2023)

### 💼 Business Value for HR Professionals
This analytics framework enables HR teams to:
1. **Diagnose Systemic Barriers**: Move beyond surface-level statistics to identify root causes of DEI challenges
2. **Measure Intervention Impact**: Track progress of DEI initiatives with quantifiable metrics
3. **Prioritize Resources**: Focus investment where disparities are most pronounced
4. **Demonstrate ROI**: Provide evidence-based reporting to stakeholders on DEI investment effectiveness
5. **Ensure Compliance**: Proactively identify and address equity gaps before regulatory issues arise

---

## 👨‍💼 Alignment with Professional Expertise
This project reflects Lorenzo Di Salvatore's specialized expertise in:
- **HR Analytics**: Advanced statistical analysis of workforce data
- **Organizational Psychology**: Application of psychological theories to workplace DEI challenges  
- **People Analytics**: Translation of complex human behavior into actionable business insights
- **Data Science**: Python-based data cleaning, analysis, and visualization
- **Evidence-Based HR Practice**: Ensuring DEI initiatives are grounded in data rather than assumptions

---

## 📊 Technical Approach

### Data Sources
- **Primary Dataset**: Kaggle Diversity, Equity and Inclusion Measures Dataset (10,000 records)
- **Variables**: Gender, ethnicity, age, disability status, LGBTQ+ status, division, manager, hire year, performance rating, salary, attrition
- **Data Quality**: Cleaned and prepared for analysis with proper variable typing and synthetic HR metrics added for comprehensive analysis

### Analytical Framework
1. **Descriptive Analysis**: Representation metrics across demographic groups
2. **Attrition Analysis**: Disparity analysis by gender, ethnicity, disability, and LGBTQ+ status
3. **Trend Analysis**: Longitudinal representation trends by hire year cohorts
4. **Compensation Analysis**: Salary equity analysis with gender pay gap calculation
5. **Statistical Validation**: Chi-square tests, t-tests, and effect size calculations

### Visualization Outputs
- Gender distribution by division (stacked bar chart)
- Attrition rates by demographic group (2x2 comparative analysis)
- Representation trends over hire years (line chart)
- Salary distribution by gender (box plot with mean indicators)

---

## 📈 Key Statistical Insights

### Representation Metrics
- Female employees: 33.9% of workforce
- Ethnic minorities: 29.1% of workforce  
- Employees with disability: 0.0% (data limitation in source)
- LGBTQ+ employees: 0.0% (data limitation in source)

### Attrition Analysis
- Overall attrition rate: 17.0%
- Female attrition: 20.4% (33% higher than male)
- Male attrition: 15.3%
- Attrition ratio (Female/Male): 1.33

### Compensation Equity
- Average male salary: 63,643 currency units
- Average female salary: 58,623 currency units  
- Gender pay gap: 5,020 currency units (7.9% favoring males)

### Trend Analysis (2020-2023 Hiring Cohorts)
- Female representation: -0.6 percentage points change
- Ethnic minority representation: -1.1 percentage points change
- Disability representation: 0.0 percentage points change
- LGBTQ+ representation: 0.0 percentage points change

---

## 🛠️ Practical Applications for HR Teams

### 1. **Strategic DEI Planning**
- Establish baseline metrics for annual DEI goal setting
- Identify priority areas for intervention based on disparity analysis
- Create department-specific DEI targets using division-level data

### 2. **Targeted Intervention Programs**
- Develop retention initiatives for female employees (addressing 33% higher attrition)
- Create pipeline programs for ethnic minority talent acquisition and advancement
- Implement regular pay equity audits to monitor and address compensation gaps

### 3. **Progress Monitoring & Reporting**
- Establish quarterly DEI dashboard reviews with leadership
- Create automated reporting for trend tracking and goal progress
- Develop executive summaries focused on actionable insights

### 4. **Evidence-Based Decision Making**
- Use statistical significance testing to validate observations
- Apply effect size calculations to prioritize interventions
- Conduct before/after analysis to measure initiative impact

---

## 📁 Repository Contents

```
dei-dashboard-emea/
├── README.md                         # This file - Project overview and methodology
├── real_dei_data.csv                 # Cleaned DEI dataset from Kaggle (10,000 records)
├── analysis.py                       # Python analysis script generating all charts and insights
├── charts/                           # Generated visualizations:
│   ├── chart_gender_division.png
│   ├── chart_attrition_demographic.png
│   ├── chart_representation_trends.png
│   └── chart_salary_gender.png
├── dei_dashboard_emea.ipynb          # Original Jupyter notebook (exploratory analysis)
└── requirements.txt                  # Python dependencies: pandas, numpy, seaborn, matplotlib
```

---

## 🔧 Implementation & Usage

### Prerequisites
```bash
pip install -r requirements.txt
```

### Generate Analysis & Visualizations
```bash
python analysis.py
```
This will:
1. Load and analyze the real DEI dataset
2. Generate four comprehensive visualization charts in the `charts/` directory
3. Print key statistical summary for reporting
4. Save cleaned dataset as `real_dei_data.csv`

### Customization for Organizational Use
1. Replace `real_dei_data.csv` with your organization's DEI dataset
2. Update column names in `analysis.py` to match your data structure
3. Adjust demographic categorizations as needed for your workforce
4. Modify visualization parameters to align with corporate branding
5. Add additional analysis modules as needed for specific DEI initiatives

---

## 📞 Professional Contact
For questions about implementing this analytics framework in your organization:
- **LinkedIn**: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
- **Professional Portfolio**: [GitHub Repositories](https://github.com/LoreBear)
- **Specialization**: HR Analytics | Organizational Psychology | People Data Strategy

---

## 📅 Project Metadata
- **Last Updated**: May 2026
- **Data Source**: Kaggle Diversity, Equity and Inclusion Measures Dataset
- **Analysis Period**: 2020-2023 hiring cohorts
- **Sample Size**: 10,000 employee records
- **Geographic Scope**: Global (dataset origin varies)
- **Industry Scope**: Cross-sector DEI measures
- **Update Frequency**: Designed for periodic refresh with new data

---

> *"The goal of DEI analytics is not just to measure diversity, but to create measurable improvement in equity and inclusion outcomes through evidence-based intervention."*  
> — Aligned with Lorenzo Di Salvatore's professional focus on bridging psychology and data science for evidence-based HR practice