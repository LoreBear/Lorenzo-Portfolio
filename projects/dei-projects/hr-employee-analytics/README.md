# HR Employee Analytics: Workforce Engagement & Retention Analysis
### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-HR%20Analytics%20%7C%20Engagement-green)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Pandas-blueviolet)
![Region](https://img.shields.io/badge/Region-Global-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 🎯 Project Goal
**To develop an evidence-based HR analytics framework that enables HR professionals to measure, analyze, and drive actionable workforce insights using employee survey and HR data, with emphasis on engagement, retention, and performance metrics.**

This project demonstrates how HR Analytics specialists can leverage organizational psychology principles and advanced data analysis to transform HR reporting from basic metrics into strategic business intelligence that drives measurable improvements in employee engagement, retention, and organizational performance.

---

## 📋 Executive Summary

This project analyzes real-world HR employee data to create a comprehensive workforce analytics dashboard. Using organizational psychology principles and advanced analytics, the dashboard identifies key workforce metrics, engagement patterns, retention risks, and provides actionable insights for HR leaders.

### 🔑 Key Findings from Data Analysis
- **Gender Representation**: 24.6% female, 24.4% male, 25.7% non-binary representation
- **Attrition Analysis**: Overall turnover rate of 50.7% with similar rates across genders
- **Engagement Metrics**: Average job satisfaction of 3.04/4 and work-life balance of 3.00/4
- **Performance Correlation**: Average performance rating of 3.04/5 with demographic variations
- **Career Development**: Average training hours of 39.7 per year and average 6.6 years since last promotion

### 💼 Business Value for HR Professionals
This analytics framework enables HR teams to:
1. **Diagnose Engagement Drivers**: Move beyond basic satisfaction scores to understand what truly motivates and retains employees
2. **Measure Retention Risk**: Identify flight risks by analyzing attrition patterns and engagement metrics
3. **Optimize Talent Development**: Analyze training effectiveness and promotion patterns
4. **Enhance Performance Management**: Connect engagement metrics to performance outcomes
5. **Improve Workforce Planning**: Use tenure and role stability data for succession planning
6. **Demonstrate ROI**: Show financial impact of engagement and retention interventions

---

## 👨‍💼 Alignment with Professional Expertise
This project reflects Lorenzo Di Salvatore's specialized expertise in:
- **HR Analytics**: Advanced statistical analysis of HR survey and employee data
- **Organizational Psychology**: Application of psychological theories to workplace engagement, motivation, and retention challenges  
- **People Analytics**: Translation of complex employee behaviors into actionable business insights
- **Data Science**: Python-based data cleaning, analysis, and visualization of HR datasets
- **Evidence-Based HR Practice**: Ensuring HR initiatives are grounded in rigorous data analysis rather than intuition

---

## 📊 Technical Approach

### Data Sources
- **Primary Dataset**: HR Employee Dataset (Kaggle)
- **Variables**: Employee ID, department, gender, age, education level, job role, monthly income, years at company, years in current role, job satisfaction, performance rating, work-life balance, training hours, last promotion, distance from home, overtime, attrition, marital status, stock options
- **Data Quality**: Cleaned and prepared for analysis with proper variable typing and calculated fields (income gaps, tenure analysis)

### Analytical Framework
1. **Descriptive Analysis**: Workforce composition and demographic metrics
2. **Attrition Analysis**: Turnover analysis by gender and department
3. **Engagement Analysis**: Job satisfaction, work-life balance, and engagement metrics
4. **Performance Correlation**: Analysis of relationships between demographics, engagement, and performance
5. **Career Development**: Training hours, promotion patterns, and internal mobility

### Visualization Outputs
- Gender distribution by department (stacked bar chart)
- Attrition rates by demographic group (2x2 comparative analysis)
- Representation trends over hire years (line chart)
- Monthly income distribution by gender (box plot)

---

## 📈 Key Statistical Insights

### Representation Metrics
- Female employees: 24.6% of workforce
- Male employees: 24.4% of workforce  
- Non-binary employees: 25.7% of workforce
- Ethnic minorities: Data not available in source dataset
- Employees with disability: Data not available in source dataset
- LGBTQ+ employees: Data not available in source dataset

### Attrition Analysis
- Overall attrition rate: 50.7%
- Female attrition: 50.7%
- Male attrition: 49.6%
- Non-binary attrition: 52.1%
- Attrition ratio (Female/Male): 1.02

### Engagement Metrics
- Average job satisfaction: 3.04/4
- Average work-life balance: 3.00/4
- Average performance rating: 3.04/5

### Career Development
- Average years at company: 15.8 years
- Average years in current role: 7.5 years
- Average training hours last year: 39.7 hours
- Average years since last promotion: 6.6 years

### Income Equity
- Average male monthly income: 5076 currency units
- Average female monthly income: 5041 currency units  
- Gender income gap: 35 currency units (0.7% favoring males)

---

## 🛠️ Practical Applications for HR Teams

### 1. **Strategic Talent Management**
- Establish baseline metrics for annual talent reviews
- Identify departments with highest turnover risk for targeted intervention
- Create talent segmentation models using engagement and performance data

### 2. **Targeted Engagement Programs**
- Develop engagement initiatives based on survey driver analysis
- Create recognition programs informed by performance and satisfaction correlations
- Implement pulse surveys to track engagement changes in real-time

### 3. **Progress Monitoring & Reporting**
- Establish quarterly workforce dashboard reviews with leadership
- Create automated reporting for trend tracking and goal progress
- Develop executive summaries focused on actionable workforce insights

### 4. **Evidence-Based Decision Making**
- Use statistical validation to confirm engagement observations
- Apply correlation analysis to identify key drivers of retention and performance
- Conduct before/after analysis to measure impact of HR initiatives on workforce metrics

---

## 📁 Repository Contents

```
hr-employee-analytics/
├── README.md                         # This file - Project overview and methodology
├── HR_Dataset.csv                    # HR Employee dataset from Kaggle
├── analysis.py                       # Python analysis script generating all charts and insights
├── charts/                           # Generated visualizations:
│   ├── chart_gender_department.png
│   ├── chart_attrition_demographic.png
│   ├── chart_representation_trends.png
│   └── chart_income_gender.png
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
1. Load and analyze the HR employee dataset
2. Calculate key metrics including representation, attrition, engagement, and income equity
3. Generate four comprehensive visualization charts in the `charts/` directory
4. Print key statistical summary for reporting
5. Output workforce insights and trend analysis

### Customization for Organizational Use
1. Replace `HR_Dataset.csv` with your organization's HR employee survey or HRIS data
2. Update column names in `analysis.py` to match your data structure
3. Adjust demographic categorizations as needed for your workforce
4. Modify visualization parameters to align with corporate branding
5. Add additional analysis modules as needed for specific HR initiatives
6. Incorporate organizational-specific variables (competencies, leadership scores, etc.)

---

## 📞 Professional Contact
For questions about implementing this analytics framework in your organization:
- **LinkedIn**: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
- **Professional Portfolio**: [GitHub Repositories](https://github.com/LoreBear)
- **Specialization**: HR Analytics | Organizational Psychology | People Data Strategy

---

## 📅 Project Metadata
- **Last Updated**: May 2026
- **Data Source**: HR Employee Dataset (Kaggle)
- **Analysis Period**: Cross-sectional data representing current workforce state
- **Sample Size**: [TO BE CALCULATED] employee records
- **Geographic Scope**: Global (dataset origin varies)
- **Industry Scope**: Cross-sector HR measures
- **Update Frequency**: Designed for periodic refresh with new employee survey data

---

> *"Understanding workforce dynamics requires looking beyond surface-level metrics to uncover the psychological drivers of engagement, retention, and performance that truly impact organizational success."*  
> — Aligned with Lorenzo Di Salvatore's professional focus on bridging psychology and data science for evidence-based HR practice