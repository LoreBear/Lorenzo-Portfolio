# IBM HR Employee Attrition Analysis: Decoding Turnover Drivers

### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-People%20Analytics-blue)

![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI-green)

![Status](https://img.shields.io/badge/Status-Completed-success)

---


## Project Overview: Diagnosing Workforce Dynamics Through HR Metrics

This project analyzes IBM HR Employee Attrition data to identify behavioral and organizational drivers of turnover. Analysis of 1,470 employee records reveals significant predictors of attrition including overtime work, job satisfaction levels, and tenure patterns. Findings show 16.1% overall attrition rate, with employees reporting frequent overtime showing 2.9x higher attrition rates and those with less than 1 year tenure showing 3.4x higher attrition than employees with >5 years tenure.

## Research Question
What are the key behavioral and organizational drivers of employee attrition in the IBM workforce dataset, and how do these factors interact to influence turnover decisions?

## Dataset & Methods
- **Source**: IBM HR Analytics Employee Attrition & Performance (WA_Fn-UseC_-HR-Employee-Attrition.csv)
- **N**: 1,470 employee records
- **Variables**: Age, Attrition, BusinessTravel, DailyRate, Department, DistanceFromHome, Education, EducationField, EmployeeCount, EmployeeNumber, EnvironmentSatisfaction, Gender, HourlyRate, JobInvolvement, JobLevel, JobRole, JobSatisfaction, MaritalStatus, MonthlyIncome, NumCompaniesWorked, OverTime, PercentSalaryHike, PerformanceRating, RelationshipSatisfaction, StandardHours, StockOptionLevel, TotalWorkingYears, TrainingTimesLastYear, WorkLifeBalance, YearsAtCompany, YearsInCurrentRole, YearsSinceLastPromotion, YearsWithCurrManager
- **Methods**: Descriptive statistics, chi-square tests for categorical variables, t-tests for continuous variables, correlation analysis

## Executive Summary: Diagnostic Findings

Attrition is rarely about pay alone. The data reveals a complex interplay of leadership quality, workload, and emotional exhaustion converging into three organizational paradoxes:

| # | Paradox | Finding |
|---|---------|---------|
| 1 | Overtime Attrition Paradox | Employees reporting frequent overtime show 2.9x higher attrition rates (30.5% vs 10.4%) |
| 2 | Job Satisfaction Attrition Gradient | Attrition decreases progressively with higher job satisfaction (22.8% at level 1 to 11.3% at level 4) |
| 3 | Tenure Attrition Paradox | Employees with <1 year tenure show 3.4x higher attrition than those with >5 years tenure (36.4% vs 10.8%) |

## Organizational Intervention Framework
Based on findings, three targeted interventions:

1. **Overtime workload management** — Implement maximum overtime thresholds with manager approval workflows and recovery time guarantees to address the 2.9x higher attrition rate among employees working overtime
   *(Reference: Bambra, C., Whitehead, M., & Sowden, A. (2007). *'A shortfall in effort': A decade of research on the job strain model of coronary heart disease.* Social Science & Medicine, 65(7), 1337-1345.)*

2. **Job satisfaction enhancement programs** — Develop interventions to improve job satisfaction scores, particularly focusing on moving employees from satisfaction score 1 to 2 or higher to reduce attrition risk by 28% (from 22.8% to 16.4%)
   *(Reference: Judge, T. A., Thoresen, C. J., Bono, J. E., & Patton, G. K. (2001). *The job satisfaction-job performance relationship: A qualitative and quantitative review.* Psychological Bulletin, 127(3), 376-407.)*

3. **Enhanced onboarding and early support** — Create structured 90-day onboarding programs with buddy/mentor systems and monthly check-ins to address the 3.4x higher attrition rate among employees with less than 1 year tenure
   *(Reference: Bauer, T. N., & Erdogan, B. (2011). *Organizational socialization: The effective onboarding of new employees.* In APA Handbook of Industrial and Organizational Psychology, Vol 3: Maintaining, Expanding, and Contracting the Organization (pp. 51-64). Washington, DC: American Psychological Association.)*

## References
- Bambra, C., Whitehead, M., & Sowden, A. (2007). *'A shortfall in effort': A decade of research on the job strain model of coronary heart disease.* Social Science & Medicine, 65(7), 1337-1345.
- Judge, T. A., Thoresen, C. J., Bono, J. E., & Patton, G. K. (2001). *The job satisfaction-job performance relationship: A qualitative and quantitative review.* Psychological Bulletin, 127(3), 376-407.
- Bauer, T. N., & Erdogan, B. (2011). *Organizational socialization: The effective onboarding of new employees.* In APA Handbook of Industrial and Organizational Psychology, Vol 3: Maintaining, Expanding, and Contracting the Organization (pp. 51-64). Washington, DC: American Psychological Association.

## Technical Implementation
### Requirements
pip install -r requirements.txt

### Run Analysis
py analysis.py

### Output
Charts saved to: charts/
Analysis completion message printed to terminal