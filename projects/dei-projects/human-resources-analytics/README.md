# Human Resources Analytics: DEI & Workforce Analysis
### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-HR%20Analytics%20%7C%20DEI-blue)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas-blueviolet)
![Region](https://img.shields.io/badge/Region-US-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🎯 Project Goal
**To develop an evidence-based HR analytics framework that enables HR professionals to measure, analyze, and drive actionable workforce insights using comprehensive organizational data, with emphasis on diversity, equity, and inclusion metrics where available.**

This project demonstrates how HR Analytics specialists can leverage organizational psychology principles and advanced data analysis to transform HR reporting from compliance-driven metrics into strategic business intelligence that drives measurable improvements in workforce equity, inclusion, and performance.

---

## 📋 Executive Summary

This project analyzes real-world HR data from the Kaggle Human Resources Dataset to create a comprehensive workforce analytics dashboard. Using organizational psychology principles and advanced analytics, the dashboard identifies key workforce metrics, representation trends, compensation equity, and provides actionable insights for HR leaders.

### 🔑 Key Findings from Data Analysis
- **Gender Representation**: 56.6% female representation in the dataset
- **Ethnic Diversity**: 45.7% ethnic minority representation  
- **Attrition Analysis**: Overall voluntary turnover rate of 28.3%, with females showing 6% higher attrition than males
- **Compensation Equity**: Gender pay gap of 4.0% favoring males (average male salary: $70,629 vs female: $67,787)
- **Workforce Composition**: Detailed demographic and employment metrics available

### 💼 Business Value for HR Professionals
This analytics framework enables HR teams to:
1. **Diagnose Workforce Trends**: Move beyond basic headcount to understand workforce composition and dynamics
2. **Measure DEI Progress**: Track diversity metrics where data is available (gender, ethnicity)
3. **Identify Retention Risks**: Analyze attrition patterns by demographic groups
4. **Compensation Analysis**: Examine salary distributions and identify potential equity gaps
5. **Performance Correlation**: Explore relationships between demographics, performance, and engagement
6. **Demonstrate ROI**: Provide evidence-based reporting to stakeholders on HR initiative effectiveness

---

## 👨‍💼 Alignment with Professional Expertise
This project reflects Lorenzo Di Salvatore's specialized expertise in:
- **HR Analytics**: Advanced statistical analysis of workforce data including compensation, performance, and retention metrics
- **Organizational Psychology**: Application of psychological theories to workplace workforce challenges  
- **People Analytics**: Translation of complex human behavior into actionable business insights
- **Data Science**: Python-based data cleaning, analysis, and visualization
- **Evidence-Based HR Practice**: Ensuring HR initiatives are grounded in data rather than assumptions

---

## 📊 Technical Approach

### Data Sources
- **Primary Dataset**: Kaggle Human Resources Dataset (HRDataset_v14.csv)
- **Variables**: Employee ID, name, gender, marital status, citizenship, Hispanic/Latino ethnicity, race description, date of birth, sex, department, salary, hire date, termination date, performance scores, engagement surveys, satisfaction metrics, and employment status
- **Data Quality**: Cleaned and prepared for analysis with proper variable typing and calculated fields (age, hire year, attrition flag)

### Analytical Framework
1. **Descriptive Analysis**: Workforce composition metrics across available demographic groups
2. **Attrition Analysis**: Voluntary turnover analysis by gender and ethnicity (where available)
3. **Trend Analysis**: Longitudinal representation trends by hire year cohorts
4. **Compensation Analysis**: Salary distribution analysis with gender pay gap calculation
5. **Experience Metrics**: Analysis of engagement, satisfaction, and performance correlations

### Visualization Outputs
- Gender distribution by department (stacked bar chart)
- Attrition rates by demographic group (2x2 comparative analysis)
- Representation trends over hire years (line chart)
- Salary distribution by gender (box plot with mean indicators)

---

## 📈 Key Statistical Insights

### Representation Metrics
- Female employees: 56.6% of workforce
- Ethnic minorities: 45.7% of workforce  
- Employees with disability: Data not available in source dataset
- LGBTQ+ employees: Data not available in source dataset

### Attrition Analysis
- Overall attrition rate: 28.3%
- Female attrition: 29.0%
- Male attrition: 27.4%
- Attrition ratio (Female/Male): 1.06

### Compensation Equity
- Average male salary: 70,629 currency units
- Average female salary: 67,787 currency units  
- Gender pay gap: 2,843 currency units (4.0% favoring males)

### Trend Analysis (Hire Year Cohorts 2006 to 2018)
- Female representation: +0.0 percentage points change
- Ethnic minority representation: +0.0 percentage points change
- Disability representation: Data not available
- LGBTQ+ representation: Data not available

---

## 🛠️ Practical Applications for HR Teams

### 1. **Strategic Workforce Planning**
- Establish baseline metrics for annual workforce planning
- Identify workforce composition trends for strategic planning
- Create department-specific workforce profiles using detailed organizational data

### 2. **Targeted Intervention Programs**
- Develop retention initiatives based on attrition pattern analysis
- Create workforce development programs informed by engagement and satisfaction data
- Implement workforce planning initiatives using hire trend analysis

### 3. **Progress Monitoring & Reporting**
- Establish quarterly workforce dashboard reviews with leadership
- Create automated reporting for trend tracking and goal progress
- Develop executive summaries focused on actionable workforce insights

### 4. **Evidence-Based Decision Making**
- Use statistical analysis to validate workforce observations
- Apply correlation analysis to prioritize HR interventions
- Conduct before/after analysis to measure initiative impact on workforce metrics

---

## 📁 Repository Contents

```
human-resources-analytics/
├── README.md                         # This file - Project overview and methodology
├── HRDataset_v14.csv                 # Human Resources dataset from Kaggle
├── analysis.py                       # Python analysis script generating all charts and insights
├── charts/                           # Generated visualizations:
│   ├── chart_gender_department.png
│   ├── chart_attrition_demographic.png
│   ├── chart_representation_trends.png
│   └── chart_salary_gender.png
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
1. Load and analyze the HR dataset
2. Calculate age from date of birth and hire year from hire date
3. Generate four comprehensive visualization charts in the `charts/` directory
4. Print key statistical summary for reporting
5. Output workforce composition and trend insights

### Customization for Organizational Use
1. Replace `HRDataset_v14.csv` with your organization's HR dataset
2. Update column names in `analysis.py` to match your data structure
3. Adjust demographic categorizations as needed for your workforce
4. Modify visualization parameters to align with corporate branding
5. Add additional analysis modules as needed for specific HR initiatives
6. Incorporate disability and LGBTQ+ status tracking if available in your data

---

## 📞 Professional Contact
For questions about implementing this analytics framework in your organization:
- **LinkedIn**: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
- **Professional Portfolio**: [GitHub Repositories](https://github.com/LoreBear)
- **Specialization**: HR Analytics | Organizational Psychology | People Data Strategy

---

## 📅 Project Metadata
- **Last Updated**: May 2026
- **Data Source**: Kaggle Human Resources Dataset
- **Analysis Period**: Calculated from hire date range in dataset
- **Sample Size**: [TO BE CALCULATED] employee records
- **Geographic Scope**: United States (based on state fields in dataset)
- **Industry Scope**: Cross-sector HR measures
- **Update Frequency**: Designed for periodic refresh with new HR data

---

> *"Effective HR analytics transforms workforce data from simple headcounts into strategic insights that drive better people decisions and organizational outcomes."*  
> — Aligned with Lorenzo Di Salvatore's professional focus on bridging psychology and data science for evidence-based HR practice