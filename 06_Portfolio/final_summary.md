```markdown

\# Executive Summary: UK Non-Store Retail Business Analysis



\*\*Lead Data Analyst:\*\* Abdeljalil El Khyati  

\*\*Date:\*\* September 2026  



\---



\## 1. Business Context \& Scope

This analysis examines \*\*541,909 transactions\*\* from a UK-based online retailer (December 2010 – December 2011). The company sells unique all-occasion gifts, with a significant wholesale (B2B) customer base. The objective was to transform raw transactional data into \*\*evidence-based, actionable business insights\*\*.



\*\*Key Data Facts:\*\*

\- \*\*Timeframe:\*\* 13 months (Dec 2010 – Dec 2011; December 2011 is incomplete — 9 days only).

\- \*\*Total Valid Revenue:\*\* £10,642,110.80.

\- \*\*Valid Transactions:\*\* 524,878 (after removing cancellations, duplicates, and invalid entries).

\- \*\*Known Customers:\*\* 4,338 (generating 83.5% of revenue).

\- \*\*Unknown/Guest Customers:\*\* Generating 16.5% of revenue.



\---



\## 2. Critical Data Quality Decisions

Before any analysis, we made \*\*evidence-based decisions\*\* to ensure analytical integrity:

\- \*\*Missing CustomerID (24.93%):\*\* Labeled as "Unknown" for sales tracking, but \*\*strictly excluded\*\* from customer behavior analysis (RFM, Pareto). These are likely B2C guest checkouts.

\- \*\*Exact Duplicates (5,268 rows):\*\* Removed to prevent artificial inflation.

\- \*\*Extreme Outlier (1 row):\*\* A single invoice for `PAPER CRAFT , LITTLE BIRDIE` (80,995 units, £168,469.60) was \*\*isolated\*\* (not deleted) to prevent statistical distortion while preserving total revenue reconciliation.

\- \*\*Operational Items (£362,268.47):\*\* `DOTCOM POSTAGE`, `POSTAGE`, `Manual`, and `BANK CHARGES` were \*\*excluded\*\* from product rankings — they are service fees, NOT physical products.



\*\*Result:\*\* A clean dataset of \*\*522,728 physical product transactions\*\* representing \*\*£10,279,842.33\*\* in true merchandise revenue.



\---



\## 3. Key Findings



\### 3.1 Revenue is Highly Concentrated in Time (Seasonality)

\- \*\*November 2011\*\* generated \*\*£1,503,866.78\*\* — approximately \*\*2x the average monthly revenue\*\*.

\- The spike is a \*\*dual-driver phenomenon\*\*:

&#x20; - \*\*Driver A (Core Amplification):\*\* `RABBIT NIGHT LIGHT` generated \*\*£34,478.40\*\* in November alone — \*\*11.7x its monthly average\*\* (48.5% of its annual revenue in one month).

&#x20; - \*\*Driver B (Seasonal Emergence):\*\* Christmas-themed products appeared almost exclusively in November, contributing \*\*£50K+\*\* in incremental revenue.

\- \*\*40% overlap\*\* between November's Top 10 and the rest of the year's Top 10 confirms a \*\*hybrid model\*\*: predictable B2B restocking + distinct seasonal product surge.



\### 3.2 Revenue is Moderately Concentrated in Customers (Pareto 26/80)

\- The top \*\*26.0% of customers\*\* generate \*\*80.0% of revenue\*\*.

\- \*\*Gini Coefficient = 0.142\*\* (surprisingly low for B2B), indicating the business is \*\*not dependent on a few "whale" clients\*\* but on a \*\*broad base of \~1,128 high-value wholesale customers\*\*.

\- This is a \*\*healthy concentration\*\* — losing one top client would be painful but not catastrophic.



\### 3.3 Customer Base Segments into Four Clear Behaviors (RFM)

| Segment | Share | Avg Revenue | Avg Frequency | Avg Recency |

|---------|-------|-------------|---------------|-------------|

| \*\*Champions\*\* | 28.6% (1,243) | £5,465 | 10.0 orders | 18 days |

| \*\*Loyal Customers\*\* | 23.6% (1,022) | £1,176 | 3.2 orders | 55 days |

| \*\*At Risk\*\* | 27.4% (1,188) | £580 | 1.6 orders | 102 days |

| \*\*Lost / Hibernating\*\* | 20.4% (885) | £228 | 1.1 orders | 223 days |



\*\*Critical Insight:\*\* Over half the customer base (47.8%) is either \*\*At Risk\*\* or \*\*Lost\*\* — representing a massive retention opportunity.



\### 3.4 Geographic Concentration is a Strategic Risk

\- \*\*United Kingdom\*\* generates \*\*84.6% of revenue\*\* (£9M) and hosts \*\*90.0% of Champions\*\* (1,119 out of 1,243).

\- This represents a \*\*dual concentration crisis\*\*: the business depends on one country AND on that country's best customers specifically.

\- \*\*High-value niche markets exist\*\* but are underdeveloped:

&#x20; - \*\*EIRE (Ireland):\*\* 4 customers generate £283K (£70K/customer average).

&#x20; - \*\*Netherlands:\*\* 9 customers generate £285K (£31K/customer average).

&#x20; - \*\*Australia:\*\* Highest AOV (£2,429) with only 9 customers.



\### 3.5 Product Portfolio Shows Clear B2B Wholesale Patterns

\- \*\*Top Revenue Product:\*\* `REGENCY CAKESTAND 3 TIER` (£174,156.54 across 1,988 invoices).

\- \*\*Strong B2B Indicators\*\* (Avg\_Qty > 20 per invoice):

&#x20; - `MEDIUM CERAMIC TOP STORAGE JAR`: 312 units/invoice.

&#x20; - `RABBIT NIGHT LIGHT`: 30 units/invoice.

&#x20; - `ASSORTED COLOUR BIRD ORNAMENT`: 25 units/invoice.

&#x20; - `JUMBO BAG RED RETROSPOT`: 23 units/invoice.

\- \*\*Dead Stock Alert:\*\* Bottom 10 products generate only \*\*£4–£11 total\*\* — storage costs likely exceed revenue.



\---



\## 4. Strategic Recommendations



\### 🔴 HIGH PRIORITY (Immediate Action — Next 30 Days)

\- \*\*R1. Protect the UK Champion Base:\*\* Implement a VIP B2B loyalty program for the 1,119 UK Champions and assign dedicated account managers.

\- \*\*R2. Launch "At Risk" Win-Back Campaign:\*\* Deploy automated, personalized email campaigns to the 1,188 "At Risk" customers. Converting just 10% back to Loyal would add \~£690K in annual revenue.

\- \*\*R3. Discontinue or Bundle Dead Stock:\*\* Review the Bottom 10 products and bundle or delist them to free warehouse space.



\### 🟡 MEDIUM PRIORITY (Strategic Investment — Next 90 Days)

\- \*\*R4. Dual-Track Seasonal Inventory Planning:\*\* Pre-build inventory for core surge products by early October, and pre-position Christmas-themed SKUs by mid-September.

\- \*\*R5. International Diversification:\*\* Invest in targeted B2B marketing in France (35 Champions) and Germany (33 Champions). Assign dedicated managers to EIRE and Netherlands "whale" clients. Target: Reduce UK revenue share to <70% within 2 years.

\- \*\*R6. Separate Operational Revenue in Reporting:\*\* Create distinct KPIs for "Product Revenue" (£10.28M) vs "Operational Revenue" (£362K) in all dashboards.



\### 🟢 LONG-TERM PRIORITY (Structural Improvement — Next 6–12 Months)

\- \*\*R7. Guest-to-Registered Conversion:\*\* Implement post-purchase email flows to convert the 15–23% revenue from "Unknown" customers into registered accounts.

\- \*\*R8. Upsell Loyal Customers:\*\* Introduce volume-based bundle discounts for the 1,022 Loyal Customers to push them into the Champions tier.



\---



\## 5. Conclusion

This analysis reveals a \*\*healthy but vulnerable business\*\*: strong B2B wholesale foundation, predictable seasonal patterns, and a diversified customer base within the UK market. However, the \*\*dual geographic concentration\*\* (84.6% revenue + 90% Champions in the UK) represents a strategic risk that must be addressed.



The most immediate opportunity lies in \*\*customer retention\*\*: nearly half the customer base is At Risk or Lost, and targeted win-back campaigns could unlock significant revenue with minimal investment.



\*\*The data speaks clearly: protect your Champions, recover your At Risk customers, diversify geographically, and plan seasonally with precision.\*\*



\---

\*\*Prepared by:\*\* Abdeljalil El Khyati, Lead Data Analyst  

\*Analysis conducted using Python, Pandas, Matplotlib, and Seaborn. All findings are evidence-based and derived from the UCI Online Retail dataset (ID: 352).\*  

© 2026 Abdeljalil El Khyati. All rights reserved.

