SELECT
 city,
 count(order_id) as jumlah
from Customer
join Orders on Customer.Customer_ID = Orders.Customer_ID
GROUP by city
ORDER by jumlah DESC