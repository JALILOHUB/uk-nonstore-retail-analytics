# \# Project Plan — UCI Online Retail Analysis

# 

# \*\*Project Lead:\*\* Abdeljalil El Khyati  

# \*\*Start Date:\*\* September 2026  

# \*\*Status:\*\* In Progress (Phase 9 Complete)

# 

# \---

# 

# \## ✅ Completed Phases

# 

# \### Phase 1: Environment Setup \& Data Acquisition

# \- \[x] Set up project folder structure

# \- \[x] Import required libraries (pandas, numpy, matplotlib, seaborn)

# \- \[x] Fetch data from UCI Repository (ID: 352)

# \- \[x] Merge missing columns (InvoiceNo, StockCode) from 'ids' key

# \- \[x] Verify complete dataset: 541,909 rows, 8 columns

# 

# \### Phase 2: Initial Inspection

# \- \[x] Examined dataset structure and data types

# \- \[x] Identified potential data quality issues

# \- \[x] Documented initial observations

# \- \[x] Identified need for column merging

# 

# \### Phase 3: Data Quality Assessment

# \- \[x] Missing values analysis

# &#x20; - CustomerID: 24.93% (135,080 records)

# &#x20; - Description: 0.27% (1,454 records)

# \- \[x] Duplicate detection: 5,268 exact duplicate rows

# \- \[x] Outlier detection: Extreme outlier (80,995 units)

# \- \[x] Operational items identification: £362,268.47

# 

# \### Phase 4: Cleaning \& Preparation

# \- \[x] Removed 5,268 exact duplicates

# \- \[x] Isolated extreme outlier (preserved for revenue reconciliation)

# \- \[x] Excluded operational items from product analysis

# \- \[x] Labeled missing CustomerID as "Unknown"

# \- \[x] Created clean dataset: 522,728 physical product transactions

# \- \[x] Created separate datasets: df\_sales, df\_customers

# 

# \### Phase 5: Baseline KPIs

# \- \[x] Total Revenue: £10,642,110.80

# \- \[x] Valid Transactions: 524,878

# \- \[x] Known Customers: 4,338 (83.5% of revenue)

# \- \[x] Unknown/Guest Revenue: 16.5%

# \- \[x] Average Order Value (AOV): £533.17

# 

# \### Phase 6: Seasonal Analysis

# \- \[x] Identified November 2011 peak: £1.5M (2x monthly average)

# \- \[x] Identified dual-driver phenomenon

# \- \[x] Analyzed November vs. annual Top 10 products

# \- \[x] Confirmed 40% overlap (hybrid model)

# 

# \### Phase 7: Product Analysis

# \- \[x] Identified top revenue products

# \- \[x] Confirmed B2B wholesale patterns (Avg\_Qty > 20)

# \- \[x] Identified dead stock (Bottom 10 products)

# \- \[x] Separated operational items from product rankings

# 

# \### Phase 8: Customer Analysis (Pareto \& Lorenz)

# \- \[x] Validated Pareto 26/80 rule

# \- \[x] Calculated Gini Coefficient: 0.142

# \- \[x] Identified broad B2B base (\~1,128 high-value customers)

# \- \[x] Confirmed healthy concentration (not whale-dependent)

# 

# \### Phase 9: RFM Segmentation

# \- \[x] Calculated Recency, Frequency, Monetary for 4,338 customers

# \- \[x] Assigned RFM scores (quintiles 1-5)

# \- \[x] Created 4 behavioral segments:

# &#x20; - Champions: 28.6% (1,243 customers)

# &#x20; - Loyal Customers: 23.6% (1,022 customers)

# &#x20; - At Risk: 27.4% (1,188 customers)

# &#x20; - Lost/Hibernating: 20.4% (885 customers)

# \- \[x] Identified retention opportunity: 47.8% At Risk or Lost

# 

# \### Phase 10: Geographic Analysis

# \- \[x] Analyzed revenue distribution by country

# \- \[x] Identified UK concentration: 84.6% of revenue

# \- \[x] Cross-referenced RFM Champions with geography

# \- \[x] Identified dual concentration crisis: 90% of Champions in UK

# \- \[x] Identified high-value niche markets (EIRE, Netherlands, Australia)

# \- \[x] Developed strategic recommendations for diversification

# 

# \---

# 

# \## 🔜 Next Steps

# 

# \### Phase 11: Customer Lifetime Value (CLV)

# \- \[ ] Calculate lifetime value of Champions

# \- \[ ] Compare CLV with customer acquisition cost

# \- \[ ] Identify most valuable customer segments

# 

# \### Phase 12: Cohort Retention Analysis

# \- \[ ] Track retention rates by acquisition month

# \- \[ ] Identify churn patterns and triggers

# \- \[ ] Develop retention strategies for At Risk segment

# 

# \### Phase 13: Market Basket Analysis

# \- \[ ] Identify frequently purchased together products

# \- \[ ] Calculate association rules (support, confidence, lift)

# \- \[ ] Develop cross-selling recommendations

# 

# \### Phase 14: Pricing Elasticity Analysis

# \- \[ ] Analyze price sensitivity for high-demand products

# \- \[ ] Test price optimization scenarios

# \- \[ ] Develop pricing strategy recommendations

# 

# \### Phase 15: Channel Attribution

# \- \[ ] Analyze sources of Unknown customers

# \- \[ ] Develop conversion strategies for guest checkouts

# \- \[ ] Calculate conversion ROI

# 

# \### Phase 16: Professionalization \& Optimization

# \- \[ ] Code refactoring for performance

# \- \[ ] Optimize memory usage

# \- \[ ] Enhance documentation

# \- \[ ] Create automated reporting pipeline

# 

# \---

# 

# \## 📊 Key Deliverables

# 

# \### Completed ✅

# \- \[x] Clean dataset (522,728 transactions)

# \- \[x] Baseline KPIs dashboard

# \- \[x] Seasonal analysis report

# \- \[x] Product performance analysis

# \- \[x] Customer segmentation (RFM)

# \- \[x] Geographic concentration analysis

# \- \[x] Strategic recommendations (8 priorities)

# 

# \### In Progress 

# \- \[ ] Customer Lifetime Value model

# \- \[ ] Cohort retention analysis

# \- \[ ] Market basket analysis

# \- \[ ] Pricing elasticity model

# 

# \---

# 

# \## 📅 Timeline

# 

# | Phase | Start Date | End Date | Status |

# |-------|------------|----------|--------|

# | Phase 1-4: Data Preparation | Sep 2026 | Sep 2026 | ✅ Complete |

# | Phase 5-7: Baseline \& Product Analysis | Sep 2026 | Sep 2026 | ✅ Complete |

# | Phase 8-10: Customer \& Geographic Analysis | Sep 2026 | Sep 2026 | ✅ Complete |

# | Phase 11-15: Advanced Analytics | Sep 2026 | Oct 2026 | 🔜 Planned |

# | Phase 16: Professionalization | Oct 2026 | Oct 2026 | 🔜 Planned |

# 

# \---

# 

# \##  Success Criteria

# 

# \- \[x] Evidence-based decision making throughout

# \- \[x] Professional documentation

# \- \[x] Actionable business recommendations

# \- \[ ] CLV model with ROI calculations

# \- \[ ] Cohort analysis with retention metrics

# \- \[ ] Market basket analysis with association rules

# \- \[ ] Automated reporting pipeline

# 

# \---

# 

# \*\*Last Updated:\*\* September 2026  

# \*\*Next Review:\*\* After Phase 11 completion

