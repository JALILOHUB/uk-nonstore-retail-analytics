\# Project Plan — UCI Online Retail Analysis



\*\*Project Lead:\*\* Abdeljalil El Khyati  

\*\*Start Date:\*\* September 2026  

\*\*Current Status:\*\* ✅ Completed (V1.1 Validated Analytical Release)



\---



\## ✅ Completed Phases



\### Phase 1: Environment Setup \& Data Acquisition

\- \[x] Set up project folder structure

\- \[x] Import required libraries (`pandas`, `numpy`, `matplotlib`, `seaborn`)

\- \[x] Fetch data from UCI Repository (ID: 352)

\- \[x] Reconstruct the complete analytical input by combining the required identifier fields

\- \[x] Verify complete dataset: \*\*541,909 rows, 8 columns\*\*



\### Phase 2: Initial Inspection

\- \[x] Examine dataset structure and data types

\- \[x] Identify potential data quality issues

\- \[x] Document initial observations

\- \[x] Verify the expected analytical columns



\### Phase 3: Data Quality Assessment

\- \[x] Missing-value analysis: `CustomerID` (24.93%), `Description` (0.27%)

\- \[x] Duplicate detection: \*\*5,268 exact duplicate rows\*\*

\- \[x] Outlier detection: \*\*80,995-unit extreme observation\*\*

\- \[x] Operational/non-product item identification: \*\*£362,103.47 across 2,149 rows\*\*



\### Phase 4: Cleaning \& Preparation

\- \[x] Remove 5,268 exact duplicate rows

\- \[x] Isolate the extreme outlier while preserving it for reconciliation

\- \[x] Exclude operational/non-product items from physical-product analysis

\- \[x] Represent missing `CustomerID` values as `Unknown CustomerID` for aggregate sales analysis

\- \[x] Create clean physical-product dataset: \*\*522,728 rows\*\*

\- \[x] Create separate analytical populations for sales and customer analysis



\### Phase 5: Baseline KPIs

\- \[x] Total valid sales revenue: \*\*£10,642,110.80\*\*

\- \[x] Valid sales rows: \*\*524,878\*\*

\- \[x] Known customers: \*\*4,338\*\*

\- \[x] Known-customer revenue share: \*\*83.5%\*\*

\- \[x] Unknown `CustomerID` revenue share: \*\*16.5%\*\*

\- \[x] Average Order Value (AOV): \*\*£533.17\*\* (computed from `df\_sales`)



\### Phase 6: Seasonal \& Product Analysis

\- \[x] Identify November 2011 peak: \*\*£1,503,866.78\*\*

\- \[x] Identify distinct November patterns involving core-product amplification and seasonal-product emergence

\- \[x] Compare November Top 10 products with Top 10 products from other observed months

\- \[x] Rank physical products by observed revenue

\- \[x] Identify a low-revenue product tail for potential catalog review



\### Phase 7: Customer \& Geographic Analytics

\- \[x] Customer concentration analysis using the known-customer population

\- \[x] Pareto analysis: approximately \*\*26% of known customers generate 80% of known-customer revenue\*\*

\- \[x] Validate corrected Gini coefficient: \*\*0.716\*\*

\- \[x] RFM segmentation into four behavioral groups

\- \[x] Geographic revenue distribution analysis

\- \[x] Champion concentration by country



\### Phase 8: V1.1 Validation \& Handoff

\- \[x] Formalize row and revenue reconciliation with \*\*£0.00 revenue difference\*\*

\- \[x] Validate clean physical-product revenue: \*\*£10,111,537.73\*\*

\- \[x] Validate operational revenue: \*\*£362,103.47\*\*

\- \[x] Refine interpretation boundaries, including:

&#x20; - `Unknown CustomerID` instead of unsupported guest-checkout assumptions

&#x20; - bulk-purchasing indicators instead of confirmed B2B transaction claims

&#x20; - historical RFM revenue baseline instead of guaranteed recoverable revenue

&#x20; - low-revenue product tail instead of confirmed dead stock

\- \[x] Export \*\*10 analytical charts\*\*

\- \[x] Export \*\*20 analytical tables\*\*

\- \[x] Generate executive presentation in \*\*PPTX and PDF\*\* formats



\---



\## 📊 Key Deliverables Status



\- \[x] Clean physical-product dataset — 522,728 rows

\- \[x] Baseline KPI outputs

\- \[x] Monthly and seasonal revenue analysis

\- \[x] Product performance analysis

\- \[x] Customer concentration analysis

\- \[x] RFM customer segmentation

\- \[x] Geographic concentration analysis

\- \[x] Operational revenue analysis

\- \[x] Management implications and recommended next analyses

\- \[x] Executive Presentation (PDF \& PPTX)

\- \[x] Portfolio documentation



\---



\## 📅 Timeline



| Phase | Start Date | End Date | Status |

|-------|------------|----------|--------|

| Phase 1–4: Data Preparation | Sep 2026 | Sep 2026 | ✅ Complete |

| Phase 5–7: Baseline, Product \& Customer Analysis | Sep 2026 | Sep 2026 | ✅ Complete |

| Phase 8: V1.1 Validation \& Handoff | Sep 2026 | Sep 2026 | ✅ Complete |

| Phase 9+: Advanced Analytics (v2.0) | TBD | TBD |  Planned |



\---



\## 🎯 Success Criteria



\- \[x] Evidence-based decision making throughout

\- \[x] Documented data-quality decisions

\- \[x] Traceable revenue and row reconciliation

\- \[x] Separation of physical-product and operational revenue

\- \[x] Explicit analytical limitations

\- \[x] Business-oriented interpretation of observed patterns

\- \[x] Actionable management implications supported by the analysis

\- \[ ] Customer Lifetime Value model with validated financial assumptions (v2.0)

\- \[ ] Cohort analysis with retention metrics (v2.0)

\- \[ ] Market basket analysis with association rules (v2.0)

\- \[ ] Automated reporting pipeline (v2.0)



\---



\##  Future Development (v2.0 Planned)



\### Customer Analytics

\- \[ ] Customer Lifetime Value (CLV) modelling

\- \[ ] Cohort retention analysis

\- \[ ] More granular customer reactivation analysis

\- \[ ] Churn-risk modelling with validation data



\### Product \& Commercial Analytics

\- \[ ] Market basket analysis

\- \[ ] Demand forecasting

\- \[ ] Pricing analysis

\- \[ ] Product affinity analysis



\### Business Economics

\- \[ ] Profitability and margin analysis

\- \[ ] Inventory economics

\- \[ ] Product rationalisation using external cost/inventory data



\### Data Engineering \& BI

\- \[ ] Production-style data pipeline

\- \[ ] Star-schema modelling

\- \[ ] Automated KPI refresh

\- \[ ] BI reporting layer

\- \[ ] Potential cloud-based data engineering architecture



\---



\*\*Last Updated:\*\* September 2026  

\*\*Next Review:\*\* Prior to initiating v2.0 Advanced Analytics

