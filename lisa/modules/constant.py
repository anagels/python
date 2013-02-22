#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""

from decimal import Decimal

TABLE_FINANCE = 't_finance'
TABLE_INVESTMENT = 't_investment'
TABLE_MARKET = 't_market'
TABLE_STOCK_NAME = 't_stock_name'
TABLE_CATEGORY = 't_category'
TABLE_SUBCATEGORY = 't_subcategory'
TABLE_ACCOUNT = 't_account'
TABLE_CURRENCY = 't_currency'
TABLE_CURRENCY_EXCHANGE = 't_currency_exchange'
TABLE_FORMULA = 't_formula'
TABLE_PARAMETER = 't_parameter'
TABLE_TRADE = 't_trade'
TABLE_RATE = 't_rate'
TABLE_DRAWDOWN = 't_drawdown'
TABLE_MARGIN = 't_margin'
TABLE_MARGIN_TYPE = 't_margin_type'
VIEW_FINANCE = 'v_finance'
VIEW_INVESTMENT = 'v_investment'
VIEW_MARKET = 'v_market'
VIEW_STOCK_NAME = 'v_stock_name'
VIEW_CATEGORY = 'v_category'
VIEW_SUBCATEGORY = 'v_subcategory'
VIEW_ACCOUNT = 'v_account'
VIEW_CURRENCY = 'v_currency'
VIEW_CURRENCY_EXCHANGE = 'v_currency_exchange'
VIEW_FORMULA = 'v_formula'
VIEW_PARAMETER = 'v_parameter'
VIEW_TRADE = 'v_trade'
VIEW_RATE = 'v_rate'
VIEW_DRAWDOWN = 'v_drawdown'
VIEW_MARGIN = 'v_margin'
VIEW_MARGIN_TYPE = 'v_margin_type'
VIEW_REP_CHECK_TOTAL = 'v_rep_check_total'
ERROR_GET_MARKET_DESCRIPTION = "Error in get_marketdescription: "
ERROR_GET_CATEGORIES = "Error in get_categories: "
ERROR_GET_ACCOUNTS = "Error in get_accounts: "
ERROR_GET_CATEGORIES = "Error in get_categories: "
ERROR_GET_SUBCATEGORIES = "Error in get_subcategories: "
ERROR_GET_MARKETS = "Error in get_markets: "
ERROR_GET_STOCK_NAMES = "Error in get_stocknames: "
ERROR_GET_STOCK_DESCRIPTION = "Error in get_stockdescription: "
ERROR_GET_STOCK_INFO = "Error in get_stockinfo: "
ERROR_GET_CURRENCIES = "Error in get_currencies: "
#TODO: delete the file_import_stocks part and the related file
#in modules/stock.py, because it is no longer used (I think?).
ERROR_FILE_IMPORT_STOCKS = "Error in file_import_stocks: "
ERROR_FILE_IMPORT_STOCKS_SESSION = "Error creating session in file_import_stocks: "
#TODO: will be removed later, when updating investments is made.
ERROR_UPDATE_STOCK = "Error in update_stock: "
ERROR_EXPORT_RECORDS = "Error in export_records: "
ERROR_SUBCATEGORY_ID_FROM_SUBCATEGORY = "Error retrieving subcategory_id: "
ERROR_ACCOUNT_ID_FROM_ACCOUNT = "Error retrieving account_id: "
ERROR_WRITE_TO_DATABASE_MAIN = "Error in write_to_database from main controller: "
ERROR_WRITE_TO_DATABASE = "Error in write_to_database: "
ERROR_WRITE_TO_DATABASE_SESSION = "Error creating session in write_to_database: "
ERROR_INSERT_DATABASE = "Error in write_statement_list_insert: "
ERROR_UPDATE_DATABASE = "Error in write_statement_list_update: "
ERROR_DELETE_DATABASE = "Error in write_statement_list_delete: "
ERROR_GET_INPUT_FIELDS = "Error in get_input_fields: "
ERROR_CREATE_STATEMENTS_TABLE_FINANCE = "Error in create_statements_TABLE_FINANCE: "
ERROR_CREATE_STATEMENTS_TABLE_STOCK = "Error in create_statements_TABLE_STOCK: "
ERROR_CREATE_STATEMENTS_TABLE_TRADE = "Error in create_statements_TABLE_TRADE: "
ERROR_CREATE_STATEMENTS_TABLE_INVESTMENT = "Error in create_statements_TABLE_INVESTMENT: "
ERROR_CREATE_STATEMENTS_TABLE_RATE = "Error in create_statements_TABLE_RATE: "
ERROR_CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE = "Error in create_statements_TABLE_CURRENCY_EXCHANGE: "
ERROR_TRADE_ALREADY_STARTED = "Error in trade_already_started: "
ERROR_INVESTMENT_ALREADY_STARTED = "Error in investment_already_started: "
ERROR_NEW_DRAWDOWN_RECORD = "Error in new_drawdown_record: "
MESSAGE_EXEC_ALL = "Executing statements all at once..."
MESSAGE_PREPARING = "Preparing statements..."
MESSAGE_DONE = "Done."
DEFAULT_DATE = "1900-01-01"
DEFAULT_DECIMAL = Decimal(0.0)
DEFAULT_INT = 0
TRADING_ACCOUNT_ID = 6
PARM_TAX = 4
STATEMENT_INSERT = 0
STATEMENT_UPDATE = 1
STATEMENT_DELETE = 2
