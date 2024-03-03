SELECT
 t1.Customer_ID as customer, t1.Sales
from Orders t1
JOIN(
	SELECT
	customer_id,
	min(order_date) as tanggal
	from (
		SELECT customer_id, order_date
  		FROM Orders
  		ORDER by order_id
	)
	GROUP by 1
)t2 on t1.Customer_ID = t2.customer_id and t1.Order_Date = t2.tanggal
ORDER by customer