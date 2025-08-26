CREATE TABLE sales_data (
  rowid int NOT NULL,
  product_id int NOT NULL,
  customer_id int NOT NULL,
  price decimal DEFAULT 0.0 NOT NULL,
  quantity int NOT NULL,
  timeestamp timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL); 