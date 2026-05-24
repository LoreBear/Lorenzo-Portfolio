# HR Behavioral Analytics: Decoding Turnover & Burnout
### Project by Lorenzo Di Salvatore  
Work and Organizational Psychology | HR Data Analytics

![Focus](https://img.shields.io/badge/Focus-People%20Analytics-blue)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Executive Summary

Why do employees leave?

This project analyzes HR Dataset v14 (1,470 employees) to identify behavioral drivers of attrition, burnout risk, and structural inequity using Python and Power BI.

The goal is to move from descriptive HR reporting to organizational diagnostics and risk detection.

### Key Findings

• High performers show higher absence rates (10.5 vs 8.3 days)  
• Two managers drive ~62% attrition inside their teams  
• “Unhappy” exit reason ranks above salary-driven exits  

---

## Visual Analysis and Organizational Diagnostics

---

### Executive Workforce Snapshot

![Dashboard Overview](Dashboard.png)
(Dashboard Overview)

**What data shows**

• Attrition Rate: 33%  
• Avg Engagement: 4.09  
• Avg Salary: 69K  
• Gender Pay Gap Index: 0.04  

**Business Meaning**
Attrition concentration appears at manager level, not company level.

---

### Managerial Risk Concentration

(Contained in dashboard overview)

**Observation**
Two managers exceed 60% attrition while most stay below 20%.

**Business Meaning**
Turnover links strongly to leadership quality.

**Action**
Target leadership coaching before launching global retention programs.

---

### Recruitment Channel Distribution

(Contained in dashboard overview)

**Observation**
Indeed and LinkedIn generate most hires.

**Risk**
High dependency on few external talent pipelines.

---

### Workforce Composition and DEI Context

![DEI Overview](DE&I.png)
(DEI Overview)

**Population Distribution**
Majority White workforce, followed by Black or African American and Asian employees.

**Why This Matters**
Population structure must be evaluated before interpreting pay gap or attrition variance.

---

### Gender Pay Gap by Department

(Contained in DEI overview)

**Observation**
• Sales favors female salary levels  
• IT/IS favors male salary levels  

**Root Driver**
Salary correlates 0.51 with SpecialProjectsCount.  
Project allocation likely influences pay distribution.

---

### Attrition by Life Context

(Contained in DEI overview)

**Observation**
Higher termination counts in Single and Married groups reflect workforce composition.

**Use Case**
Validates attrition models against demographic distribution.

---

### Termination Reasons: Culture vs Market

![Termination Reasons](hr_termination_reasons.png)

**What data shows**

• Another Position ranks first  
• Unhappy ranks second  
• More Money ranks third  

**Business Meaning**
Cultural dissatisfaction drives exits more than compensation alone.

**Analysis:** I found that **"Unhappy"** (14 cases) is a more significant exit driver than "More Money" (11 cases). This signals a breakdown in the organizational climate. As a psychologist, I interpret this as a clear indicator that cultural intervention is more urgent than a general pay raise.


---

### Burnout Risk Detection

![Engagement vs Absences](hr_engagement_vs_absences.png)

**What data shows**
High performers record highest absence averages.

**Business Meaning**
Early burnout indicator, not disengagement.

**Analysis:** The data reveals a counter-intuitive trend: top performers ("Exceeds") have higher absence rates (10.5 days) than low performers (8.3 days). This is a **Leading Indicator of Burnout**. These employees are over-extending themselves, using absences as a coping mechanism before eventual resignation.

---

### Structural Pay Equity Pattern

![Gender Pay Equity](hr_gender_pay_equity.png)

**What data shows**
Pay variance exists at department level, not company level.

**Analysis:** The pay gap in the IT/IS department is strongly linked to the **0.51 correlation** between salary and `SpecialProjectsCount`. This suggests that the "gap" is likely a result of unequal access to high-visibility projects rather than direct salary bias.

---

## Technical Architecture

---

### Data Engineering Layer (Python)

Tools  
• kagglehub  
• pandas  
• seaborn  
• matplotlib  

Work Completed  
• Automated dataset ingestion  
• Removed trailing whitespace in categorical columns  
• Created binary Attrition variable  
• Built correlation models between workload, salary, and absence  

---

### Business Intelligence Layer (Power BI)

Goal: Convert statistical output into decision interface.

#### Core DAX Measure

```dax
Attrition Rate =
DIVIDE(
    CALCULATE(COUNTROWS('HR_Data'),
    'HR_Data'[Status] = "Terminated"),
    COUNTROWS('HR_Data'),
    0
)
```

Other Measures  
• Gender Pay Gap Index  
• Manager Attrition Risk Ranking  
• Workforce Engagement Index  

---

### Dashboard Decision Flow

Executive Layer  
• Attrition KPI  
• Engagement KPI  
• Salary KPI  

Diagnostic Layer  
• Burnout Signals  
• Termination Drivers  

Root Cause Layer  
• Manager Attrition Ranking  
• Department Pay Equity  

---

## Strategic Actions

### Leadership Intervention
Focus on highest attrition managers first.

### Burnout Early Warning
Flag employees with:
Performance > 4  
Absences > 10  

Treat as retention risk group.

### Project Allocation Audit
Review Special Project assignment distribution inside IT.

---

## Business Value

Python identifies statistical relationships.  
Power BI translates results into operational decisions.

Outcome: shift from reactive hiring to predictive retention strategy.

---

## Author

Lorenzo Di Salvatore  
HR Analytics | Organizational Psychology | People Data Strategy
* LinkedIn: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
* Portfolio: [GitHub Repositories](https://github.com/LoreBear)

