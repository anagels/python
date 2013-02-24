#!/usr/local/bin/python
"""
    See LICENSE file for copyright and license details.
"""
from datetime import datetime

from database.databaseaccess import DatabaseAccess
from modules.function import *

class CurrencyExchange(CoreModule):
    """
        CurrencyExchange class.
    """

   def create_statements(self, input_fields):
        """
            Creates the records needed for TABLE_CURRENCY_EXCHANGE.
        """
        try:
            statement_currency_exchange = Statement(TABLE_CURRENCY_EXCHANGE)
            date_created = current_date()
            date_modified = current_date()
            records = 0
            for fields in input_fields:
                records = records + 1
                #NOTE: we don't need to query, because we always add a new
                #currency_exchange line. The same value can be used multiple
                #times, so it's not possible to query if one already exists.
                statement_currency_exchange.add(
                    records,
                    {
                        'currency_exchange_id':None,
                        'from_currency_id':self.currency_id_from_currency(fields['from_currency']),
                        'to_currency_id':int(self.config.default_currency),
                        'exchange_rate':Decimal(fields['exchange_rate']),
                        'date_created':date_created,
                        'date_modified':date_modified
                    }
                )
            return statement_currency_exchange
        except Exception as ex:
            print(ERROR_CREATE_STATEMENTS_TABLE_CURRENCY_EXCHANGE, ex)
