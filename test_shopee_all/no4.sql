SELECT
	t1.City, t2.pembelian_pertama, count(t2.customer_id) as jumlah
FROM Customer t1
join (
	select
  		customer_id, min(order_date) as pembelian_pertama
  	from Orders
  	group by customer_id
)t2 ON t1.Customer_ID = t2.customer_id
group by city, pembelian_pertama
order by jumlah desc