SELECT
	customer_id,
    min(order_date) as tanggal
FROM Orders
GROUP by customer_id
order by customer_id asc