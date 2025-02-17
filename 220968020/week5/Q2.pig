sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
filtered_products = FILTER sales_data BY amount > 5000;
DUMP filtered_products;
STORE filtered_products INTO '/user/220968020/week5/output2/' USING PigStorage(',');
