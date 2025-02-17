sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
grouped_by_category = GROUP sales_data BY category;
category_sales_total = FOREACH grouped_by_category GENERATE group AS category, SUM(sales_data.amount) AS total_sales;
DUMP category_sales_total;
STORE category_sales_total INTO '/user/220968020/week5/output4/' USING PigStorage(',');
