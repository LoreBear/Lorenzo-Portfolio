# Inclusive Leadership Workshop Analytics - Real Data Version

## Abstract
This project analyzes HR employee data to measure the effectiveness of inclusive leadership training programs through leadership competency proxies. Analysis of 3,400 employee records reveals overall leadership competency of 2.97/5.0, with Development & Growth Mindset as the lowest competency (2.60/5.0) and Experience & Role Stability as the highest (3.13/5.0). Gender analysis shows minimal disparities in leadership competencies.

## Research Question
What is the current state of inclusive leadership competencies in the workforce, and which areas show the greatest need for development based on analysis of HR employee data?

## Dataset & Methods
- **Source**: HR Employee Dataset (Kaggle)
- **N**: 3,400 employee records
- **Variables**: Job satisfaction, performance rating, work-life balance, training hours, years at company, years in current role, attrition risk
- **Methods**: Leadership competency proxy creation from HR metrics, demographic analysis by gender and department, correlation analysis between competencies and HR outcomes

## Key Findings
- Total employees analyzed: 3,400
- Overall leadership competency: 2.97/5.0
- Gender distribution: 24.6% female, 24.4% male, 25.7% non-binary, 25.3% prefer not to say
- Leadership competency ranking (highest to lowest):
  1. Experience & Role Stability: 3.13/5.0
  2. Self-Awareness & Engagement: 3.04/5.0
  3. Decision-Making & Results Orientation: 3.04/5.0
  4. Psychological Safety & Well-being: 3.00/5.0
  5. Retention & Psychological Safety: 2.97/5.0
  6. Development & Growth Mindset: 2.60/5.0
- Gender competency disparities (female vs male):
  - Self-Awareness & Engagement: Females 0.04 points lower
  - Decision-Making & Results Orientation: Females 0.06 points higher
  - Psychological Safety & Well-being: Females 0.05 points higher
  - Development & Growth Mindset: Females 0.02 points higher
  - Experience & Role Stability: Females 0.01 points higher
  - Retention & Psychological Safety: Females 0.05 points lower
- Strongest predictor of retention: Retention & Psychological Safety (1.000 correlation)
- Development gap (Experience & Role Stability minus Development & Growth Mindset): 0.53 points

## Organizational Intervention Framework
Based on findings, three targeted interventions:

1. **Development & Growth Mindset enhancement programs** — Implement targeted training to address the lowest leadership competency (2.60/5.0), focusing on learning orientation, challenge-seeking, and resilience
   *(Reference: Dweck, C. S. (2006). *Mindset: The new psychology of success.* Random House.)*

2. **Experience & Role Stability leveraging initiatives** — Create mentorship and knowledge transfer programs to utilize the highest leadership competency (3.13/5.0) for organizational benefit
   *(Reference: Allen, T. D., & Eby, L. T. (2007). *Relationships between informal mentoring, satisfaction, and organizational commitment.* Journal of Vocational Behavior, 70(3), 447-463.)*

3. **Retention-focused psychological safety interventions** — Develop programs targeting the strongest retention predictor (Retention & Psychological Safety: 1.000 correlation) through inclusive leadership practices
   *(Reference: Edmondson, A. C. (1999). *Psychological safety and learning behavior in work teams.* Administrative Science Quarterly, 44(2), 350-383.)*

## References
- Dweck, C. S. (2006). *Mindset: The new psychology of success.* Random House.
- Allen, T. D., & Eby, L. T. (2007). *Relationships between informal mentoring, satisfaction, and organizational commitment.* Journal of Vocational Behavior, 70(3), 447-463.
- Edmondson, A. C. (1999). *Psychological safety and learning behavior in work teams.* Administrative Science Quarterly, 44(2), 350-383.

## Technical Implementation
### Requirements
pip install -r requirements.txt

### Run Analysis
py workshop_analysis_real_data.py

### Output
Charts saved to: charts_real/
Summary report saved: workshop_real_data_summary.txt
Leadership competency proxies and demographic analysis printed to terminal