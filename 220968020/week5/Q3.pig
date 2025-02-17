sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
sorted_products = ORDER sales_data BY amount DESC;
DUMP sorted_products;
STORE sorted_products INTO '/user/220968020/week5/output3/' USING PigStorage(',');
