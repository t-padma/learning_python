--  This command sets the context to the SQLprep database, meaning all subsequent
--  commands will be executed within this database.
USE [SQLprep]
GO  -- batch separator

-- select specific columns --
-- Use * to select all columns --
SELECT *
FROM Customers;
GO

-- to identify column data types --
SELECT 
    COLUMN_NAME, 
    DATA_TYPE
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'Customers';
GO

-- WHERE followed by AND/OR --
SELECT CustomerID, City, State
FROM Customers
WHERE CustomerID BETWEEN 1000 AND 3000
    AND State IN ('MN')
    OR State IN ('AZ');
GO

-- Using WHERE to filter rows of text data column

-- Using = and != are case sensitive
-- extract all rows corresponding to people in CA
SELECT *
FROM Customers
WHERE State = 'CA'; -- case sensitive
GO

-- extract all rows corresponding to people not in CA
SELECT *
FROM Customers
WHERE State != 'CA'; -- case sensitive
GO

-- LIKE and NOT LIKE are case-insensitive
SELECT *
FROM Customers
WHERE State LIKE 'ca'; -- case insensitive
GO

-- % vs _ (both are used with LIKE or NOT LIKE)
-- % is used to match 0 or more chatacters
SELECT *
FROM Customers
WHERE City LIKE '%am%';
GO

-- _ will match a single character
SELECT *
FROM Customers
WHERE City LIKE 'T_mp_';
GO

-- select all distinct state-city combinations
SELECT DISTINCT State, City
FROM Customers;

-- select all distinct state-city combinations in AZ
SELECT DISTINCT State, City
FROM Customers
WHERE State = 'AZ';

-- ORDER BY for numeric column
-- ORDER BY column_name ASC/DESC
SELECT *
FROM Customers
ORDER BY CustomerID DESC;

-- ORDER BY for text based column
SELECT *
FROM Customers
ORDER BY City ASC;

-- ORDER BY for multiple columns
SELECT *
FROM Customers
ORDER BY City, CustomerID ASC;

-- ORDER BY followed by OFFSET and FETCH NEXT
-- OFFSET to skip first few rows
SELECT *
FROM Customers
WHERE City LIKE 'B%'
ORDER BY FirstName ASC
OFFSET 10 ROWS
FETCH NEXT 100 ROWS ONLY;
