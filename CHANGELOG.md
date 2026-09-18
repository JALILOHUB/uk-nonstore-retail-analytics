# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2026-09-18

### Changed
- Promoted the project to **Validated Analytical Release v1.1**.
- Updated the main notebook path to: `03_Notebooks/Online_Retail_Analysis_Final_V1.1.ipynb`
- Reorganised the repository into dedicated setup, raw-data, working-data, notebook, output, documentation, and portfolio directories.
- Updated the README, data dictionary, decision log, project plan, and portfolio summary to reflect the validated V1.1 analytical results.
- Updated the executive reporting to use the validated V1.1 outputs.
- Added the final executive presentation in both `.pptx` and `.pdf` formats.

### Corrected
- Corrected the customer revenue concentration analysis.
- Validated the **Gini coefficient at 0.716**.
- Corrected clean physical-product revenue to **£10,111,537.73**.
- Corrected operational revenue to **£362,103.47**.
- Formalised row and revenue reconciliation with a **£0.00 revenue difference**.
- Refined the treatment of missing `CustomerID` values and replaced unsupported "Guest Customer" interpretations with `Unknown CustomerID`.
- Refined the interpretation of high-quantity transactions as **bulk-purchasing indicators**, not definitive proof of B2B transactions.
- Reframed the approximately **£689K** RFM revenue figure as a historical observed baseline rather than a guaranteed recoverable revenue estimate.
- Replaced unsupported "Dead Stock" conclusions with **low-revenue product tail / catalog-review candidates**.
- Clarified that December 2011 is an incomplete observation period.
- Clarified the distinction between physical-product revenue and operational/non-product revenue.

### Analytical Results
- Raw transactions: **541,909**
- Valid sales rows: **524,878**
- Physical-product rows: **522,728**
- Valid sales revenue: **£10,642,110.80**
- Clean physical-product revenue: **£10,111,537.73**
- Operational revenue: **£362,103.47**
- Extreme outlier revenue: **£168,469.60**
- Known customers: **4,338**
- Known-customer revenue share: **83.5%**
- Unknown `CustomerID` revenue share: **16.5%**
- Customer concentration: approximately **26% of known customers generating 80% of known-customer revenue**
- Gini coefficient: **0.716**
- November 2011 revenue: **£1,503,866.78**
- Champions: **1,243**
- Loyal Customers: **1,022**
- Potential Loyalists / At Risk: **1,188**
- Lost / Hibernating: **885**
- UK revenue share: **84.6%**
- UK Champion share: approximately **90.0%**

### Outputs
- Added **10 analytical charts** under `04_Outputs/Charts/`.
- Added **20 analytical CSV tables** under `04_Outputs/Tables/`.
- Added `UCI_Retail_Executive_Presentation.pptx`.
- Added `UCI_Retail_Executive_Presentation.pdf`.

### Documentation
- Updated `README.md`.
- Updated `05_Documentation/data_dictionary.md`.
- Updated `06_Portfolio/final_summary.md`.
- Maintained project decision tracking and project planning documentation.

---

## [1.0.0] - 2026-09-12

### Added
- Initial portfolio release of the UCI Online Retail analysis.
- Initial end-to-end Jupyter Notebook workflow.
- Initial business analysis covering: Data cleaning, Product analysis, Customer segmentation, Geographic analysis, Seasonality, Visualization, and Initial business recommendations.
- Initial README, data dictionary, decision log, and project plan.
- Initial executive presentation, analytical output tables, and charts.

### Notes
This release was later superseded by **v1.1.0** after validation identified issues in customer concentration metrics, revenue reconciliation, revenue classification, and several interpretation boundaries.

---

## [Unreleased]

### Planned for v2.0
- Customer Lifetime Value (CLV)
- Cohort retention analysis
- Market basket analysis
- Advanced demand and pricing analysis
- Profitability and margin analysis using external cost data
- Inventory and stock-economics analysis using external inventory data
- Production-style data pipeline
- Star-schema data modelling
- Automated BI reporting and KPI refresh
- Potential cloud-based data engineering architecture