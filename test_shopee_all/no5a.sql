SELECT
	t2.Customer_ID as id, t2.Sales
FROM (
	select
  		customer_id, min(order_date) as pembelian_pertama
  	from Orders
  	GROUP by customer_id
)t1
join Orders t2 on t1.customer_id = t2.Customer_ID and t1.pembelian_pertama = t2.Order_Date
order by id asc