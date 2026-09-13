\# Decision Log — UCI Online Retail Analysis



| Date | Decision | Why | Evidence | Impact |

|------|----------|-----|----------|--------|

| 2026-09-12 | Isolated extreme outlier (PAPER CRAFT, LITTLE BIRDIE) | Single invoice with 80,995 units would distort statistical analysis | 1 invoice with 80,995 units (£168,469.60) | Preserved total revenue reconciliation while preventing statistical distortion in product analysis |

| 2026-09-12 | Excluded operational items from product rankings | POSTAGE, Manual, Bank Charges are service fees and accounting adjustments, not physical products | £362,268.47 in operational items across 4 categories | Accurate product performance analysis; prevented misleading inventory decisions |

| 2026-09-12 | Labeled missing CustomerID as "Unknown" for sales tracking | 24.93% missing CustomerID likely represents B2C guest checkouts, not system errors | 135,080 rows with missing CustomerID; Avg Qty=2.00, Avg Price=£8.08 | Preserved revenue data while excluding from RFM/Pareto analysis to maintain analytical integrity |

| 2026-09-12 | Removed exact duplicates | 5,268 exact duplicate rows would artificially inflate metrics | 5,268 duplicate rows across all columns | Prevented artificial inflation of revenue and transaction count metrics |

| 2026-09-12 | Excluded Unknown CustomerID from RFM analysis | Cannot calculate meaningful Recency/Frequency/Monetary for unknown customers | 135,080 rows with no customer identity | Maintained RFM analytical integrity; focused on 4,338 known customers |

| 2026-09-12 | Isolated (not deleted) extreme outlier | Deleting would lose £168,469.60 in revenue; keeping would distort statistics | Single invoice: 80,995 units of PAPER CRAFT, LITTLE BIRDIE | Balanced revenue reconciliation with statistical accuracy |

| 2026-09-12 | Created separate df\_sales and df\_customers datasets | Different analytical purposes require different data subsets | Need clean data for both product and customer analysis | Enabled parallel analysis paths without data contamination |

| 2026-09-12 | Used internal benchmarks only | External benchmarks may not apply to this specific business context | Unique B2B wholesale business model | Ensured findings are relevant and actionable for this specific business |

