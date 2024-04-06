SELECT
	t2.city,
    count(t1.Order_ID) as total
FROM Orders t1
join (
	SELECT 
  		DISTINCT customer_id, city
  	FROM Customer
) t2 ON t1.Customer_ID = t2.customer_id
GROUP by city
Order by total desc