# Bluestock Mutual Fund Analytics — Data Dictionary

## Project Overview

This data dictionary describes the datasets used in the Bluestock Mutual Fund Analytics project. It documents the fields, data types, and business meanings used for ETL, SQL analysis, performance analytics, and dashboard development.

---

# 1. Fund Master

Source table: `01_fund_master`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI identifier for the mutual fund scheme |
| fund_house | TEXT | Name of the asset management company |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Broad mutual fund category |
| sub_category | TEXT | Detailed fund sub-category |
| plan | TEXT | Direct or regular investment plan |
| launch_date | DATE | Date on which the scheme was launched |
| benchmark | TEXT | Benchmark index used for performance comparison |
| expense_ratio_pct | REAL | Annual expense ratio as a percentage |
| exit_load_pct | REAL | Exit load charged on redemption |
| min_sip_amount | REAL | Minimum amount required for SIP investment |
| min_lumpsum_amount | REAL | Minimum lump-sum investment amount |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk classification of the scheme |
| sebi_category_code | TEXT | SEBI classification code |

---

# 2. NAV History

Source table: `02_nav_history`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| date | DATE | NAV observation date |
| nav | REAL | Net Asset Value per unit |

---

# 3. AUM by Fund House

Source table: `03_aum_by_fund_house`

| Column | Data Type | Description |
|---|---|---|
| date | DATE | Reporting date |
| fund_house | TEXT | Asset management company |
| aum_lakh_crore | REAL | Assets under management in lakh crore |
| aum_crore | REAL | Assets under management in crore |
| num_schemes | INTEGER | Number of schemes managed by the fund house |

---

# 4. Monthly SIP Inflows

Source table: `04_monthly_sip_inflows`

| Column | Data Type | Description |
|---|---|---|
| month | DATE/TEXT | Reporting month |
| sip_inflow_crore | REAL | Monthly SIP inflows in crore |
| active_sip_accounts_crore | REAL | Number of active SIP accounts in crore |
| new_sip_accounts_lakh | REAL | New SIP accounts in lakh |
| sip_aum_lakh_crore | REAL | SIP-linked AUM in lakh crore |
| yoy_growth_pct | REAL | Year-over-year SIP growth percentage |

---

# 5. Category Inflows

Source table: `05_category_inflows`

| Column | Data Type | Description |
|---|---|---|
| month | DATE/TEXT | Reporting month |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow into the category in crore |

---

# 6. Industry Folio Count

Source table: `06_industry_folio_count`

| Column | Data Type | Description |
|---|---|---|
| month | DATE/TEXT | Reporting month |
| total_folios_crore | REAL | Total mutual fund folios in crore |
| equity_folios_crore | REAL | Equity folios in crore |
| debt_folios_crore | REAL | Debt folios in crore |
| hybrid_folios_crore | REAL | Hybrid fund folios in crore |
| others_folios_crore | REAL | Other category folios in crore |

---

# 7. Scheme Performance

Source table: `07_scheme_performance`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identifier |
| scheme_name | TEXT | Mutual fund scheme name |
| fund_house | TEXT | Asset management company |
| category | TEXT | Fund category |
| plan | TEXT | Direct or regular plan |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Three-year benchmark return |
| alpha | REAL | Excess return relative to expected benchmark-based return |
| beta | REAL | Sensitivity of fund returns to benchmark movements |
| sharpe_ratio | REAL | Risk-adjusted return measure |
| sortino_ratio | REAL | Downside-risk-adjusted return measure |
| std_dev_ann_pct | REAL | Annualized return volatility |
| max_drawdown_pct | REAL | Maximum observed decline from a peak |
| aum_crore | REAL | Scheme AUM in crore |
| expense_ratio_pct | REAL | Expense ratio percentage |
| morningstar_rating | REAL | Morningstar rating |
| risk_grade | TEXT | Risk classification/grade |

---

# 8. Investor Transactions

Source table: `08_investor_transactions`

| Column | Data Type | Description |
|---|---|---|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | Mutual fund scheme identifier |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | Classification of city by tier |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual investor income in lakh |
| payment_mode | TEXT | Mode used for payment |
| kyc_status | TEXT | Investor KYC status |

---

# 9. Portfolio Holdings

Source table: `09_portfolio_holdings`

| Column | Data Type | Description |
|---|---|---|
| amfi_code | INTEGER | Mutual fund scheme identifier |
| stock_symbol | TEXT | Security/stock symbol |
| stock_name | TEXT | Name of the holding |
| sector | TEXT | Sector of the holding |
| weight_pct | REAL | Portfolio weight percentage |
| market_value_cr | REAL | Market value in crore |
| current_price_inr | REAL | Current price in INR |
| portfolio_date | DATE | Portfolio reporting date |

---

# 10. Benchmark Indices

Source table: `10_benchmark_indices`

| Column | Data Type | Description |
|---|---|---|
| date | DATE | Benchmark observation date |
| index_name | TEXT | Name of benchmark index |
| close_value | REAL | Closing index value |

---

# Star Schema

## dim_fund

Stores descriptive information about mutual fund schemes.

Primary Key:

`amfi_code`

## dim_date

Stores calendar information used for time-based analysis.

Primary Key:

`date`

## fact_nav

Stores historical NAV observations.

Primary Key:

`amfi_code + date`

Foreign Keys:

- `amfi_code` → `dim_fund.amfi_code`
- `date` → `dim_date.date`

## fact_performance

Stores scheme-level performance metrics.

Primary Key:

`amfi_code`

Foreign Key:

`amfi_code` → `dim_fund.amfi_code`

## fact_transactions

Stores investor-level transaction records.

Primary Key:

`transaction_id`

Foreign Keys:

- `amfi_code` → `dim_fund.amfi_code`
- `transaction_date` → `dim_date.date`

## fact_aum

Stores fund-house-level AUM observations.

Primary Key:

`date + fund_house`

Foreign Key:

`date` → `dim_date.date`

---

# Key Relationships

```text
dim_fund
   |
   | amfi_code
   |
   +-------- fact_nav
   |
   +-------- fact_performance
   |
   +-------- fact_transactions

dim_date
   |
   +-------- fact_nav
   |
   +-------- fact_transactions
   |
   +-------- fact_aum