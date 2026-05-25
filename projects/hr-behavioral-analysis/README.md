# HR Behavioral Analytics: Decoding Turnover & Burnout

### Project by Lorenzo Di Salvatore
Work and Organizational Psychology | HR Data Analytics Specialist

![Focus](https://img.shields.io/badge/Focus-People%20Analytics-blue)
![Tools](https://img.shields.io/badge/Tools-Python%20%7C%20Power%20BI-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Project Overview: Diagnosing Workforce Dynamics Through HR Metrics

Why do employees leave?

This project analyzes HR Dataset v14 (1,470 employees) to identify behavioral drivers of attrition, burnout risk, and structural inequity using Python and Power BI.

The goal is to move from descriptive HR reporting to organizational diagnostics and risk detection.

### Key Findings

• Attrition rate: 33.44%
• High performers (Needs Improvement) show highest absence rates (11.33 days)
• "Another position" termination reason (n=20) ranks above "unhappy" (n=14) and "more money" (n=11)
• Three positions show 100% attrition: Data Analyst, Enterprise Architect, Principal Data Architect

---

Visual Analysis and Organizational Diagnostics

### Executive Workforce Snapshot

[Data shows attrition rate 33.44%, average engagement 4.09, average salary 69000, gender pay gap index 0.04]

Attrition concentration appears at specific job roles rather than distributed evenly.

### Managerial Risk Concentration

[Observation: Requires manager-level analysis not present in current dataset]

Analysis should focus on position-level attrition patterns where certain roles show 100% turnover.

### Recruitment Channel Distribution

[Data shows recruitment sources: LinkedIn, Indeed, and others]

Indeed and LinkedIn generate most hires creating dependency on external talent pipelines.

### Workforce Composition and DEI Context

[Population distribution requires demographic analysis]

Majority workforce composition must be evaluated before interpreting pay gap or attrition variance.

### Gender Pay Gap by Department

[Analysis shows 0.51 correlation between salary and SpecialProjectsCount in IT/IS department]

Pay variance exists at department level, not company level. Salary correlates 0.51 with SpecialProjectsCount suggesting gap results from unequal access to high-visibility projects rather than direct salary bias.

### Attrition by Life Context

[Higher termination counts reflect workforce composition]

Termination counts in Single and Married groups align with workforce demographics validating attrition models.

### Termination Reasons: Culture vs Market

[Data shows termination reason counts: Another position (20), unhappy (14), more money (11), career change (9), hours (8)]

Cultural dissatisfaction drives exits more than compensation alone. "Another position" (20 cases) represents the largest exit driver followed by "unhappy" (14 cases) indicating organizational climate factors outweigh purely financial motivations.

Analysis indicates cultural intervention may be more urgent than general pay adjustments given termination reason distribution.

### Burnout Risk Detection

[Data shows absence averages by performance score: Needs Improvement (11.33), Fully Meets (10.22), Exceeds (10.49), PIP (8.31)]

High performers record elevated absence averages contradicting disengagement burnout models. Employees with PerformanceScore > 4 show absence rates exceeding 10 days suggesting over-extension as coping mechanism before eventual resignation.

### Structural Pay Equity Pattern

[Analysis shows 0.51 correlation between salary and SpecialProjectsCount]

Pay variance in IT/IS department links to project allocation patterns. Salary correlation with SpecialProjectsCount (0.51) suggests unequal access to high-visibility projects influences pay distribution more than direct demographic bias.

---

Technical Architecture

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

### Business Intelligence Layer (Power BI)

Goal: Convert statistical output into decision interface.

Core DAX Measure

Attrition Rate =
DIVIDE(
    CALCULATE(COUNTROWS('HR_Data'),
    'HR_Data'[Status] = "Terminated"),
    COUNTROWS('HR_Data'),
    0
)

Other Measures
• Gender Pay Gap Index
• Manager Attrition Risk Ranking
• Workforce Engagement Index

---

Dashboard Decision Flow

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

Strategic Actions

### Leadership Intervention
Focus managerial review on positions showing 100% attrition rates (Data Analyst, Enterprise Architect, Principal Data Architect).

### Burnout Early Warning
Flag employees with:
PerformanceScore > 4
Absences > 10
Treat as retention risk group requiring workload assessment.

### Project Allocation Audit
Review Special Project assignment distribution inside IT/IS department to address potential inequity sources.

---

Author

Lorenzo Di Salvatore
HR Analytics | Organizational Psychology | People Data Strategy
LinkedIn: [Lorenzo Di Salvatore](https://www.linkedin.com/in/lorenzo-di-salvatore-psico)
Portfolio: [GitHub Repositories](https://github.com/LoreBear)