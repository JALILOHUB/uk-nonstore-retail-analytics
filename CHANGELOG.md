# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-09-12

### Added
- Initial portfolio release of the UCI Online Retail Business Analysis.
- Complete Jupyter Notebook (`03_Notebooks/01_Online_Retail_Analysis.ipynb`) documenting the end-to-end analytical workflow.
- Executive Presentation (`04_Outputs/Reports/UCI_Retail_Executive_Presentation.pdf` and `.pptx`) featuring 11 strategic slides and 12 embedded charts.
- Comprehensive `README.md` with project structure, key findings, and methodology.
- Data dictionary, decision log, and project plan for full transparency and reproducibility.
- Automated Python export pipeline (`export_project_docs.py`) for tables and charts.
- 6 Power BI-ready data splits in `01_Raw_Data/` (transactions, products, customers, countries, time series, segments).

### Key Insights Delivered
- Identified a "Dual-Driver Phenomenon" in November 2011 seasonality.
- Validated a healthy Pareto 26/80 customer concentration (Gini = 0.142).
- Uncovered a critical geographic concentration risk (84.6% revenue from the UK).
- Segmented the customer base into 4 actionable RFM groups, revealing a 47.8% retention opportunity.

### Known Limitations (To be addressed in v1.1)
- Extreme outlier handling logic will be refined for better revenue reconciliation.
- Visualization consistency will be enhanced across all notebooks.
- Minor text refinements based on supervisor feedback.

---

## [Unreleased]

### Planned for v1.1 (Data & Logic Corrections)
- Refine outlier isolation logic to improve revenue reconciliation accuracy.
- Enhance visualization consistency (colors, labels, and chart types).
- Address minor supervisor feedback on analytical wording.

### Planned for v2.0 (Professionalization & Optimization)
- Code refactoring for performance optimization (e.g., vectorization).
- Advanced analytics: Customer Lifetime Value (CLV), Cohort Retention Analysis, and Market Basket Analysis.
- Enhanced documentation and automated reporting pipelines.