WITH data as (
	select
  		customer_id, min(order_date) as pembelian_pertama
  	from Orders
  	group by customer_id
)



SELECT
	t2.City, t1.pembelian_pertama, count(t1.customer_id) as jumlah
FROM data t1
join Customer t2 on t1.customer_id = t2.Customer_ID
GROUP by city, pembelian_pertama
ORDER by jumlah desc