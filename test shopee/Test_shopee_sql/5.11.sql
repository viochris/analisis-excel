SELECT
	customer_id,
	min(order_date) as tanggal
from (
	SELECT customer_id, order_date
  	FROM Orders
  	ORDER by order_id
)
GROUP by customer_id
