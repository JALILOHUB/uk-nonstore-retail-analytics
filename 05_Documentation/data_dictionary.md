\# Data Dictionary — UCI Online Retail



\## Dataset Overview

\- \*\*Source:\*\* UCI Machine Learning Repository (Dataset ID: 352)

\- \*\*Timeframe:\*\* December 1, 2010 – December 9, 2011

\- \*\*Total Raw Records:\*\* 541,909 transactions

\- \*\*Clean Physical Product Records:\*\* 522,728 transactions (after excluding duplicates, cancellations, and operational fees)



\---



\## Core Variables



| Column | Data Type | Description | Known Issues \& Analytical Notes |

|--------|-----------|-------------|--------------------------------|

| \*\*InvoiceNo\*\* | String (Categorical) | 6-digit integral number uniquely assigned to each transaction. | Starts with 'C' indicates a cancellation. \*\*0% missing\*\*. |

| \*\*StockCode\*\* | String (Categorical) | 5-digit integral number uniquely assigned to each distinct product. | \*\*0% missing\*\*. |

| \*\*Description\*\* | String (Categorical) | Product (item) name. | \*\*0.27% missing\*\* (1,454 records). Some entries are operational (e.g., "POSTAGE", "Manual", "Bank Charges") and were excluded from product performance analysis. |

| \*\*Quantity\*\* | Integer | Quantities of each product (item) per transaction. | Range: -80,995 to 80,995. Negative values indicate returns/cancellations. Extreme positive values indicate B2B wholesale orders. |

| \*\*InvoiceDate\*\* | Datetime | Day and time when each transaction was generated. | Format: DD/MM/YYYY HH:MM. \*\*0% missing\*\*. |

| \*\*UnitPrice\*\* | Float (Continuous) | Product price per unit in sterling (£). | Range: -11,062.06 to 38,970.00. Zero or negative values indicate refunds, discounts, or accounting adjustments. |

| \*\*CustomerID\*\* | Float (Categorical) | 5-digit integral number uniquely assigned to each customer. | \*\*24.93% missing\*\* (135,080 records). Stored as Float due to NaN values. Labeled as "Unknown" for sales tracking, but strictly excluded from RFM/Pareto customer behavior analysis. |

| \*\*Country\*\* | String (Categorical) | Name of the country where each customer resides. | 38 unique countries. \*\*0% missing\*\*. |



\---



\## Derived Variables (Created during Analysis)



| Column | Data Type | Description | Notes |

|--------|-----------|-------------|-------|

| \*\*Revenue\*\* | Float | Calculated as `Quantity` × `UnitPrice`. | Calculated only for valid, positive transactions. Excludes cancellations and operational adjustments. |

| \*\*Month\*\* | Period | Extracted from `InvoiceDate` for monthly aggregation. | Format: YYYY-MM. Used for time-series and seasonality analysis. |

| \*\*Customer\_Type\*\* | String | Categorical label: "Known" or "Unknown". | Used to separate B2B wholesale behavior from guest/B2C checkout behavior. |



\---



\## Critical Data Quality Decisions Documented

1\. \*\*Extreme Outlier Handling:\*\* A single invoice (`InvoiceNo`: 540421) containing 80,995 units of "PAPER CRAFT, LITTLE BIRDIE" (£168,469.60) was \*\*isolated\*\* during product analysis to prevent statistical distortion, but \*\*retained\*\* in total revenue reconciliation.

2\. \*\*Operational Items Exclusion:\*\* £362,268.47 in revenue from "DOTCOM POSTAGE", "POSTAGE", "Manual", and "Bank Charges" was excluded from product rankings, as these are service fees, not physical merchandise.

3\. \*\*Missing CustomerID Strategy:\*\* Instead of dropping the 135,080 rows (which would lose 16.5% of total revenue), they were labeled "Unknown". This preserves revenue integrity for overall sales analysis while maintaining the statistical validity of the RFM segmentation (which requires known identities).

4\. \*\*Incomplete December 2011:\*\* Data for December 2011 covers only 9 days. It was excluded from monthly trend comparisons to prevent misleading "drop" conclusions.

