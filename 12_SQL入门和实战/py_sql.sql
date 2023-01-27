create database py_sql charset utf8;
use py_sql;
create table orders(
    order_date DATE,
    order_id VARCHAR(255),
    money INT,
    province VARCHAR(10)
);
