DROP DATABASE IF EXISTS pizza_db;
CREATE DATABASE pizza_db;

select * from pizza_sales;

-- Total Pendapatan (Revenue)
select sum(total_price) as total_revenue from pizza_sales;

-- Rata-rata order (Average Order Value)
select sum(total_price) / count(distinct order_id) as average_order_value from pizza_sales;

-- Jumlah pizza yang terjual (Total Pizzas Sold)
select sum(quantity) as total_pizza_sold from pizza_sales;

-- Total orders
select count(distinct order_id) as total_order from pizza_sales;

-- Rata rata jumlah pizza yang terjual per order (Average Pizzas Per Order)
select cast(cast(sum(quantity) as decimal(10, 2)) / cast(count(distinct order_id) as decimal(10, 2)) as  decimal(10, 2)) as average_pizza_per_order from pizza_sales;

-- Tren harian untuk total pesanan (Daily Trend for Total Orders)
SELECT DAYNAME(order_date) AS order_day, COUNT(DISTINCT order_id) AS total_orders 
FROM pizza_sales
GROUP BY DAYNAME(order_date)

-- Tren bulanan untuk total pesanan (Monthly Trend for Orders)
select MONTHNAME(order_date) as Month_Name, COUNT(DISTINCT order_id) as Total_Orders
from pizza_sales
GROUP BY MONTHNAME(order_date)

-- Presentase penjualan berdasarkan kategori pizza (% of Sales by Pizza Category)
SELECT pizza_category, CAST(SUM(total_price) AS DECIMAL(10,2)) as total_revenue,
CAST(SUM(total_price) * 100 / (SELECT SUM(total_price) from pizza_sales) AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_category;

-- Presentase penjualan berdasarkan ukuran pizza (. % of Sales by Pizza Size) 
SELECT pizza_size, CAST(SUM(total_price) AS DECIMAL(10,2)) as total_revenue,
CAST(SUM(total_price) * 100 / (SELECT SUM(total_price) from pizza_sales) AS DECIMAL(10,2)) AS PCT
FROM pizza_sales
GROUP BY pizza_size
ORDER BY pizza_size

-- Pizza teratas berdasarkan pendapatan 
SELECT pizza_name, SUM(total_price) AS Total_Revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue DESC;

-- Pizza terbawah berdasakan pendapatan
SELECT pizza_name, SUM(total_price) AS Total_Revenue
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Revenue ASC;

-- Pizza teratas berdasarkan penjualan (sold) 
SELECT pizza_name, SUM(quantity) AS Total_Pizza_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizza_Sold DESC;

-- Pizza terbawah berdasarkan penjualan (sold) 
SELECT pizza_name, SUM(quantity) AS Total_Pizza_Sold
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Pizza_Sold ASC;

-- Pizza teratas berdasarkan total order 
SELECT pizza_name, COUNT(DISTINCT order_id) AS Total_Orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Orders DESC;

-- Pizza terbawah berdasarkan total order 
SELECT pizza_name, COUNT(DISTINCT order_id) AS Total_Orders
FROM pizza_sales
GROUP BY pizza_name
ORDER BY Total_Orders ASC;
















