/* markets */
INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('ams', 'Amsterdam', current_date, current_date);

INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('ebr', 'Brussels', current_date, current_date);

INSERT INTO T_MARKET(code, name, date_created, date_modified)
values('dax', 'Germany', current_date, current_date);

/* stock names */
INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('rhji', '2', 'RHJI International', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('nests', '2', 'Nestle', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('devg', '2', 'Devgen', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('enin', '2', '4 Energy Invest', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('adhof', '1', 'Koninklijke AHOLD N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('dexb', '2', 'Dexia', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('crxl', '1', 'Crucell N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('drak', '1', 'Draka Holding N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('theb', '2', 'Thenergo N.V.', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('eurn', '2', 'Euronav', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('tnet', '2', 'Telenet', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('exm', '2', 'Exmar', current_date, current_date);

INSERT INTO T_STOCK_NAME(name, mid, description, date_created, date_modified)
values('cofb', '2', 'Cofinimmo N.V.', current_date, current_date);

/* products */
INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('account.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('account.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('bill.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('bill.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('car.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('car.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('clothes.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('clothes.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('extra.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('extra.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('food.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('food.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('gift.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('gift.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('hobby.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('hobby.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('house.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('house.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('invest.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('invest.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('refund.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('refund.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('salary.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('salary.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('tax.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('tax.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('travel.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('travel.tx', 0, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('utilities.rx', 1, current_date, current_date);

INSERT INTO T_PRODUCT(product, flg_income, date_created, date_modified)
values('utilities.tx', 0, current_date, current_date);

/* t_object */
INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(1, 'none', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(2, 'buystocks', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(3, 'sellstocks', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(4, 'invest', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(5, 'refund', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(6, 'close', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(7, 'electricity', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(8, 'gas', current_date, current_date);

INSERT INTO T_OBJECT(oid, object, date_created, date_modified)
values(9, 'water', current_date, current_date);

/* margin types */
INSERT INTO T_MARGIN_TYPE(margin_type)
values('safety');

/* margins */
INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve after crossover', 1600000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safety margin passive income', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safe withdrawal rate', 0.03, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Bargain reserve', 100000, current_date, current_date);
COMMIT;
