\# Decision Log — UCI Online Retail Analysis



| Date | Decision | Why | Evidence | Impact |

|------|----------|-----|----------|--------|

| 2026-09-12 | Isolated extreme outlier (`PAPER CRAFT, LITTLE BIRDIE`) | A single transaction containing 80,995 units could materially distort product-level analysis | 1 transaction: 80,995 units × £2.08 = £168,469.60 | Preserved the observation for reconciliation while preventing it from dominating core physical-product analysis |

| 2026-09-12 | Excluded operational/non-product items from physical-product rankings | Operational entries should not be interpreted as merchandise performance | £362,103.47 across 2,149 rows, including `DOTCOM POSTAGE`, `POSTAGE`, `Manual`, and `BANK CHARGES` | Kept product-performance analysis focused on physical merchandise |

| 2026-09-12 | Represented missing `CustomerID` as `Unknown CustomerID` for aggregate sales analysis | Missing identifiers should not cause valid sales revenue to be discarded; the dataset does not establish the reason for the missing identifiers | 135,080 rows with missing `CustomerID` (24.93%) | Preserved revenue information while excluding unidentified transactions from customer-level RFM and concentration analysis |

| 2026-09-12 | Removed exact duplicates | Exact duplicate records can artificially inflate transaction and revenue metrics | 5,268 exact duplicate rows | Prevented duplicate records from affecting downstream metrics |

| 2026-09-12 | Excluded `Unknown CustomerID` from RFM analysis | Recency, Frequency, and Monetary metrics require a reliable customer identifier | 135,080 rows without customer identity | Maintained customer-level analytical integrity and focused RFM on 4,338 known customers |

| 2026-09-12 | Created separate sales and customer analytical datasets | Product/revenue analysis and customer-level analysis require different populations and fields | `df\_sales` and customer-level analytical data serve different purposes | Enabled parallel analytical paths without mixing incompatible populations |

| 2026-09-12 | Formalized revenue reconciliation | Every transformation from valid sales to physical-product sales should be traceable and verifiable | Row difference: 0; revenue difference: £0.00 | Confirmed that the physical-product analytical population is internally consistent |

| 2026-09-12 | Corrected Gini coefficient calculation | The previous implementation understated customer revenue concentration | Corrected calculation using `1 - 2 \* np.trapezoid(y, x)` | Validated Gini coefficient at \*\*0.716\*\* |

| 2026-09-12 | Refined B2B interpretation | High transaction quantities can indicate bulk purchasing but do not prove the nature of an individual customer or transaction | High-quantity patterns observed across several products | Reported these patterns as bulk-purchasing indicators requiring further validation rather than confirmed B2B transactions |

| 2026-09-12 | Reframed the approximately £689K RFM figure | Historical observed revenue should not be presented as guaranteed recoverable revenue | 1,188 Potential Loyalists / At Risk customers with approximately £689K historical observed revenue | Established the figure as a historical baseline for future retention testing |

| 2026-09-18 | Standardized V1.1 terminology across project documentation | Earlier documentation contained unsupported terms such as "Guest Customers", "Dead Stock", and confirmed B2B claims | V1.1 validation and interpretation review | Aligned documentation with the evidence supported by the dataset |

