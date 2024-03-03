SELECT
	t2.City, t1.tanggal, count(t1.customer_id) as num_user
FROM(
SELECT
	customer_id,
	min(order_date) as tanggal
from Orders
GROUP by 1
)as t1
JOIN Customer t2  on t1.customer_id = t2.Customer_ID
GROUP by city, tanggal
ORDER by tanggal