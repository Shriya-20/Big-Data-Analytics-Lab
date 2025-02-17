sales_data = LOAD '/user/220968020/week5/input.csv' USING PigStorage(',') AS (order_id:int, product:chararray, category:chararray, amount:float);
first_10_records = LIMIT sales_data 10;
DUMP first_10_records;
STORE first_10_records INTO '/user/220968020/week5/output1/' USING PigStorage(',');
