\# Data Dictionary — UCI Online Retail



\## Dataset Overview



\- \*\*Source:\*\* UCI Machine Learning Repository (Dataset ID: 352)

\- \*\*Timeframe:\*\* December 1, 2010 – December 9, 2011

\- \*\*Total Raw Records:\*\* 541,909 transactions

\- \*\*Valid Sales Records:\*\* 524,878 transactions

\- \*\*Clean Physical-Product Records:\*\* 522,728 transactions

\- \*\*Known Customers:\*\* 4,338



> ⚠️ \*\*Important:\*\* December 2011 contains only the first 9 days of the month and is therefore treated as an incomplete observation period.



\---



\## Core Variables



| Column | Data Type | Description | Known Issues \& Analytical Notes |

|--------|-----------|-------------|--------------------------------|

| \*\*InvoiceNo\*\* | String (Categorical) | Transaction invoice identifier. | Invoice numbers beginning with `C` indicate cancellations. |

| \*\*StockCode\*\* | String (Categorical) | Product/item identifier. | Some operational entries use non-standard item codes or descriptions and are separated from physical-product analysis where applicable. |

| \*\*Description\*\* | String (Categorical) | Product or item description. | \*\*0.27% missing\*\* (1,454 records). Some descriptions represent operational/non-product entries such as `POSTAGE`, `Manual`, and `BANK CHARGES`. |

| \*\*Quantity\*\* | Integer | Quantity of an item recorded on a transaction. | Negative values are associated with returns/cancellations. Very high positive quantities may indicate bulk purchasing behaviour, but do not by themselves prove a B2B transaction. |

| \*\*InvoiceDate\*\* | Datetime | Date and time when the transaction was generated. | Format: DD/MM/YYYY HH:MM. |

| \*\*UnitPrice\*\* | Float (Continuous) | Unit price in pounds sterling (£). | Non-positive values are excluded from the defined valid-sales population. |

| \*\*CustomerID\*\* | Float (Categorical) | Customer identifier. | \*\*24.93% missing\*\* (135,080 records). Stored as Float because of missing values. Missing identifiers are represented as `Unknown CustomerID` for aggregate analysis and excluded from customer-level RFM and concentration analysis. |

| \*\*Country\*\* | String (Categorical) | Country associated with the customer record. | 38 unique countries. |



\---



\## Derived Variables



| Variable | Data Type | Description | Analytical Notes |

|----------|-----------|-------------|------------------|

| \*\*Revenue\*\* | Float | Calculated as `Quantity × UnitPrice`. | Calculated within the defined valid-sales population. Operational/non-product rows remain part of the valid-sales population for reconciliation but are separated from physical-product analysis. |

| \*\*Month\*\* | Period | Month extracted from `InvoiceDate`. | Format: YYYY-MM. Used for monthly performance and seasonality analysis. |

| \*\*Customer\_Type\*\* | String | Analytical identifier-status classification: `Known` or `Unknown`. | Used to distinguish records with a known CustomerID from records without one. It is \*\*not\*\* interpreted as a customer channel, B2B/B2C classification, or guest-checkout indicator. |



\---



\## Analytical Populations



\### Raw Dataset

\*\*541,909 rows\*\*  

The original analytical input after reconstructing the expected identifier fields.



\### Valid Sales Population

\*\*524,878 rows\*\* | \*\*£10,642,110.80 revenue\*\*  

This population excludes the transaction records defined as cancellations, duplicate records, or non-positive sales during the cleaning workflow.



\### Extreme Outlier

One transaction was isolated from the core physical-product analysis:

\- \*\*Description:\*\* `PAPER CRAFT , LITTLE BIRDIE`

\- \*\*Quantity:\*\* 80,995

\- \*\*Unit Price:\*\* £2.08

\- \*\*Revenue:\*\* £168,469.60  

\*The observation is preserved for reconciliation rather than deleted from the overall analytical lineage.\*



\### Operational / Non-Product Population

\*\*2,149 rows\*\* | \*\*£362,103.47 revenue\*\*  

Known operational descriptions include: `DOTCOM POSTAGE`, `POSTAGE`, `Manual`, and `BANK CHARGES`.  

\*These records are retained in the valid-sales population but excluded

