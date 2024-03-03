SELECT
 city,
 count(DISTINCT(customer_id)) as jumlah
from Customer
GROUP by city
ORDER by jumlah DESC