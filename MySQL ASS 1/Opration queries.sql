USE ASSIGNMENT1;
# Count the number of Salesperson whose name begin with ‘a’/’A’.
SELECT COUNT(SNAME)
FROM SALESPEOPLE
WHERE SNAME LIKE 'a%' OR 'A%';


#  Display all the Salesperson whose all orders worth is more than Rs. 2000.
SELECT S.SNAME, O.AMT
FROM SALESPEOPLE S
LEFT JOIN ORDERS O
ON S.SNUM = O.SNUM
WHERE O.AMT > 2000
ORDER BY O.AMT;

#  Count the number of Salesperson belonging to Newyork.
SELECT COUNT(*) NYBASED
FROM SALESPEOPLE
WHERE CITY = 'NEWYORK';


#  Display the number of Salespeople belonging to London and belonging to Paris.
SELECT *
FROM SALESPEOPLE 
WHERE CITY= 'LONDON' OR CITY = 'PARIS';


# Display the number of orders taken by each Salesperson and their date of orders.
SELECT S.SNAME,O.ODATE,COUNT(O.ODATE) AS NO_OF_ORDERS
FROM SALESPEOPLE S
LEFT JOIN ORDERS O
ON S.SNUM = O.SNUM
GROUP BY S.SNAME, O.ODATE;