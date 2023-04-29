SELECT a.name, a.primary_poc, w.occurred_at, w.channel
FROM accounts AS a
JOIN web_events AS w
ON a.id = w.account_id
WHERE a.name = 'Walmart'


SELECT 	r.name AS region_name,
		s.name AS sales_rep_name, 
        a.name AS account_name
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
ORDER BY account_name


SELECT	r.name AS region_name,
		a.name AS account_name,
        o.total_amt_usd / (o.total + 0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
JOIN orders AS o
ON a.id = o.account_id


SELECT	r.name AS region_name,
		s.name AS sales_reps_name,
        a.name AS accounts_name
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest'
ORDER BY a.name


SELECT	r.name AS region_name,
		s.name AS sales_reps_name,
        a.name AS accounts_name
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest' AND s.name LIKE 'S%'
ORDER BY a.name


SELECT	r.name AS region_name,
		s.name AS sales_reps_name,
        a.name AS accounts_name
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
WHERE r.name = 'Midwest' AND s.name LIKE '% %K%'
ORDER BY a.name


SELECT	r.name AS region_name,
		a.name AS account_name,
        o.total_amt_usd / (o.total + 0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
JOIN orders AS o
ON a.id = o.account_id
WHERE o.standard_qty > 100


SELECT	r.name AS region_name,
		a.name AS account_name,
        o.total_amt_usd / (o.total + 0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
JOIN orders AS o
ON a.id = o.account_id
WHERE o.standard_qty > 100 AND poster_qty > 50


SELECT	r.name AS region_name,
		a.name AS account_name,
        o.total_amt_usd / (o.total + 0.01) AS unit_price
FROM region AS r
JOIN sales_reps AS s
ON r.id = s.region_id
JOIN accounts AS a
ON s.id = a.sales_rep_id
JOIN orders AS o
ON a.id = o.account_id
WHERE o.standard_qty > 100 AND poster_qty > 50
ORDER BY unit_price DESC


SELECT DISTINCT	accounts.name,
				web_events.channel
FROM web_events
JOIN accounts
ON web_events.account_id = accounts.id
WHERE accounts.id = 1001


SELECT SUM(poster_amt_usd) AS poster_total_amount
FROM orders


SELECT SUM(standard_qty) AS standard_total_amount
FROM orders


SELECT SUM(total_amt_usd) AS dollar_total_amount
FROM orders


SELECT	id,
		SUM(standard_amt_usd) + SUM (gloss_amt_usd) AS total_amount_spent
FROM orders
GROUP BY id


SELECT SUM(standard_amt_usd)/SUM(standard_qty) AS standard_price_per_unit 
FROM orders;


/* Which account (by name) placed the earliest order? Your solution should have the account name and the date of the order. */

SELECT	accounts.name,
		MIN(orders.occurred_at) AS order_date
FROM accounts
JOIN orders
ON orders.account_id = accounts.id
GROUP BY accounts.name
ORDER BY order_date
LIMIT 1


/* Find the total sales in usd for each account. You should include two columns - the total sales for each company's orders in usd and the company name. */

SELECT	accounts.name,
		SUM(orders.total_amt_usd) AS total_sales_usd
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY accounts.name
ORDER BY accounts.name


/* Via what channel did the most recent (latest) web_event occur, which account was associated with this web_event? Your query should return only three values - the date, channel, and account name. */

SELECT w.occurred_at, w.channel, a.name
FROM web_events w
JOIN accounts a
ON w.account_id = a.id 
ORDER BY w.occurred_at DESC
LIMIT 1;


/* Find the total number of times each type of channel from the web_events was used. Your final table should have two columns - the channel and the number of times the channel was used. */

SELECT	channel,
		COUNT(channel)
FROM web_events
GROUP BY channel


/* Who was the primary contact associated with the earliest web_event? */

SELECT	accounts.primary_poc,
		MIN(web_events.occurred_at) AS earliest_web_event_date
FROM accounts
JOIN web_events
ON accounts.id = web_events.account_id
GROUP BY accounts.primary_poc
ORDER BY earliest_web_event_date
LIMIT 1


/* What was the smallest order placed by each account in terms of total usd. Provide only two columns - the account name and the total usd. Order from smallest dollar amounts to largest. */

SELECT	accounts.name AS account_name,
		MIN(orders.total_amt_usd) AS smallest_order
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY account_name
ORDER BY smallest_order


/* Find the number of sales reps in each region. Your final table should have two columns - the region and the number of sales_reps. Order from the fewest reps to most reps. */

SELECT	region.name,
		COUNT(sales_reps.id) AS sales_reps_count
FROM region
JOIN sales_reps
ON region.id = sales_reps.region_id
GROUP BY region.name
ORDER BY sales_reps_count


/* For each account, determine the average amount of each type of paper they purchased across their orders. Your result should have four columns - one for the account name and one for the average quantity purchased for each of the paper types for each account. */

SELECT	accounts.name,
		AVG(orders.standard_qty) AS standard_average,
        AVG(orders.gloss_qty) AS gloss_average,
        AVG(orders.poster_qty) AS poster_average
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY accounts.name


/* For each account, determine the average amount spent per order on each paper type. Your result should have four columns - one for the account name and one for the average amount spent on each paper type. */

SELECT	accounts.name,
	AVG(orders.standard_amt_usd) AS standard_average,
        AVG(orders.gloss_amt_usd) AS gloss_average,
        AVG(orders.poster_amt_usd) AS poster_average
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY accounts.name


/* Determine the number of times a particular channel was used in the web_events table for each sales rep. Your final table should have three columns - the name of the sales rep, the channel, and the number of occurrences. Order your table with the highest number of occurrences first. */

SELECT	sales_reps.name,
	web_events.channel,
        COUNT(web_events.id) AS num_events
FROM	sales_reps
JOIN	accounts
ON	sales_reps.id = accounts.sales_rep_id
JOIN	web_events
ON	accounts.id = web_events.account_id
GROUP BY sales_reps.name, web_events.channel
ORDER BY num_events DESC


/* Determine the number of times a particular channel was used in the web_events table for each region. Your final table should have three columns - the region name, the channel, and the number of occurrences. Order your table with the highest number of occurrences first. */

SELECT	region.name,
	web_events.channel,
        COUNT(web_events.id) AS num_events
FROM	region
JOIN	sales_reps
ON		region.id = sales_reps.region_id
JOIN	accounts
ON		sales_reps.id = accounts.sales_rep_id
JOIN	web_events
ON		accounts.id = web_events.account_id
GROUP BY region.name, web_events.channel
ORDER BY num_events DESC

/* Use DISTINCT to test if there are any accounts associated with more than one region. */

SELECT	DISTINCT accounts.id,
		region.name
FROM accounts
JOIN sales_reps
ON accounts.sales_rep_id = sales_reps.id
JOIN region
ON sales_reps.region_id = region.id
ORDER BY accounts.id


/* Have any sales reps worked on more than one account? */

SELECT s.id, s.name, COUNT(*) num_accounts
FROM accounts a
JOIN sales_reps s
ON s.id = a.sales_rep_id
GROUP BY s.id, s.name
ORDER BY num_accounts;


/* How many of the sales reps have more than 5 accounts that they manage? */

SELECT	sales_reps.name,
		COUNT(accounts.*) AS nums_account
FROM sales_reps
JOIN accounts
ON sales_reps.id = accounts.sales_rep_id
GROUP BY sales_reps.name
HAVING COUNT(accounts.*) > 5
ORDER BY nums_account DESC


/* How many accounts have more than 20 orders? */

SELECT	accounts.id,
		accounts.name,
        COUNT(orders.*) AS orders_qty
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
HAVING COUNT(orders.*) > 20
ORDER BY orders_qty DESC


/* Which account has the most orders? */

SELECT	accounts.id,
		accounts.name,
        COUNT(orders.*) AS orders_qty
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
ORDER BY orders_qty DESC
LIMIT 1


/* Which accounts spent more than 30,000 usd total across all orders? */

SELECT	accounts.id,
		accounts.name,
        SUM(orders.total_amt_usd) AS total_orders_spent
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
HAVING SUM(orders.total_amt_usd) > 30000
ORDER BY  total_orders_spent DESC


/* Which accounts spent less than 1,000 usd total across all orders? */

SELECT	accounts.id,
		accounts.name,
        SUM(orders.total_amt_usd) AS total_orders_spent
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
HAVING SUM(orders.total_amt_usd) < 1000
ORDER BY  total_orders_spent DESC


/* Which account has spent the most with us? */

SELECT	accounts.id,
		accounts.name,
        SUM(orders.total_amt_usd) AS total_orders_spent
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
ORDER BY  total_orders_spent DESC
LIMIT 1


/* Which account has spent the least with us? */

SELECT	accounts.id,
		accounts.name,
        SUM(orders.total_amt_usd) AS total_orders_spent
FROM accounts
JOIN orders
ON accounts.id = orders.account_id
GROUP BY 1, 2
ORDER BY  total_orders_spent
LIMIT 1


/* Which accounts used facebook as a channel to contact customers more than 6 times? */

SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
HAVING COUNT(*) > 6 AND w.channel = 'facebook'
ORDER BY use_of_channel


/* Which account used facebook most as a channel? */

SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
WHERE w.channel = 'facebook'
GROUP BY a.id, a.name, w.channel
ORDER BY use_of_channel DESC
LIMIT 1


/* Which channel was most frequently used by most accounts? */

SELECT a.id, a.name, w.channel, COUNT(*) use_of_channel
FROM accounts a
JOIN web_events w
ON a.id = w.account_id
GROUP BY a.id, a.name, w.channel
ORDER BY use_of_channel DESC
LIMIT 10;

