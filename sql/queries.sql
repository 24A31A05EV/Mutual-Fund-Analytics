-- ============================================================
-- Bluestock Mutual Fund Analytics
-- Week 1 - Analytical SQL Queries
-- ============================================================

-- Q1. Top 5 Funds by AUM
SELECT
    f.scheme_name,
    f.fund_house,
    p.aum_crore
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;


-- Q2. Average NAV Per Month
SELECT
    d.year,
    d.month,
    d.month_name,
    ROUND(AVG(n.nav), 2) AS average_nav
FROM fact_nav n
JOIN dim_date d
    ON n.date = d.date
GROUP BY d.year, d.month, d.month_name
ORDER BY d.year, d.month;


-- Q3. SIP Year-over-Year Growth
SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM "04_monthly_sip_inflows"
ORDER BY month;


-- Q4. Transactions by State
SELECT
    state,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;


-- Q5. Funds with Expense Ratio Below 1%
SELECT
    f.scheme_name,
    f.fund_house,
    p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
WHERE p.expense_ratio_pct < 1.0
ORDER BY p.expense_ratio_pct;


-- Q6. Top 10 Funds by 1-Year Return
SELECT
    f.scheme_name,
    f.fund_house,
    p.return_1yr_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
WHERE p.return_1yr_pct IS NOT NULL
ORDER BY p.return_1yr_pct DESC
LIMIT 10;


-- Q7. Average Return by Fund Category
SELECT
    f.category,
    ROUND(AVG(p.return_1yr_pct), 2) AS avg_1yr_return_pct,
    ROUND(AVG(p.return_3yr_pct), 2) AS avg_3yr_return_pct,
    COUNT(*) AS number_of_funds
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
GROUP BY f.category
ORDER BY avg_1yr_return_pct DESC;


-- Q8. Transaction Type Analysis
SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr,
    ROUND(AVG(amount_inr), 2) AS average_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount_inr DESC;


-- Q9. Top 10 Funds by Sharpe Ratio
SELECT
    f.scheme_name,
    f.fund_house,
    p.sharpe_ratio,
    p.std_dev_ann_pct
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
WHERE p.sharpe_ratio IS NOT NULL
ORDER BY p.sharpe_ratio DESC
LIMIT 10;


-- Q10. Monthly AUM by Fund House
SELECT
    date,
    fund_house,
    ROUND(aum_lakh_crore, 2) AS aum_lakh_crore,
    ROUND(aum_crore, 2) AS aum_crore,
    num_schemes
FROM fact_aum
ORDER BY date, aum_crore DESC;