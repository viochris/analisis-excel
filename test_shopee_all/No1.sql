SELECT
	city,
    COUNT(DISTINCT(customer_id)) as total
from customer
GROUP by city
order by total DESC