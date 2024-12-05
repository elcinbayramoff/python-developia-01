"""
Structured Query Language

•DML - Data Manipulation Language
INSERT INTO Customers (Name, Email) VALUES ('John Doe', 'john@example.com');
UPDATE Products SET Price = 29.99 WHERE Category = 'Electronics';
DELETE FROM Orders WHERE OrderDate < '2023-01-01';


•DQL
SELECT FirstName, LastName FROM Employees WHERE Department = 'HR';
SEÇ Ad Soyad İşçilərdən hansı ki sahəsi HR-dir
İşçilərdən sahəsi HR-olanlardan Ad və Soyadı seç


SELECT ProductName, Price FROM Products WHERE Price < 50;
Seç MəhsulAdı, Qiyməti

•DDL
CREATE TABLE Students (ID INT PRIMARY KEY, Name VARCHAR(50));
ALTER TABLE Customers ADD COLUMN Age INT;
DROP TABLE Orders;


•TCL
BEGIN TRANSACTION;
UPDATE Inventory SET Quantity = Quantity - 10 WHERE ProductID = 101;
SAVEPOINT sp1;
UPDATE Orders SET Status = 'Shipped' WHERE OrderID = 201;
ROLLBACK TO sp1;
COMMIT;

"""