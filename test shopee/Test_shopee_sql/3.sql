SELECT
	customer_id,
	min(order_date) as tanggal
from Orders
GROUP by customer_id
ORDER by tanggal ASC