"""
Project Structure Setup Script
Creates the complete folder structure for UCI Online Retail Analysis project.
"""

import os
import json

# Project root directory
base_dir = r"H:\UCI_Online_Retail_Case_Study"

# Define folder structure
folders = [
    "00_Project_Setup",
    "01_Raw_Data",
    "02_Working_Data",
    "03_Notebooks",
    "04_Outputs/Charts",
    "04_Outputs/Reports",
    "04_Outputs/Tables",
    "05_Documentation",
    "06_Portfolio"
]

# Create folders
for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    os.makedirs(folder_path, exist_ok=True)
    print(f"✅ Created: {folder}")

# Create .gitkeep files for empty folders (to keep them in Git)
empty_folders = [
    "01_Raw_Data",
    "02_Working_Data",
    "04_Outputs/Charts",
    "04_Outputs/Tables"
]

for folder in empty_folders:
    gitkeep_path = os.path.join(base_dir, folder, ".gitkeep")
    if not os.path.exists(gitkeep_path):
        with open(gitkeep_path, 'w') as f:
            pass  # Empty file
        print(f"✅ Created .gitkeep in: {folder}")

# Create initial file contents
files_content = {
    os.path.join(base_dir, "00_Project_Setup", "decision_log.md"): """# Decision Log

| Date | Decision | Why | Evidence | Impact |
|------|----------|-----|----------|--------|
| 2026-09-12 | Isolated extreme outlier (PAPER CRAFT, LITTLE BIRDIE) | 80,995 units in single invoice would distort statistics | Single invoice with 80,995 units (£168,469.60) | Preserved total revenue reconciliation while preventing statistical distortion |
| 2026-09-12 | Excluded operational items from product rankings | POSTAGE, Manual, Bank Charges are service fees, not merchandise | £362,268.47 in operational items | Accurate product performance analysis |
| 2026-09-12 | Labeled missing CustomerID as "Unknown" | 24.93% missing CustomerID likely B2C guest checkouts | 135,080 rows with missing CustomerID | Preserved revenue data while excluding from RFM analysis |
| 2026-09-12 | Removed exact duplicates | 5,268 exact duplicate rows | 5,268 duplicate rows | Prevented artificial inflation of metrics |
""",
    
    os.path.join(base_dir, "00_Project_Setup", "project_plan.md"): """# Project Plan — UCI Online Retail Analysis

## Completed Phases ✅

### Phase 1: Environment Setup & Data Acquisition
- Set up project structure
- Imported required libraries (pandas, numpy, matplotlib, seaborn)
- Fetched data from UCI Repository (ID: 352)
- Merged missing columns (InvoiceNo, StockCode) from 'ids' key

### Phase 2: Initial Inspection
- Examined dataset structure (541,909 rows, 8 columns)
- Identified data types and potential issues
- Documented initial observations

### Phase 3: Data Quality Assessment
- Missing values analysis (CustomerID: 24.93%, Description: 0.27%)
- Duplicate detection (5,268 rows)
- Outlier detection (extreme outlier: 80,995 units)
- Operational items identification

### Phase 4: Cleaning & Preparation
- Removed duplicates
- Isolated extreme outlier
- Excluded operational items from product analysis
- Labeled missing CustomerID as "Unknown"
- Created clean dataset: 522,728 physical product transactions

### Phase 5: Baseline KPIs
- Total Revenue: £10,642,110.80
- Valid Transactions: 524,878
- Known Customers: 4,338 (83.5% of revenue)
- AOV: £533.17

### Phase 6: Seasonal Analysis
- November 2011 peak: £1.5M (2x monthly average)
- Dual-driver phenomenon identified
- 40% overlap between November Top 10 and annual Top 10

### Phase 7: Product Analysis
- Top performers identified
- B2B wholesale patterns confirmed
- Dead stock identified (Bottom 10 products)

### Phase 8: Customer Analysis (Pareto & RFM)
- Pareto 26/80 validated
- Gini Coefficient: 0.142
- 4 behavioral segments: Champions, Loyal, At Risk, Lost

### Phase 9: Geographic Analysis
- UK: 84.6% of revenue, 90% of Champions
- Dual concentration crisis identified
- High-value niche markets identified (EIRE, Netherlands, Australia)

## Next Steps 🔜

### Phase 10: Customer Lifetime Value (CLV)
- Calculate lifetime value of Champions
- Compare with acquisition cost

### Phase 11: Cohort Retention Analysis
- Track retention rates by acquisition month
- Identify churn patterns

### Phase 12: Market Basket Analysis
- Identify frequently purchased together products
- Cross-selling opportunities

### Phase 13: Professionalization & Optimization
- Code refactoring
- Performance optimization
- Enhanced documentation
""",
    
    os.path.join(base_dir, "05_Documentation", "data_dictionary.md"): """# Data Dictionary — UCI Online Retail

## Dataset Overview
- **Source:** UCI Machine Learning Repository (ID: 352)
- **Timeframe:** December 2010 – December 2011
- **Total Records:** 541,909 transactions
- **Clean Records:** 522,728 physical product transactions

## Variables

### InvoiceNo
- **Type:** String (Categorical)
- **Description:** 6-digit integral number uniquely assigned to each transaction
- **Notes:** Starts with 'C' indicates cancellation
- **Missing Values:** 0%

### StockCode
- **Type:** String (Categorical)
- **Description:** 5-digit integral number uniquely assigned to each distinct product
- **Missing Values:** 0%

### Description
- **Type:** String (Categorical)
- **Description:** Product (item) name
- **Missing Values:** 0.27% (1,454 records)
- **Notes:** Some descriptions may be generic or operational (e.g., "POSTAGE", "Manual")

### Quantity
- **Type:** Integer
- **Description:** Quantities of each product (item) per transaction
- **Range:** -80,995 to 80,995
- **Notes:** Negative values indicate returns/cancellations; extreme positive values indicate wholesale orders

### InvoiceDate
- **Type:** DateTime
- **Description:** Day and time when each transaction was generated
- **Format:** DD/MM/YYYY HH:MM
- **Missing Values:** 0%

### UnitPrice
- **Type:** Float (Continuous)
- **Description:** Product price per unit in sterling (£)
- **Range:** -11,062.06 to 38,970.00
- **Notes:** Negative values indicate refunds/adjustments; extreme values may be operational adjustments

### CustomerID
- **Type:** Float (Categorical)
- **Description:** 5-digit integral number uniquely assigned to each customer
- **Missing Values:** 24.93% (135,080 records)
- **Notes:** Missing values likely represent B2C guest checkouts; stored as float due to NaN values

### Country
- **Type:** String (Categorical)
- **Description:** Name of the country where each customer resides
- **Unique Values:** 38 countries
- **Missing Values:** 0%

## Derived Variables

### Revenue
- **Type:** Float
- **Description:** Calculated as Quantity × UnitPrice
- **Notes:** Calculated only for valid transactions (excludes cancellations, duplicates, operational items)

### Month
- **Type:** Period
- **Description:** Extracted from InvoiceDate for monthly aggregation
- **Format:** YYYY-MM

## Data Quality Notes
- Extreme outlier isolated: PAPER CRAFT, LITTLE BIRDIE (80,995 units)
- Operational items excluded from product analysis: POSTAGE, Manual, Bank Charges
- Missing CustomerID labeled as "Unknown" for sales tracking
""",
    
    os.path.join(base_dir, "06_Portfolio", "final_summary.md"): """# Final Portfolio Summary — UCI Online Retail Analysis

## Project Overview
Comprehensive analysis of 541,909 transactions from a UK-based online retailer (December 2010 – December 2011), transforming raw transactional data into evidence-based, actionable business insights.

## Key Achievements
- **Data Quality:** Cleaned and validated 522,728 physical product transactions representing £10.28M in true merchandise revenue
- **Seasonal Insights:** Identified dual-driver phenomenon in November 2011 (£1.5M revenue, 2x monthly average)
- **Customer Segmentation:** Validated Pareto 26/80 rule with Gini Coefficient of 0.142
- **Risk Identification:** Uncovered dual concentration crisis (84.6% revenue + 90% Champions in UK)
- **Strategic Recommendations:** 8 prioritized recommendations with expected impact of ~£690K from win-back campaigns

## Technical Skills Demonstrated
- **Data Processing:** pandas, numpy for data manipulation and cleaning
- **Visualization:** matplotlib, seaborn for data visualization
- **Statistical Analysis:** Pareto analysis, Gini coefficient calculation, RFM segmentation
- **Business Acumen:** Translated data insights into actionable business recommendations
- **Professional Documentation:** Evidence-based decision making, comprehensive documentation

## Business Impact
- **Immediate Opportunity:** Win-back campaign for 1,188 At Risk customers could unlock ~£690K annually
- **Strategic Risk:** Dual concentration crisis requires international diversification (target: <70% UK revenue within 2 years)
- **Operational Efficiency:** Dual-track seasonal inventory planning to prevent November stockouts

## Lessons Learned
- Evidence-based decision making prevents analytical bias
- Data quality decisions must balance statistical rigor with business reality
- Professional documentation is as important as the analysis itself
- Business context is essential for meaningful insights

## Next Steps
1. Customer Lifetime Value (CLV) analysis
2. Cohort retention analysis
3. Market basket analysis for cross-selling opportunities
4. Pricing elasticity analysis
5. Channel attribution for Unknown customers

---

**Prepared by:** Abdeljalil El Khyati  
**Date:** September 2026  
**Tools:** Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook
"""
}

# Create files with initial content
for file_path, content in files_content.items():
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✅ Created: {os.path.basename(file_path)}")

# Create empty Jupyter Notebook structure
notebook_path = os.path.join(base_dir, "03_Notebooks", "01_Online_Retail_Analysis.ipynb")
notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# UCI Online Retail — Business Data Analysis\n",
                "\n",
                "**Lead Data Analyst:** Abdeljalil El Khyati  \n",
                "**Date:** September 2026  \n",
                "\n",
                "## Project Objective\n",
                "Analyze 541,909 transactions from a UK-based online retailer to deliver evidence-based, actionable business insights.\n",
                "\n",
                "## Methodology\n",
                "**Evidence → Decision → Action → Validation**\n",
                "\n",
                "Every finding is supported by quantitative evidence. No assumptions without data support."
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3 (ipykernel)",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.12.7"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(notebook_path, 'w', encoding='utf-8') as f:
    json.dump(notebook_content, f, indent=2)
print("✅ Created: 01_Online_Retail_Analysis.ipynb (template)")

print("\n" + "="*50)
print("✅ Project structure setup complete!")
print("="*50)