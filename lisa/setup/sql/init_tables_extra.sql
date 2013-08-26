-- Add market names
-- NOTE: see list of country codes at:
-- http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm
--TODO: check if this still maps to the current market id's in production
--and check this when using KETTLE
INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(2, 'ams', 'Amsterdam stock exchange AEX25', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(3, 'ebr', 'Brussels stock exchange BEL20', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(4, 'etr', 'Frankfurt Xetra DAX30', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(5, 'epa', 'Paris Stock Exchange CAC40', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(6, 'other', 'Other', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(7, 'eli', 'Lisbon Stock Exchange', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(8, 'lse', 'London Stock Exchange', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(9, 'ise', 'Irish Stock Exchange (Dublin)', 'IE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(10, 'mil', 'Milan Stock Exchange', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(11, 'bma', 'Bolsa de Madrid', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(12, 'vse', 'Vienna Stock Exchange', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(13, 'cfd .gold', 'CFD - World Spot Gold', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(14, 'cfd .silver', 'CFD - World Spot Silver', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(15, 'cfd oil', 'CFD - Brent and WTI oil', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(16, 'cfd other non-share', 'CFD - other non-share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(17, 'cfd BE', 'CFD - Belgium', 'BE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(18, 'cfd FR', 'CFD - France', 'FR', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(19, 'cfd DE', 'CFD - Germany', 'DE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(20, 'cfd UK', 'CFD - United Kingdom', 'UK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(21, 'cfd DK', 'CFD - Denmark', 'DK', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(22, 'cfd FI', 'CFD - Finland', 'FI', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(23, 'cfd IT', 'CFD - Italy', 'IT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(24, 'cfd NL', 'CFD - Netherlands', 'NL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(25, 'cfd NO', 'CFD - Norway', 'NO', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(26, 'cfd PT', 'CFD - Portugal', 'PT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(27, 'cfd SE', 'CFD - Sweden', 'SE', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(28, 'cfd CH', 'CFD - Switzerland', 'CH', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(29, 'cfd ES', 'CFD - Spain', 'ES', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(30, 'cfd other share', 'CFD - other share', '', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(31, 'cfd AU', 'CFD - Australia', 'AU', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(32, 'cfd AT', 'CFD - Austria', 'AT', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(33, 'cfd CN', 'CFD - China', 'CN', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(34, 'cfd PL', 'CFD - Poland', 'PL', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(35, 'cfd SG', 'CFD - Singapore', 'SG', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(36, 'nyse', 'Ney York Stock Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(37, 'nasdaq', 'Nasdaq', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(38, 'otc bb & pinksheets', 'OTC BB & pinksheets', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(39, 'amex', 'American Exchange', 'US', 1, current_date, current_date);

INSERT INTO T_MARKET(market_id, code, name, country, active, date_created, date_modified)
values(40, 'other us', 'Other US markets', 'US', 1, current_date, current_date);

-- Add commodity names
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('rhji', 3, 'RHJI International', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('nests', 3, 'Nestle', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('devg', 3, 'Devgen', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('enin', 3, '4 Energy Invest', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('adhof', 2, 'Koninklijke AHOLD N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('dexb', 3, 'Dexia', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('crxl', 2, 'Crucell N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('drak', 2, 'Draka Holding N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('theb', 3, 'Thenergo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('eurn', 3, 'Euronav', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('tnet', 3, 'Telenet', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('exm', 3, 'Exmar', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('cofb', 3, 'Cofinimmo N.V.', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('fme', 4, 'Fresenius Medical Care', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('gsz', 5, 'GDF Suez SA', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('zsl23.90', 3, 'Zilver Sprinter Long 23.90', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('car', 5, 'Carrefour', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('boka', 2, 'Koninklijke Boskalis Westminster NV', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('sr', 2, 'SNS Reaal NV', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('solb', 3, 'Solvay S.A.', 1, current_date, current_date);

-- CFD's
INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CCZ3.cfd', 16, 'US COCOA, US Dollar DecYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('CTZ3.cfd', 16, 'US Cotton No.2, US Dollar/100 DecYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('KCZ3.cfd', 16, 'US Coffee C, US Dollar/100 DecYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LCCU3.cfd', 16, 'London Cocoa, Pound Sterling SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LEV3.cfd', 16, 'Live Cattle (per 0.01), US Dollar/100 OctYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCU3.cfd', 16, 'London Coffee, US Dollar SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LRCX3.cfd', 16, 'London Coffee, US Dollar NovYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LSUV3.cfd', 16, 'London Sugar, US Dollar OctYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('LWBX3.cfd', 16, 'London Wheat (per 0.01), Pound Sterling NovYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJU3.cfd', 16, 'Orange Juice, US Dollar/100 SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('OJX3.cfd', 16, 'Orange Juice, US Dollar/100 NovYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('SBV3.cfd', 16, 'US Sugar No11, US Dollar/100 OctYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZVU3.cfd', 16, 'US Corn, US Dollar/100 SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZCZ3.cfd', 16, 'US Corn, US Dollar/100 DecYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLU3.cfd', 16, 'US Soybean Oil, US Dollar/100 SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZLV3.cfd', 16, 'US Soybean Oil, US Dollar/100 OctYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSU3.cfd', 16, 'US Soybeans, US Dollar/100 SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZSX3.cfd', 16, 'US Soybeans, US Dollar/100 NovYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWU3.cfd', 16, 'US Wheat, US Dollar/100 SepYY', 1, current_date, current_date);

INSERT INTO T_STOCK_NAME(name, market_id, description, active, date_created, date_modified)
values('ZWZ3.cfd', 16, 'US Wheat, US Dollar/100 DecYY', 1, current_date, current_date);

-- Add accounts for known commodities
/* my accounts */
INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:belf00', 'belf00', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:belf01', 'belf01', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:belf02', 'belf02', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:binb00', 'binb00', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:cash', 'cash', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:payp00', 'payp00', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:unib00', 'unib00', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:current_assets:whsi00', 'whsi00', 1, current_date, current_date);

/* stocks */
INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.ahodf', 'ams.ahodf', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.boka', 'ams.boka', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.crxl', 'ams.crxl', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.drak', 'ams.drak', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.sbm', 'ams.sbm', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ams.sr', 'ams.sr', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.cofb', 'ebr.cofb', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.devg', 'ebr.devg', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.dexb', 'ebr.dexb', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.enin', 'ebr.enin', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.eurn', 'ebr.eurn', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.exm', 'ebr.exm', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.nests', 'ebr.nests', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.rhji', 'ebr.rhji', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.solb', 'ebr.solb', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:ebr.tess', 'ebr.tess', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:epa.car', 'epa.car', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:epa.gsz', 'epa.gsz', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:stock:zsl23.90', 'zsl23.90', 1, current_date, current_date);

/* Commodities */
INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:CCZ3.cfd', 'CCZ3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:CCZ3.cfd', 'CCZ3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:CTZ3.cfd', 'CTZ3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:KCZ3.cfd', 'KCZ3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LCCU3.cfd', 'LCCU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LEV3.cfd', 'LEV3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LRCU3.cfd', 'LRCU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LRCX3.cfd', 'LRCX3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LSUV3.cfd', 'LSUV3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:LWBX3.cfd', 'LWBX3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:OJU3.cfd', 'OJU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:OJX3.cfd', 'OJX3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZVU3.cfd', 'ZVU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZCZ3.cfd', 'ZCZ3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZLU3.cfd', 'ZLU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZLV3.cfd', 'ZLV3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZSU3.cfd', 'ZSU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZSX3.cfd', 'ZSX3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZWU3.cfd', 'ZWU3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:softs:ZWZ3.cfd', 'ZWZ3.cfd', 1, current_date, current_date);

-- oil
INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:oil:.BRENT.cfd', '.BRENT.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:oil:.WTI.cfd', '.WTI.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:oil:.CLV3.cfd', 'CLV3.cfd', 1, current_date, current_date);

INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
values('assets:cfd:oil:.CLX3.cfd', 'CLX3.cfd', 1, current_date, current_date);

/* list:
-- softs - august
CCZ3.cfd - US COCOA, US Dollar Dec13
CTZ3.cfd - US Cotton No.2, US Dollar/100 Dec13
KCZ3.cfd - US Coffee C, US Dollar/100 Dec13
LCCU3.cfd - London Cocoa, Pound Sterling Sep13
LEV3.cfd - Live Cattle (per 0.01), US Dollar/100 Oct13
LRCU3.cfd - London Coffee, US Dollar Sep13
LRCX3.cfd - London Coffee, US Dollar Nov13
LSUV3.cfd - London Sugar, US Dollar Oct13
LWBX3.cfd - London Wheat (per 0.01), Pound Sterling Nov13
OJU3.cfd - Orange Juice, US Dollar/100 Sep13
OJX3.cfd - Orange Juice, US Dollar/100 Nov13
SBV3.cfd - US Sugar No11, US Dollar/100 Oct13
ZVU3.cfd - US Corn, US Dollar/100 Sep13
ZCZ3.cfd - US Corn, US Dollar/100 Dec13
ZLU3.cfd - US Soybean Oil, US Dollar/100 Sep13
ZLV3.cfd - US Soybean Oil, US Dollar/100 Oct13
ZSU3.cfd - US Soybeans, US Dollar/100 Sep13
ZSX3.cfd - US Soybeanr, US Dollar/100 Nov13
ZWU3.cfd - US Wheat, US Dollar/100 Sep13
ZWZ3.cfd - US Wheat, US Dollar/100 Dec13
-- oil (market 15)
.BRENT.cfd - SPOT Brent Crude Oil, US Dollar/100
.WTI.cfd - SPOT WTI Light Crude Oil, US Dollar
CLV3.cfd - WTI Crude Oil, US Dollar Oct13
CLX3.cfd - WTI Crude Oil, US Dollar Nov13
HOU3.cfd - Heating Oil, US Dollar Sep13
HOV3.cfd - Heating Oil, US Dollar Oct13
LCOV3.cfd - Brent Crude Oil, US Dollar/100 Oct13
LCOX3.cfd - Brent Crude Oil, US Dollar/100 Nov13
LGOU3.cfd - London Gas Oil (per 25), US Dollar/100 Sep13
LGOV3.cfd - London Gas Oil (per 25), US Dollar/100 Oct13
-- metals
.GOLD.cfd - Spot Gold, US Dollar
.MGOLD.cfd - MINI Spot Gold, US Dollar
.MSILVER.cfd - Spot Mini Silver, US Dollar/100
.SILVER.cfd - Spot Silver, US Dollar/100
GCZ3.cfd - Gold, US Dollar Dec13
HGU3.cfd - High Grade Copper (per 0.05), US Dollar Sep13
HGZ3.cfd - High Grade Copper (per 0.05), US Dollar Dec13
MINISIU3.cfd - Mini Silver, US Dollar/100 Sep13
MINISIZ3.cfd - Mini Silver, US Dollar/100 Dec13
PAU3.cfd - Palladium, US Dollar Sep13
PAZ3.cfd - Palladium, US Dollar Dec13
PLV3.cfd - Platinum, US Dollar Oct13
SIU3.cfd - Silver, US Dollar/100 Sep13
SIZ3.cfd - Silver, US Dollar/100 Dec13
-- indices (Note: BE not available)
.DE30.cfd - Germany 30 cash, Euro
.ES35 - Spain 35 cash, Euro
.F40.cfd - France 40 cash, Euro
.N25.cfd - Netherlands 25 cash, Euro
*/

--INSERT INTO T_ACCOUNT(name, description, active, date_created, date_modified)
--values('assets:e-mini:commodities:ojx...', 'e-mini:ojx...', 1, current_date, current_date);

-- Add specific parameters
/*INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(1, 'comm_binb_be', 9.75, 'Commission binkbank for buying regular stocks.');

--TODO: add another parameter for the 2500 EUR!
--We need to check for this in the code that determines
--which formula/parameter to use.
INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(2, 'comm_binb_be_below2500', 7.25, 'Commission binkbank for buying regular stocks < 2500 EUR.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(3, 'comm_whsi_commodities_us', 0.25, 'Solid amount for calculation of costs for commodities on US markets.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(4, 'tax_stocks_be', 0.0025, 'Tax on Belgian stock market transactions.');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(5, 'tax_dividend_be', 0.25, 'dividend tax - BE');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(6, 'tax_dividend_d', 0.2675, 'dividend tax - D');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(7, 'tax_dividend_fr', 0.30, 'dividend tax - FR');

INSERT INTO T_PARAMETER(parameter_id, name, value, description)
values(8, 'tax_dividend_nl', 0.15, 'dividend tax - NL');*/

-- Add specific margin types
/*INSERT INTO T_MARGIN_TYPE(margin_type)
values('safety');*/

-- Add specific margins
/* -- Note: this might belong to the bi sql folder
INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Financial reserve after crossover', 1600000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safety margin passive income', 5000, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Safe withdrawal rate', 0.03, current_date, current_date);

INSERT INTO T_MARGIN(margin_type_id, description, value, date_created, date_modified)
values(1, 'Bargain reserve', 100000, current_date, current_date);*/

-- Add specific formulae
--TODO: add a column where you can say what the parameters are?
--TODO: add a table which contains the values for tax and commissions?
/*INSERT INTO T_FORMULA(formula_id, value, description)
values(1, '{0}', 'Default: no formula needed, just use the value.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(2, '{0}+{1}*{2}', 'WHS commission calculation for US markets: <solid amount>+<small fraction>*<number of shares>.');

INSERT INTO T_FORMULA(formula_id, value, description)
values(3, '{0}+{1}*{2}/100', 'WHS commission calculation for non-US markets: <solid amount>+<small percentage>*<order size>.');

--TODO: this system is under review.
--Might be too complex to implement.
INSERT INTO T_FORMULA(formula_id, value, description)
values(4, 'if {0} >= {1} : {2} else {3}', 'commission be stocks');

INSERT INTO T_FORMULA(formula_id, value, description)
values(5, '','commission us stocks');*/
