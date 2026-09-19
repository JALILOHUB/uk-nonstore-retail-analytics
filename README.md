# 📊 UK Non-Store Retail Analytics

> **Version:** 1.1 (Validated Analytical Release)  
> **Date:** September 2026  
> **Author:** Abdeljalil El Khyati  
> **License:** MIT (Code & Documentation) / CC BY 4.0 (Data)

## 📋 Project Overview

This repository contains a comprehensive, evidence-based analysis of the **UCI Online Retail dataset**.

The project transforms more than **541,000 raw transactions** into a structured analytical workflow covering data quality, validation, product performance, seasonality, customer behaviour, geographic concentration, and management-oriented business insights.

The project is designed as an **independent business case study analysis based on real-world transactional data from a UK non-store retailer**. It is not presented as paid client work.

The analytical workflow follows:

**DATA → EVIDENCE → INTERPRETATION → ACTION**

Every major analytical conclusion is separated into:
- **Fact:** directly measured or calculated from the dataset
- **Interpretation:** reasoned reading of an observed pattern
- **Hypothesis:** plausible explanation requiring further validation
- **Recommendation:** proposed business action

No causal claim is made from observational transactional data alone.

---

## 🎯 Key Deliverables

### Data Integrity & Validation
- Processed **541,909 raw transactions**
- Identified and removed **5,268 exact duplicates**
- Identified **135,080 missing CustomerID values (24.93%)**
- Isolated one extreme transaction containing **80,995 units**
- Separated **2,149 operational/non-product rows**
- Produced a final physical-product dataset of **522,728 rows**
- Passed row and revenue reconciliation with a **£0.00 revenue difference**

### Customer Analytics
- Analysed **4,338 known customers**
- Measured customer revenue concentration using Pareto analysis
- Calculated a validated **Gini coefficient of 0.716**
- Built an RFM segmentation framework with four behavioural groups
- Identified **1,188 Potential Loyalists / At Risk customers**
- Identified **885 Lost / Hibernating customers**

### Product & Seasonal Analytics
- Ranked physical products by observed revenue
- Identified the highest-revenue products
- Investigated the November 2011 revenue peak
- Compared November product performance with other observed months
- Identified products with unusually high November seasonal lift
- Identified a low-revenue product tail for potential catalog review

### Geographic Analytics
- Measured revenue distribution by country
- Measured Champion concentration by country
- Identified strong dependence on the United Kingdom market
- Highlighted smaller international markets for further investigation while accounting for small customer populations

### Executive Communication
- 10 publication-ready analytical charts
- 20 analytical CSV tables
- Executive presentation generated from the validated V1.1 outputs
- Portfolio-oriented documentation and decision tracking

---

## 🏢 Business Context

The dataset represents a UK-based registered non-store online retailer selling unique all-occasion gifts. The official UCI description states that many of the company's customers are wholesalers.

The dataset covers transactions from:
**1 December 2010 → 9 December 2011**

> ⚠️ **Important:** December 2011 contains only the first 9 days of the month and is therefore not treated as a normal full-month observation.

### Key Business Facts

| Metric | Value |
|---|---:|
| Raw Transactions | 541,909 |
| Valid Sales Rows | 524,878 |
| Valid Sales Revenue | £10,642,110.80 |
| Operational Revenue | £362,103.47 |
| Extreme Outlier Revenue | £168,469.60 |
| Clean Physical-Product Revenue | **£10,111,537.73** |
| Physical-Product Rows | 522,728 |
| Known Customers | 4,338 |
| Known-Customer Revenue | £8,887,208.89 |
| Known-Customer Revenue Share | 83.5% |
| Unknown CustomerID Revenue Share | 16.5% |
| November 2011 Revenue | £1,503,866.78 |

---

## 📁 Project Structure

```text
uk-nonstore-retail-analytics/
 │
 ├── 00_Project_Setup/
 │   ├── decision_log.md
 │   ├── export_project_docs.py
 │   ├── project_plan.md
 │   └── setup_project_structure.py
 │
 ├── 01_Raw_Data/
 │   └── online_retail_raw_541909_rows.csv
 │
 ├── 02_Working_Data/
 │   ├── .gitkeep
 │   ├── df_extreme_outliers.csv
 │   ├── df_physical_products_522728_rows.csv
 │   ├── df_sales_clean_excluding_extreme_outlier.csv
 │   ├── df_sales_valid_524878_rows.csv
 │   └── operational_sales.csv
 │
 ├── 03_Notebooks/
 │   └── Online_Retail_Analysis_Final_V1.1.ipynb
 │
 ├── 04_Outputs/
 │   ├── Charts/
 │   │   ├── 01_monthly_revenue_trend.png
 │   │   ├── 02_monthly_revenue_known_vs_unknown.png
 │   │   ├── 03_top_10_physical_products.png
 │   │   ├── 04_bottom_10_physical_products.png
 │   │   ├── 05_operational_items_revenue.png
 │   │   ├── 06_november_seasonal_lift.png
 │   │   ├── 07_november_vs_other_months_top10.png
 │   │   ├── 08_customer_revenue_concentration.png
 │   │   ├── 09_top_10_countries_revenue.png
 │   │   └── 10_top_10_champion_countries.png
 │   │
 │   ├── Reports/
 │   │   ├── UCI_Retail_Executive_Presentation.pdf
 │   │   └── UCI_Retail_Executive_Presentation.pptx
 │   │
 │   └── Tables/
 │       ├── bottom_10_physical_products_min_5_invoices.csv
 │       ├── champions_by_country.csv
 │       ├── country_revenue_metrics.csv
 │       ├── customer_revenue_concentration.csv
 │       ├── isolated_extreme_outliers.csv
 │       ├── monthly_performance.csv
 │       ├── monthly_revenue_known_vs_unknown.csv
 │       ├── operational_items_summary.csv
 │       ├── portfolio_kpi_summary.csv
 │       ├── rfm_customer_segments.csv
 │       ├── rfm_segment_metrics.csv
 │       ├── seasonal_product_comparison.csv
 │       ├── top_10_physical_products_all_time.csv
 │       ├── top_10_products_november_2011_physical.csv
 │       ├── top_10_products_other_months_physical.csv
 │       ├── top_products_november_2011_valid_sales.csv
 │       ├── top_products_overall_valid_sales.csv
 │       ├── top_seasonal_products_november_lift.csv
 │       ├── top_unknown_customer_products_november_2011.csv
 │       └── v1_1_reconciliation_summary.csv
 │
 ├── 05_Documentation/
 │   └── data_dictionary.md
 │
 ├── 06_Portfolio/
 │   └── final_summary.md
 │
 ├── .gitignore
 ├── CHANGELOG.md
 ├── LICENSE
 └── README.md
```

> **Note:** The executive presentation is generated from the final notebook outputs using the presentation-generation cell and saved under `04_Outputs/Reports/`.

---

## 🚀 Quick Start

### Prerequisites
* Python 3.12
* Jupyter Notebook or JupyterLab
* pandas, numpy, matplotlib, seaborn
* ucimlrepo
* python-pptx

### Installation
```bash
# Clone the repository
git clone https://github.com/JALILOHUB/uk-nonstore-retail-analytics.git
cd uk-nonstore-retail-analytics

# Install dependencies
pip install pandas numpy matplotlib seaborn ucimlrepo python-pptx

# Launch Jupyter
jupyter notebook
```

### Running the Analysis
1. Open: `03_Notebooks/Online_Retail_Analysis_Final_V1.1.ipynb`
2. Run the notebook sequentially (`Shift + Enter`).
3. Review the generated outputs under: `02_Working_Data/` and `04_Outputs/`
4. Run the final presentation-generation cell to create: `04_Outputs/Reports/UCI_Retail_Executive_Presentation.pptx`
5. Review the portfolio summary under: `06_Portfolio/final_summary.md`

---

# 📊 Key Findings

## 1. Data Quality & Revenue Reconciliation
The analysis begins with **541,909 raw transactions** and applies explicit data-quality decisions before calculating business metrics.

### Major quality decisions
* **135,080 missing CustomerID values (24.93%)** are retained for aggregate sales analysis and represented as `Unknown`.
* `Unknown` transactions are excluded from RFM and customer-concentration analysis because they cannot reliably support customer-level behaviour metrics.
* **5,268 exact duplicates** are removed.
* Non-positive sales and cancellation transactions are excluded from the defined valid-sales population.
* One extreme observation is isolated rather than silently deleted.
* Known operational/non-product descriptions are separated from physical merchandise analysis.

### Extreme Outlier
The isolated transaction is: `PAPER CRAFT , LITTLE BIRDIE`
* Quantity: **80,995**
* Unit Price: **£2.08**
* Revenue: **£168,469.60**

The observation is preserved for reconciliation while excluded from the core physical-product ranking.

### Final Reconciliation
| Measure | Value |
|---|---:|
| Valid Sales Rows | 524,878 |
| Outlier Rows | 1 |
| Operational Rows | 2,149 |
| Expected Physical Rows | 522,728 |
| Actual Physical Rows | 522,728 |
| **Row Difference** | **0** |
| Valid Sales Revenue | £10,642,110.80 |
| Outlier Revenue | £168,469.60 |
| Operational Revenue | £362,103.47 |
| Expected Physical Revenue | £10,111,537.73 |
| Actual Physical Revenue | £10,111,537.73 |
| **Revenue Difference** | **£0.00** |

**✅ RECONCILIATION PASSED:** The transformation from valid sales to physical-product sales is internally consistent.

---

## 2. Seasonal Revenue Drivers
### November 2011 Revenue Peak
November 2011 generated **£1,503,866.78**, the highest observed monthly revenue in the dataset. (Average monthly revenue is ~£840K when incomplete December 2011 is excluded).

### Highest Seasonal Lift
| Product | November Revenue | Seasonal Lift |
|---|---:|---:|
| RABBIT NIGHT LIGHT | £34,478.40 | £32,409.02 |
| PAPER CHAIN KIT 50'S CHRISTMAS | £28,955.54 | £26,314.42 |
| POPCORN HOLDER | £14,188.80 | £12,854.61 |
| PAPER CHAIN KIT VINTAGE CHRISTMAS | £12,929.74 | £11,370.33 |
| HOT WATER BOTTLE KEEP CALM | £11,760.07 | £10,579.70 |

> The observed data identifies the pattern but does not establish an external causal explanation for the November increase.

---

## 3. Customer Revenue Concentration
Customer-level concentration analysis is based on the **4,338 known customers**.
* Known-customer revenue: **£8,887,208.89**
* Approximately **26% of known customers generate 80% of known-customer revenue**
* **Gini coefficient: 0.716**

The Gini result indicates a substantial concentration of revenue among known customers, identifying it as an important management-monitoring area.

---

## 4. Customer Segmentation — RFM
| Segment | Customers | Avg. Monetary | Avg. Frequency | Avg. Recency |
|---|---:|---:|---:|---:|
| **Champions** | 1,243 | £5,465 | 10.0 | 18 days |
| **Loyal Customers** | 1,022 | £1,176 | 3.2 | 55 days |
| **Potential Loyalists / At Risk** | 1,188 | £580 | 1.6 | 102 days |
| **Lost / Hibernating** | 885 | £228 | 1.1 | 223 days |

Potential Loyalists / At Risk plus Lost / Hibernating represent **47.8% of known customers**. Their historical observed revenue is approximately **£689K**.
> ⚠️ This £689K figure is a **historical revenue baseline**, not a forecast of guaranteed recoverable revenue.

---

## 5. Geographic Concentration Risk
### United Kingdom
* **84.6% of total valid-sales revenue**
* **1,119 of 1,243 Champions** (~90.0% of the Champion segment)

### Selected Smaller Markets
* **EIRE:** £283K from **3** known customers
* **Netherlands:** £285K from 9 known customers
* **Australia:** £138K from 9 known customers (AOV: £2,429)

---

## 6. Product Portfolio Analysis
* **Highest-Revenue Physical Product:** REGENCY CAKESTAND 3 TIER (£174,156.54 across 1,988 invoices).
* **Top 3 Physical Products:** Generated £379,838.49, representing **3.8% of clean physical-product revenue**.
* **Low-Revenue Product Tail:** Identified as candidates for catalog review. They are not classified as confirmed dead stock due to the absence of inventory/cost data in the dataset.

---

## 7. Operational Revenue
Descriptions representing operational/non-product transactions (`DOTCOM POSTAGE`, `POSTAGE`, `Manual`, `BANK CHARGES`) are separated from physical merchandise analysis.
* **Validated Operational Revenue:** £362,103.47
* **Operational Rows:** 2,149

---

## 8. Unknown CustomerID Activity
| Customer Identifier Status | Revenue | Share |
|---|---:|---:|
| Known CustomerID | £8,887,208.89 | 83.5% |
| Unknown CustomerID | £1,754,901.91 | 16.5% |

The project deliberately uses **Unknown CustomerID** rather than assuming these transactions represent guest checkouts, as the dataset lacks evidence to determine the exact reason for missing identifiers.

---

# 🎯 Management Implications
1. **Customer Retention:** Test targeted retention strategies for the 1,188 Potential Loyalists / At Risk customers.
2. **Seasonal Planning:** Distinguish between products with strong recurring performance and those with strong November-specific performance.
3. **Geographic Concentration:** Keep UK concentration visible in management reporting; investigate smaller markets cautiously.
4. **Data Architecture:** Maintain clear separation between Product Revenue and Operational Revenue in BI dashboards.

---

# 🧪 Recommended Next Analyses
1. Customer Lifetime Value (CLV)
2. Cohort Retention Analysis
3. Market Basket Analysis
4. Demand and Pricing Analysis
5. Unknown CustomerID Investigation
6. Profitability & Inventory Analysis (pending external cost data)

---

# 🛠️ Methodology & Technology Stack

## Analytical Methodology
DATA → DATA ACQUISITION → INITIAL INSPECTION → DATA QUALITY ASSESSMENT → QUALITY DECISIONS → CLEANING & PREPARATION → VALIDATION → EXPLORATORY DATA ANALYSIS → QUESTION DISCOVERY → TARGETED ANALYSIS → FINDINGS → RECOMMENDATIONS → FINAL VALIDATION → PORTFOLIO OUTPUTS

## Technology Stack
| Technology | Purpose |
|---|---|
| **Python 3.12** | Core analysis and automation |
| **pandas / NumPy** | Data cleaning, transformation, and numerical calculations |
| **Matplotlib / Seaborn** | Data and statistical visualization |
| **Jupyter Notebook** | Reproducible analysis |
| **UCI ML Repository API** | Dataset acquisition |
| **python-pptx** | Executive presentation generation |

---

# 🔍 Data Quality Decisions
| Issue | Decision |
|---|---|
| Missing CustomerID | Retain as `Unknown` for aggregate sales analysis; Exclude from RFM/Pareto |
| Exact duplicates | Remove |
| Cancellations / Non-positive values | Exclude from valid-sales population |
| Extreme high-quantity observation | Isolate |
| Operational/non-product items | Separate from physical-product analysis |
| December 2011 | Treat as incomplete observation period |

---

# ⚠️ Analytical Limitations
1. **Incomplete December 2011:** Ends on 9 December; not a full month.
2. **Missing CustomerID:** 24.93% of raw transactions lack identifiers, limiting customer-level behavioral analysis for that subset.
3. **No Cost/Inventory Data:** ROI, profitability, storage costs, and confirmed dead stock cannot be calculated.
4. **Observational Data:** Observed relationships do not establish causality.
5. **RFM Limitations:** Segments describe observed behavior, not validated churn predictions.
6. **Small International Samples:** High average revenue in small markets requires cautious interpretation.
7. **B2B Interpretation Boundary:** High-quantity indicators are noted, but not treated as absolute proof of B2B structure without CRM data.

---

# 📈 Portfolio Metrics
| KPI | Result |
|---|---:|
| Raw transactions | 541,909 |
| Valid sales rows | 524,878 |
| Physical-product rows | 522,728 |
| Valid sales revenue | £10,642,110.80 |
| Clean physical-product revenue | **£10,111,537.73** |
| Operational revenue | £362,103.47 |
| Extreme outlier revenue | £168,469.60 |
| Known customers | 4,338 |
| Known-customer revenue | £8,887,208.89 |
| Unknown CustomerID revenue share | 16.5% |
| Pareto customer share | 26% |
| Pareto revenue share | 80% |
| Gini coefficient | **0.716** |
| November 2011 revenue | £1,503,866.78 |
| Champions | 1,243 |
| Loyal Customers | 1,022 |
| Potential Loyalists / At Risk | 1,188 |
| Lost / Hibernating | 885 |
| UK revenue share | 84.6% |
| UK Champion share | 90.0% |
| Top 3 physical-product revenue share | 3.8% |
| Row reconciliation difference | **0** |
| Revenue reconciliation difference | **£0.00** |

---

# 📈 Project Evolution
### v1.0 — Initial Portfolio Release
Initial analytical release containing data cleaning, product analysis, customer segmentation, geographic analysis, visualizations, and initial documentation.

### v1.1 — Validated Analytical Release (Current)
* Corrected customer concentration calculation and validated **Gini coefficient = 0.716**.
* Formalized revenue reconciliation (£0.00 difference).
* Corrected physical-product revenue to **£10,111,537.73**.
* Separated operational revenue from merchandise revenue.
* Refined handling of missing CustomerID values and tightened interpretation of B2B indicators.
* Changed the £689K retention figure into a historical baseline rather than a recovery forecast.
* Clarified limitations around inventory and profitability.

### Future Development
CLV, Cohort Retention, Market Basket Analysis, advanced demand analysis, and potential cloud-based data engineering architecture.

---

# 📚 Documentation

* **Main Analysis:** `03_Notebooks/Online_Retail_Analysis_Final_V1.1.ipynb`
* **Data Dictionary:** `05_Documentation/data_dictionary.md`
* **Decision Log:** `00_Project_Setup/decision_log.md`
* **Project Plan:** `00_Project_Setup/project_plan.md`
* **Portfolio Summary:** `06_Portfolio/final_summary.md`
* **Executive Presentation (PPTX):** `04_Outputs/Reports/UCI_Retail_Executive_Presentation.pptx`
* **Executive Presentation (PDF):** `04_Outputs/Reports/UCI_Retail_Executive_Presentation.pdf`

---

# 👤 Author
**Abdeljalil El Khyati**  
Lead Data Analyst  
September 2026

---

# 📋 Portfolio Disclosure
This is an **independent portfolio project** based on a publicly available dataset from the UCI Machine Learning Repository.
* **Dataset:** UCI Online Retail (ID: 352)
* **Project Type:** Independent portfolio analysis simulating a real-world analytical engagement.
* **Purpose:** Demonstrate data analysis, data-quality management, business reasoning, visualization, documentation, and executive communication skills.

The project is **not presented as paid client work or as professional commercial experience**.

---

## 📄 License
The analytical code and documentation in this repository are licensed under the **MIT License**.  
The underlying dataset is sourced from the UCI Machine Learning Repository and is subject to the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.  
See [LICENSE](LICENSE) for details.

---
**Last updated:** September 2026
