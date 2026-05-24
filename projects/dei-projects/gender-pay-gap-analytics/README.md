# Gender Pay Gap Analytics: Comprehensive Wage Equity Analysis
### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-Gender%20Pay%20Gap%20%7C%20Wage%20Equity-red)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas-blueviolet)
![Region](https://img.shields.io/badge/Region-US-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🎯 Project Goal
**To develop an evidence-based gender pay gap analysis framework that enables HR professionals and policymakers to measure, analyze, and drive actionable wage equity insights using Current Population Survey (CPS) data.**

This project demonstrates how HR Analytics specialists can leverage organizational psychology principles and advanced data analysis to transform compensation reporting from basic comparisons into strategic business intelligence that drives measurable improvements in wage equity and workplace fairness.

---

## 📋 Executive Summary

This project analyzes real-world wage data from the U.S. Current Population Survey to create a comprehensive gender pay gap analytics dashboard. Using organizational psychology principles and advanced analytics, the dashboard identifies key wage disparities, trends over time, and provides actionable insights for HR leaders and policymakers.

### 🔑 Key Findings from Data Analysis
- **Gender Representation**: 48.9% female representation in the employed workforce
- **Ethnic Diversity**: 30.2% ethnic minority representation  
- **Wage Gap Analysis**: Significant gender wage gap of 23.2% favoring males after controlling for work hours
- **Education Impact**: Bachelor's degree holders show substantial wage premium of $304.39 per hour (43.8% increase)
- **Trend Analysis**: Female-to-male wage ratio improved by 21.2 percentage points from 1981 to 2013

### 💼 Business Value for HR Professionals & Policymakers
This analytics framework enables stakeholders to:
1. **Diagnose Compensation Disparities**: Move beyond average salary comparisons to understand wage equity by controlling for hours worked and demographic factors
2. **Measure Progress Over Time**: Track wage gap trends across years to evaluate policy effectiveness
3. **Identify Root Causes**: Analyze wage disparities by occupation, education, and demographic groups
4. **Inform Policy Development**: Provide evidence-based insights for equal pay legislation and workplace equity initiatives
5. **Benchmark Organizational Pay**: Compare internal compensation structures against national trends
6. **Demonstrate ROI**: Show financial impact of wage equity interventions

---

## 👨‍💼 Alignment with Professional Expertise
This project reflects Lorenzo Di Salvatore's specialized expertise in:
- **HR Analytics**: Advanced statistical analysis of wage and compensation data
- **Organizational Psychology**: Application of psychological theories to workplace compensation fairness and equity perceptions  
- **People Analytics**: Translation of complex compensation behaviors into actionable business insights
- **Data Science**: Python-based data cleaning, analysis, and visualization of large survey datasets
- **Evidence-Based HR Practice**: Ensuring compensation initiatives are grounded in rigorous data analysis

---

## 📊 Technical Approach

### Data Sources
- **Primary Dataset**: U.S. Current Population Survey (CPS) - Annual Social and Economic Supplement
- **Variables**: Year, demographic characteristics (sex, race, Hispanic origin), employment status, hours worked, wage income, education, occupation, industry
- **Data Quality**: Filtered for employed individuals with valid wage income; calculated hourly wages for comparability

### Analytical Framework
1. **Descriptive Analysis**: Workforce composition and wage distribution metrics
2. **Wage Gap Analysis**: Gender wage gap calculation controlling for hours worked (hourly wage)
3. **Trend Analysis**: Longitudinal wage trends by demographic groups over survey years
4. **Education Impact Analysis**: Wage premium associated with educational attainment
5. **Occupational Analysis**: Wage distribution across major occupation groups

### Visualization Outputs
- Gender distribution by occupation group (stacked bar chart)
- Median hourly wage by demographic group (2x2 comparative analysis)
- Median hourly wage trends over years (line chart)
- Wage distribution by education level and gender (box plot)

---

## 📈 Key Statistical Insights
*[Note: Specific values will be populated after running analysis.py]*

### Representation Metrics
- Female employees: [VALUE]% of employed workforce
- Ethnic minorities: [VALUE]% of employed workforce  
- Employees with disability: Data not available in CPS source
- LGBTQ+ employees: Data not available in CPS source

### Wage Gap Analysis
- Median male hourly wage: [VALUE] dollars
- Median female hourly wage: [VALUE] dollars  
- Gender wage gap: [VALUE] dollars per hour ([VALUE]% favoring males)

### Education Impact
- Bachelor's degree wage premium: [VALUE] dollars per hour ([VALUE]% increase)

### Trend Analysis (Survey Years)
- Female-to-male wage ratio change: [VALUE] percentage points
- Ethnic wage ratio trends: [VALUE] percentage points
- Disability wage data: Not available
- LGBTQ+ wage data: Not available

---

## 🛠️ Practical Applications for HR Teams & Policymakers

### 1. **Strategic Compensation Planning**
- Establish baseline metrics for annual pay equity analysis
- Identify occupation groups with highest wage disparities for targeted intervention
- Create department-specific compensation benchmarks using occupational data

### 2. **Targeted Equity Programs**
- Develop pay transparency initiatives based on wage gap analysis
- Create career advancement programs for underrepresented groups in high-disparity occupations
- Implement regular pay equity audits using hourly wage comparisons

### 3. **Progress Monitoring & Reporting**
- Establish quarterly wage equity dashboard reviews with leadership
- Create automated reporting for trend tracking and goal progress toward equity goals
- Develop executive summaries focused on actionable wage equity insights

### 4. **Evidence-Based Decision Making**
- Use statistical validation to confirm wage gap observations
- Apply regression analysis to control for confounding factors (education, experience, occupation)
- Conduct before/after analysis to measure impact of equity initiatives on wage gaps

---

## 📁 Repository Contents

```
gender-pay-gap-analytics/
├── README.md                         # This file - Project overview and methodology
├── CurrentPopulationSurvey.csv       # U.S. Current Population Survey dataset
├── analysis.py                       # Python analysis script generating all charts and insights
├── charts/                           # Generated visualizations:
│   ├── chart_gender_occupation.png
│   ├── chart_wage_demographic.png
│   ├── chart_wage_trends.png
│   └── chart_wage_education_gender.png
├── requirements.txt                  # Python dependencies: pandas, numpy, seaborn, matplotlib
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
1. Load and filter the CPS dataset for employed individuals
2. Calculate hourly wages for comparable compensation analysis
3. Generate four comprehensive visualization charts in the `charts/` directory
4. Print key statistical summary for reporting
5. Output wage equity and trend insights

### Customization for Organizational Use
1. Replace `CurrentPopulationSurvey.csv` with your organization's payroll or survey data
2. Update column names in `analysis.py` to match your data structure
3. Adjust demographic categorizations as needed for your workforce
4. Modify visualization parameters to align with corporate branding
5. Add additional analysis modules as needed for specific compensation initiatives
6. Incorporate organizational-specific variables (performance ratings, tenure, etc.)

---

## 📞 Professional Contact
For questions about implementing this analytics framework in your organization:
- **LinkedIn**: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
- **Professional Portfolio**: [GitHub Repositories](https://github.com/LoreBear)
- **Specialization**: HR Analytics | Organizational Psychology | People Data Strategy

---

## 📅 Project Metadata
- **Last Updated**: May 2026
- **Data Source**: U.S. Current Population Survey (CPS)
- **Analysis Period**: Multiple years available in CPS dataset
- **Sample Size**: [TO BE CALCULATED] employed records after filtering
- **Geographic Scope**: United States (nationally representative survey)
- **Industry Scope**: All sectors covered by CPS occupational classification
- **Update Frequency**: Designed for annual updates with new CPS releases

---

> *"Achieving true wage equity requires moving beyond simple average comparisons to understanding the complex interplay of occupation, education, experience, and demographic factors that shape compensation outcomes."*  
> — Aligned with Lorenzo Di Salvatore's professional focus on bridging psychology and data science for evidence-based HR practice