BEGIN;
truncate table T_TEAM;
truncate table T_MARKET cascade;
truncate table T_OBJECT cascade;
truncate table T_PRODUCT;
truncate table T_MARGIN_TYPE cascade;
truncate table T_MARGIN;
truncate table T_BET_CURRENT;
truncate table T_BET_RESULT;
truncate table T_BET;
truncate table T_STOCK_CURRENT;
truncate table T_STOCK_NAME cascade;
truncate table T_STOCK;
truncate table T_FINANCE cascade;
drop table T_TEAM;
drop table T_PRODUCT;
drop table T_OBJECT;
drop table T_MARGIN;
drop table T_MARGIN_TYPE;
drop table T_BET_CURRENT;
drop table T_BET_RESULT;
drop table T_BET;
drop table T_STOCK_CURRENT;
drop table T_STOCK;
drop table T_STOCK_NAME;
drop table T_MARKET;
drop table T_FINANCE;
COMMIT;
