sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
customer_data = LOAD '/user/220968020/week5/customer.csv' USING PigStorage(',') AS (order_id:int, customer_name:chararray, city:chararray);
joined_data = JOIN sales_data BY order_id, customer_data BY order_id;
DUMP joined_data;
STORE joined_data INTO '/user/220968020/week5/output5/' USING PigStorage(',');
