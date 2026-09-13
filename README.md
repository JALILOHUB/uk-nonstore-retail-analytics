# 📊 UCI Online Retail — Business Data Analysis

> **Version:** 1.0 (Initial Portfolio Release)  
> **Date:** September 2026  
> **Author:** Abdeljalil El Khyati  
> **License:** MIT

## 📋 Project Overview
This repository contains a comprehensive, evidence-based data analysis of a UK-based non-store online retailer. Transforming over 541,000 raw transactions into actionable business intelligence, this project simulates a real-world freelance data analytics engagement.

### 🎯 Key Deliverables:
- **Data Integrity:** Rigorous cleaning pipeline isolating outliers and operational fees to reveal true merchandise revenue (£10.28M).
- **Customer Segmentation:** RFM analysis revealing a healthy Pareto (26/80) distribution and identifying a massive retention opportunity (47.8% of customers are At-Risk/Lost).
- **Strategic Risk Identification:** Uncovered a "dual concentration crisis" with 84.6% of revenue and 90% of top-tier "Champions" concentrated solely in the UK market.
- **Actionable Recommendations:** Prioritized 30-day, 90-day, and long-term strategies for inventory planning, international diversification, and customer win-back campaigns.

---

## 🏢 Business Context
The dataset represents 13 months of transactions (December 2010 – December 2011) from a UK-based online retailer specializing in unique all-occasion gifts, with a significant wholesale (B2B) customer base.

**Key Business Facts:**
- **Total Revenue:** £10,642,110.80 (valid transactions)
- **Valid Transactions:** 524,878 (after data quality processing)
- **Known Customers:** 4,338 (generating 83.5% of revenue)
- **Unknown/Guest Customers:** Generating 16.5% of revenue
- **Timeframe:** Dec 2010 – Dec 2011 (December 2011 is incomplete — 9 days only)

---

## 📁 Project Structure
```text
UCI_Online_Retail_Case_Study/
 │
 ├── 00_Project_Setup/
 │   ├── decision_log.md          # Decision tracking and rationale
 │   ├── project_plan.md          # Project planning and timeline
 │   └── setup_project_structure.py  # Folder structure setup script
 │
 ├── 01_Raw_Data/                 # Raw data storage (if applicable)
 │
 ├── 02_Working_Data/             # Intermediate processed data
 │
 ├── 03_Notebooks/
 │   └── 01_Online_Retail_Analysis.ipynb  # Main analysis notebook
 │
 ├── 04_Outputs/
 │   ├── Charts/                  # Generated visualizations
 │   ├── Reports/                 # Generated reports
 │   └── Tables/                  # Generated data tables
 │
 ├── 05_Documentation/
 │   ├── data_dictionary.md       # Data dictionary and variable descriptions
 │   ├── Executive Summary UCI Online Retail Business Analysis (En-Fr-Ar).docx
 │   ├── UCI_Retail_Executive_Presentation.pdf
 │   └── UCI_Retail_Executive_Presentation.pptx
 │
 ├── 06_Portfolio/
 │   └── final_summary.md         # Portfolio summary document
 │
 └── README.md                    # This file

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Required libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

### Installation
```bash
# Clone the repository
git clone [repository-url]
cd UCI_Online_Retail_Case_Study

# Install dependencies (if needed)
pip install pandas numpy matplotlib seaborn

# Launch Jupyter
jupyter notebook
```

### Running the Analysis
1. Open `03_Notebooks/01_Online_Retail_Analysis.ipynb`
2. Run all cells sequentially (`Shift + Enter`)
3. View outputs in `04_Outputs/` directory
4. Review executive presentation in `05_Documentation/`

---

## 📊 Key Findings

### 1. Seasonal Revenue Drivers
- November 2011 generated £1.5M (2x monthly average).
- **Dual-driver phenomenon:**
  - **Driver A (Core Amplification):** `RABBIT NIGHT LIGHT` generated £34,478.40 in November alone (48.5% of annual revenue).
  - **Driver B (Seasonal Emergence):** Christmas-themed products contributed £50K+ in incremental revenue.
- 40% overlap between November's Top 10 and annual Top 10 confirms a hybrid model.

### 2. Customer Concentration (Pareto 26/80)
- Top 26% of customers generate 80% of revenue.
- **Gini Coefficient = 0.142** (surprisingly low for B2B).
- Indicates a broad base of ~1,128 high-value wholesale customers, not whale-dependent.
- Healthy concentration — losing one top client would be painful but not catastrophic.

### 3. Customer Segmentation (RFM Analysis)
| Segment | Share | Avg Revenue | Avg Frequency | Avg Recency |
| :--- | :--- | :--- | :--- | :--- |
| **Champions** | 28.6% (1,243) | £5,465 | 10.0 orders | 18 days |
| **Loyal Customers** | 23.6% (1,022) | £1,176 | 3.2 orders | 55 days |
| **At Risk** | 27.4% (1,188) | £580 | 1.6 orders | 102 days |
| **Lost/Hibernating** | 20.4% (885) | £228 | 1.1 orders | 223 days |
> **Critical Insight:** 47.8% of the customer base is At Risk or Lost — representing a massive retention opportunity.

### 4. Geographic Concentration Risk
- **United Kingdom:** 84.6% of revenue (£9M) AND 90% of Champions (1,119/1,243).
- **Dual concentration crisis:** Dependency on the UK market AND the UK's best customers.
- **High-value niche markets:**
  - **EIRE (Ireland):** 4 customers → £283K (£70K/customer avg)
  - **Netherlands:** 9 customers → £285K (£31K/customer avg)
  - **Australia:** Highest AOV (£2,429) with only 9 customers

---

## 🎯 Strategic Recommendations

### 🔴 HIGH PRIORITY (30 Days)
- **Protect UK Champions:** VIP loyalty program for 1,119 UK Champions + dedicated account managers.
- **Win-Back Campaign:** Email campaign for 1,188 At Risk customers (15% discount) → Expected impact: ~£690K.
- **Dead Stock Management:** Discontinue/bundle Bottom 10 products (<£12/year each).

### 🟡 MEDIUM PRIORITY (90 Days)
- **Dual-Track Seasonal Inventory:** Pre-build `RABBIT NIGHT LIGHT` by early Oct; Christmas SKUs by mid-Sept.
- **International Diversification:** Target France/Germany; assign managers to EIRE/NL whale clients.
- **Revenue Separation:** Separate Product Revenue (£10.28M) from Operational Revenue (£362K) in dashboards.

### 🟢 LONG-TERM (6-12 Months)
- **Guest-to-Registered Conversion:** Post-purchase email flows for 15-23% Unknown customer revenue.
- **Upsell Loyal Customers:** Volume-based bundle discounts for 1,022 Loyal Customers → Champions tier.
- **Target:** Reduce UK revenue share from 84.6% to <70% within 2 years.

---

## 🛠️ Methodology & Technology Stack

### Data Quality Decisions (Evidence-Based)
- **Missing CustomerID (24.93%):** Labeled "Unknown" for sales tracking; strictly excluded from RFM/Pareto analysis.
- **Exact Duplicates (5,268 rows):** Removed to prevent artificial inflation.
- **Extreme Outlier (1 row):** `PAPER CRAFT, LITTLE BIRDIE` (80,995 units, £168,469.60) — isolated, not deleted.
- **Operational Items (£362,268.47):** POSTAGE, Manual, Bank Charges excluded from product rankings.

### Analytical Framework
- Evidence → Decision → Action → Validation
- No assumptions without data support; external benchmarks avoided; internal comparisons used.
- **Techniques Applied:** Descriptive Statistics, Time Series Analysis, Pareto Analysis, RFM Segmentation, Geographic Analysis, Product Analysis.

### Technology Stack
- **Language:** Python 3.12
- **Data Processing:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`
- **Environment:** Jupyter Notebook
- **Data Source:** UCI Machine Learning Repository (Dataset ID: 352)

---

## 📈 Project Evolution

### Version History
- **v1.0 — Initial Portfolio Release (September 2026)**
  - Complete analytical workflow from raw data to executive recommendations.
  - Evidence-based decision making throughout.
  - Professional documentation and visualization.
- **Planned v1.1 — Data & Logic Corrections**
  - Refine outlier handling logic.
  - Improve revenue reconciliation.
  - Enhance visualization consistency.
- **Planned v2.0 — Professionalization & Optimization**
  - Performance optimization and code refactoring.
  - Advanced analytics (CLV, Cohort Analysis, Market Basket).

---

## 📚 Documentation
- **Main Analysis:** `03_Notebooks/01_Online_Retail_Analysis.ipynb`
- **Executive Presentation:** `05_Documentation/UCI_Retail_Executive_Presentation.pdf`
- **Data Dictionary:** `05_Documentation/data_dictionary.md`
- **Decision Log:** `00_Project_Setup/decision_log.md`
- **Project Plan:** `00_Project_Setup/project_plan.md`

---

## 🎓 Learning Objectives
This project demonstrates:
- Professional data analysis workflow.
- Evidence-based decision making.
- Business problem translation to analytical solutions.
- Stakeholder communication through visualization.
- Critical thinking and analytical rigor.
- Portfolio-ready documentation.

---

## 📄 License
This project is licensed under the MIT License — see the LICENSE file for details.

## 👤 Author
**Abdeljalil El Khyati**  
Lead Data Analyst  
September 2026

## 🙏 Acknowledgments
- **Dataset:** UCI Machine Learning Repository — Online Retail (ID: 352)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)
- **Original Paper:** "Data mining for the online retail industry: A case study of RFM model-based customer segmentation using data mining" by Daqing Chen, Sai Laing Sain, Kun Guo (2012)

## 📞 Contact
For questions or collaboration opportunities, please reach out through the repository issues or contact the author directly.

---
*© 2026 Abdeljalil El Khyati. All rights reserved.*