SELECT
	Customer.City as kota,
    min(Order_Date) as tanggal,
    COUNT(Orders.Customer_ID) as jumlah_kustomer
FROM Orders
JOIN Customer on Orders.Customer_ID = Customer.Customer_ID
GROUP by kota
ORDER by tanggal;