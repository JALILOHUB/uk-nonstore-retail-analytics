# Executive Summary: UK Non-Store Retail Business Analysis

**Lead Data Analyst:** Abdeljalil El Khyati  
**Date:** September 2026  
**Version:** 1.1 — Validated Analytical Release  

---

## 1. Business Context & Scope

This analysis examines **541,909 raw transactions** from a UK-based registered non-store online retailer covering the period **1 December 2010 to 9 December 2011**.

The business sells unique all-occasion gifts, and the official UCI dataset description notes that many customers are wholesalers.

The objective was to transform raw transactional data into a structured analytical workflow covering:

- Data quality and validation
- Revenue reconciliation
- Product performance
- Seasonality
- Customer concentration
- RFM customer segmentation
- Geographic concentration
- Operational versus physical-product revenue
- Management-oriented recommendations

The project is an **independent portfolio analysis** simulating a real-world analytical engagement. It is not presented as paid client work or professional commercial experience.

The analytical framework follows:

**DATA → EVIDENCE → INTERPRETATION → ACTION**

Major conclusions are separated conceptually into measured facts, analytical interpretations, hypotheses requiring further validation, and proposed actions.

---

## 2. Business Facts

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
| Unknown CustomerID Revenue | £1,754,901.91 |
| Unknown CustomerID Revenue Share | 16.5% |
| November 2011 Revenue | £1,503,866.78 |

> **Time-series note:** December 2011 contains only the first 9 days of the month and is therefore not treated as a normal full-month observation.

---

## 3. Critical Data Quality Decisions

The analytical workflow applies explicit quality rules before business metrics are calculated.

### Missing CustomerID

**135,080 rows (24.93%)** do not contain a CustomerID.

These transactions are:

- Retained for aggregate sales and revenue analysis
- Represented as `Unknown CustomerID`
- Excluded from customer-level RFM and concentration analysis

The analysis does **not** assume that missing identifiers represent guest checkouts because the dataset does not provide enough evidence to determine the reason for the missing identifiers.

### Exact Duplicates

**5,268 exact duplicate rows** were identified and removed before downstream analysis.

### Cancellations and Invalid Sales

Cancellation transactions and non-positive sales values are excluded from the defined valid-sales population.

### Extreme High-Quantity Observation

One extreme transaction was isolated:

`PAPER CRAFT , LITTLE BIRDIE`

- Quantity: **80,995**
- Unit Price: **£2.08**
- Revenue: **£168,469.60**

The observation was isolated rather than deleted so that its effect could be assessed while maintaining transparent reconciliation.

### Operational / Non-Product Transactions

Known operational descriptions such as:

- `DOTCOM POSTAGE`
- `POSTAGE`
- `Manual`
- `BANK CHARGES`

are separated from physical merchandise analysis.

---

## 4. Revenue Reconciliation

The final analytical transformation from valid sales to physical-product sales was explicitly reconciled.

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

**Reconciliation status: PASSED**

This confirms that the physical-product analytical population is internally consistent with the validated sales population after the documented exclusions and isolations.

---

# 5. Key Findings

## 5.1 November 2011 Was the Highest Observed Revenue Month

November 2011 generated:

**£1,503,866.78**

This was the highest observed monthly revenue in the dataset.

Average monthly revenue is approximately **£840K** when incomplete December 2011 is excluded.

The November analysis also identifies products with substantially higher observed revenue than their average across other months.

### Highest Observed November Seasonal Lift

| Product | November Revenue | Average Other-Month Revenue | Seasonal Lift |
|---|---:|---:|---:|
| RABBIT NIGHT LIGHT | £34,478.40 | £2,069.38 | £32,409.02 |
| PAPER CHAIN KIT 50'S CHRISTMAS | £28,955.54 | £2,641.12 | £26,314.42 |
| POPCORN HOLDER | £14,188.80 | £1,334.19 | £12,854.61 |
| PAPER CHAIN KIT VINTAGE CHRISTMAS | £12,929.74 | £1,559.41 | £11,370.33 |
| HOT WATER BOTTLE KEEP CALM | £11,760.07 | £1,180.37 | £10,579.70 |

These observations identify a strong November seasonal pattern, but the transactional dataset alone does not establish the external causes of the revenue increase.

---

## 5.2 Customer Revenue Is Strongly Concentrated

Customer concentration analysis is based on the **4,338 known customers**.

Key observations:

- Known-customer revenue: **£8,887,208.89**
- Approximately **26% of known customers generate 80% of known-customer revenue**
- **Gini coefficient: 0.716**

The concentration metrics indicate that revenue is substantially unevenly distributed across known customers.

This makes customer concentration an important area for monitoring, retention analysis, and further customer-value modelling.

---

## 5.3 RFM Segmentation Reveals Four Analytical Customer Groups

| Segment | Customers | Share | Avg. Monetary | Avg. Frequency | Avg. Recency |
|---|---:|---:|---:|---:|---:|
| **Champions** | 1,243 | 28.6% | £5,465 | 10.0 | 18 days |
| **Loyal Customers** | 1,022 | 23.6% | £1,176 | 3.2 | 55 days |
| **Potential Loyalists / At Risk** | 1,188 | 27.4% | £580 | 1.6 | 102 days |
| **Lost / Hibernating** | 885 | 20.4% | £228 | 1.1 | 223 days |

The **Potential Loyalists / At Risk** and **Lost / Hibernating** segments together represent **47.8% of known customers**.

Their combined historical observed revenue is approximately **£689K**.

> **Important:** £689K is a historical revenue baseline observed in the dataset. It is not a forecast of recoverable revenue and should not be interpreted as a guaranteed retention opportunity.

RFM segments describe observed customer behaviour and should not be treated as validated churn predictions.

---

## 5.4 Geographic Revenue Is Highly Concentrated in the United Kingdom

The United Kingdom accounts for:

- **84.6% of valid-sales revenue**
- **1,119 of 1,243 Champions**, approximately **90.0%** of the Champion segment

This creates a strong geographic concentration that should remain visible in management reporting.

Selected smaller markets also show meaningful observed revenue despite small known-customer populations:

| Market | Revenue | Known Customers |
|---|---:|---:|
| EIRE | £283K | 3 |
| Netherlands | £285K | 9 |
| Australia | £138K | 9 |

Small customer populations mean that averages and customer-level conclusions for these markets should be interpreted cautiously.

---

## 5.5 Product Portfolio Shows Strong Revenue Leaders and a Long Low-Revenue Tail

The highest-revenue physical product is:

**REGENCY CAKESTAND 3 TIER — £174,156.54 across 1,988 invoices**

The top three physical products generated:

**£379,838.49**, representing approximately **3.8% of clean physical-product revenue**.

The analysis also identifies a low-revenue product tail.

These products are treated as **catalog-review candidates**, not confirmed dead stock, because the dataset does not contain the inventory, cost, margin, or storage information required to establish profitability or stock economics.

### Bulk Purchasing Indicators

Several products show high average quantities per invoice, including:

- `MEDIUM CERAMIC TOP STORAGE JAR`
- `RABBIT NIGHT LIGHT`
- `ASSORTED COLOUR BIRD ORNAMENT`
- `JUMBO BAG RED RETROSPOT`

These patterns may indicate bulk purchasing behaviour.

However, transaction quantity alone is not treated as definitive proof that an individual transaction is B2B.

---

## 5.6 Operational Revenue Should Be Reported Separately

Operational/non-product transactions generated:

**£362,103.47**

across **2,149 rows**.

Separating these transactions from physical merchandise revenue prevents operational charges from distorting product-performance analysis.

The resulting analytical distinction is:

| Revenue Type | Amount |
|---|---:|
| Clean Physical-Product Revenue | **£10,111,537.73** |
| Operational Revenue | £362,103.47 |

---

## 5.7 Unknown CustomerID Activity Represents a Material Share of Revenue

| Customer Identifier Status | Revenue | Share |
|---|---:|---:|
| Known CustomerID | £8,887,208.89 | 83.5% |
| Unknown CustomerID | £1,754,901.91 | 16.5% |

The **16.5% Unknown CustomerID revenue share** is large enough to matter for reporting and customer analytics.

Because the reason for missing identifiers is not available in the dataset, the analysis deliberately avoids describing these transactions as guest checkouts.

---

# 6. Management Implications

The findings suggest several areas for management attention.

### Customer Retention

The **Potential Loyalists / At Risk** and **Lost / Hibernating** segments represent a large portion of known customers.

A logical next step is to test differentiated retention and reactivation strategies using customer-level behaviour rather than applying a single campaign to the entire customer base.

### Seasonal Planning

November-specific product performance suggests value in distinguishing between:

- Products with strong recurring performance
- Products with strong November-specific lift

This distinction can support future demand-planning analysis.

### Geographic Monitoring

The large UK revenue share and concentration of Champions in the UK should remain visible in management dashboards.

Smaller markets can be investigated as potential growth areas, but their small customer populations require careful validation before major resource commitments.

### Revenue Architecture

Dashboards should maintain separate reporting for:

- Physical-product revenue
- Operational/non-product revenue
- Known-customer revenue
- Unknown CustomerID revenue

This improves transparency and prevents mixed business concepts from being interpreted as a single KPI.

---

# 7. Recommended Next Analyses

The current project establishes a foundation for deeper analysis.

### Customer Analytics
- Customer Lifetime Value (CLV)
- Cohort retention analysis
- Customer purchase-frequency analysis
- More granular churn-risk modelling

### Product Analytics
- Market basket analysis
- Product affinity analysis
- Demand and pricing analysis
- Seasonal demand forecasting

### Business Economics
- Profitability analysis
- Margin analysis
- Inventory economics
- Product rationalisation using external cost and inventory data

### Data Engineering / BI Extension
- Production-style data pipeline
- Star-schema modelling
- Automated KPI refresh
- Power BI reporting layer

---

# 8. Analytical Limitations

1. **Incomplete December 2011:** Only the first 9 days are present.
2. **Missing CustomerID:** 24.93% of raw transactions lack customer identifiers, limiting customer-level analysis for those transactions.
3. **No Cost or Inventory Data:** Profitability, margin, storage cost, stock turnover, and confirmed dead-stock analysis cannot be established from this dataset alone.
4. **Observational Dataset:** Observed relationships do not establish causality.
5. **RFM Segmentation:** RFM groups describe observed behaviour and are not validated churn predictions.
6. **Small International Samples:** Revenue and AOV observations in small markets can be sensitive to a small number of customers.
7. **B2B Interpretation Boundary:** High-quantity transactions are treated as bulk-purchasing indicators rather than definitive proof of B2B transactions.
8. **Unknown CustomerID:** The dataset does not provide enough information to determine why CustomerID is missing for a transaction.

---

# 9. Conclusion

The V1.1 analysis establishes a validated analytical foundation for the UCI Online Retail dataset.

The main evidence points are:

- A validated **£10.64M valid-sales revenue population**
- **£10.11M clean physical-product revenue** after documented exclusions and isolation
- A successful **£0.00 revenue reconciliation**
- A strong **November 2011 revenue peak**
- Significant **customer revenue concentration**, with a Gini coefficient of **0.716**
- Four analytical RFM segments, with **47.8% of known customers** classified as Potential Loyalists / At Risk or Lost / Hibernating
- Strong concentration of both revenue and Champions in the **United Kingdom**
- A material **16.5% Unknown CustomerID revenue share**
- Clear high-performing products alongside a long low-revenue product tail
- A meaningful operational revenue component that should remain separate from merchandise performance

The analysis therefore provides a defensible foundation for subsequent work in customer retention, seasonal demand, product strategy, profitability, business intelligence, and eventually more advanced data-engineering workflows.

---

# 10. Portfolio Disclosure

This is an **independent portfolio project** based on the publicly available **UCI Online Retail dataset (Dataset ID: 352)**.

It is intended to demonstrate:

- Data cleaning and validation
- Analytical reasoning
- Business-oriented exploratory analysis
- Customer and product analytics
- Visualization
- Documentation
- Executive communication

The project is **not presented as paid client work or as professional commercial experience**.

---

**Prepared by:** Abdeljalil El Khyati, Lead Data Analyst  
**Analysis tools:** Python, pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook  
**Dataset:** UCI Online Retail — Dataset ID 352  

**Last updated:** September 2026