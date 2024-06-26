SELECT
	t1.Customer_ID as ID, t1.Sales
FROM Orders t1
join (
	select
  		customer_id, min(order_date) as pembelian_pertama
  	from Orders
  	GROUP by customer_id
)t2 on t1.Customer_ID = t2.customer_id and t1.Order_Date = t2.pembelian_pertama
order by id asc