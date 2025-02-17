sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
sorted_products = ORDER sales_data BY amount DESC;
top_3_products = LIMIT sorted_products 3;
DUMP top_3_products;
STORE top_3_products INTO '/user/220968020/week5/output6/' USING PigStorage(',');
