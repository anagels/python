#! /usr/local/bin/python
"""
    See LICENSE file for copyright and license details.					
"""

from sqlalchemy import Table, MetaData, Column, Integer, or_, and_
from sqlalchemy.types import VARCHAR
#from sqlalchemy.sql import exisst
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from decimal import Decimal
from datetime import datetime

from generic.modules.function import *
from generic.modules.function_sqlalchemy import row_to_dict
from generic.modules.messagehandler import *
from generic.modules.calculator_finance import *
from modules.constant import *
from modules.function import *
from meta import engine, Base
from database.mappings import *
from database.mappings_views import *


class DatabaseAccess():
    """
        Connecting to the database.
    """

    def __init__(self, config):
        """
            Initialize object.
        """
        try:
            self.config = config
            self.Session = sessionmaker(bind=engine)
            self.metadata = Base.metadata
            #self.map_tables()
            #self.map_views()
            self.tables = [x for x in self.metadata.tables.keys() if is_a_table(x)]
        except Exception as ex:
            print "Error in initialisation of DatabaseAccess: ", ex

    def get_accounts(self):
        """
            Get the accounts.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_ACCOUNT)
            for instance in query:
                values.append(
                    {
                        "name": instance.name,
                        "account_id": instance.account_id
                    }
                )
        except Exception as ex:
            print Error.GET_ACCOUNTS, ex
        finally:
            session.rollback()
            session = None
        return values

    def get_account_list(self):
        """
            Get the account_names in a list.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_ACCOUNT)
            for instance in query:
                values.append(instance.name)
        except Exception as ex:
            print Error.GET_ACCOUNT_LIST, ex
        finally:
            session.rollback()
            session = None
        return values

    def get_markets(self):
        """
            Get the market codes.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(
                    T_MARKET.active == 1)
            for instance in query:
                values.append(instance.code)
        except Exception as ex:
            print Error.GET_MARKETS, ex
        finally:
            session.rollback()
            session = None
        return values

    def get_commodity_names(self, code):
        """
            Get the commodity names.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(V_COMMODITY_INFO).filter(
                V_COMMODITY_INFO.market_code == code
            )
            for instance in query:
                values.append(instance.commodity_name)
        except Exception as ex:
            print "Error in get_commodity_names: ", ex
        finally:
            session.rollback()
            session = None
        return values

    def get_market_description(self, market):
        """
            Get the market description.
        """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_MARKET).filter(T_MARKET.code == market)
            for instance in query:
                value = instance.name
                break
        except Exception as ex:
            print Error.GET_MARKET_DESCRIPTION, ex
        finally:
            session.rollback()
            session = None
        return value

    def get_commodity_description(self, commodity):
        """
            Get the commodity description.
        """
        value = ''
        try:
            session = self.Session()
            query = session.query(T_COMMODITY).filter(
                T_COMMODITY.name == commodity
            )
            for instance in query:
                value = instance.description
                break
        except Exception as ex:
            print "Error in get_commodity_description: ", ex
        finally:
            session.rollback()
            session = None
        return value

    def get_commodity_info(self, commodity_name):
        """
            Get extra commodity info.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(
                T_COMMODITY.name.label("commodity_name"),
                T_MARKET.name.label("marketname"),
                T_MARKET.country
            ).join(
                T_MARKET,
                T_COMMODITY.market_id == T_MARKET.market_id
            ).filter(
                T_COMMODITY.name == commodity_name
            )
            for instance in query:
                values.append(instance.commodity_name)
                values.append(instance.marketname)
                values.append(instance.country)
        except Exception as ex:
            print Error.GET_COMMODITY_INFO, ex
        finally:
            session.rollback()
            session = None
        return values

    def get_currencies(self):
        """
            Get the currency codes.
        """
        values = []
        try:
            session = self.Session()
            query = session.query(T_CURRENCY)
            for instance in query:
                values.append(instance.code)
        except Exception as ex:
            print Error.GET_CURRENCIES, ex
        finally:
            session.rollback()
            session = None
        return values

    def trade_closed(self, trade_record):
        """
            Checks if a trade is closed.
        """
        return (
            (trade_record['date_buy'] != DEFAULT_DATE)
            and (trade_record['date_sell'] != DEFAULT_DATE)
            and (trade_record['shares_buy'] == trade_record['shares_sell'])
        )

    def get_long_flag_value(self, account_from, account_to, trade_record):
        """
            Are we long?
        """
        result = False
        if trade_record == {}:
            result = is_a_trading_account(account_from) and \
                deals_with_commodities(account_to)
            # NOTE: if account_from = broker and account_to is a commodity,
            # we know we are trading + buying
            # and that is going long if we don't have a trading record yet.
        else:
            result = (deals_with_commodities(account_from, account_to)
                and trade_record['date_buy'] != DEFAULT_DATE)
        return 1 if result else 0

    def get_win_flag_value(self, price_buy, price_sell):
        """
            Trade finished... did we win?
        """
        result = (price_buy < price_sell)
        return 1 if result else 0

    def write_to_database(self, statements):
        """
            Writes the records of a given statements list to the database.
        """
        try:
            if statements != []:
                #insert
                statements_insert = self.assemble_statement_list_insert(
                        statements, StatementType.INSERT)
                self.write_statement_list_insert(
                        statements_insert, statements.table)
                #update
                statements_update = self.assemble_statement_list_update(
                        statements, StatementType.UPDATE)
                print "test: statements_update = ", statements_update
                self.write_statement_list_update(
                        statements_update, statements.table)
                #delete
                statements_delete = self.assemble_statement_list_delete(
                        statements, StatementType.DELETE)
                self.write_statement_list_delete(
                        statements_delete, statements.table)
        except Exception as ex:
            print Error.WRITE_TO_DATABASE_SESSION, ex

    def write_statement_list_insert(self, final_statements, table):
        """
            Commit the insert statements to database.
        """
        session = self.Session()
        try:
            if final_statements != []:
                #NOTE: The below 3 lines are this one-liner in python3:
                #print(table_name, end=': ')
                #splitnames = table.__name__.split(':')
                #for name in splitnames:
                #    print name
                session.add_all(final_statements)
                session.commit()
                # TODO: {0} in python2.7?
                print "{0} records added.".format(str(len(final_statements)))
                print ''
        except Exception as ex:
            print Error.INSERT_DATABASE, ex
        finally:
            session.rollback()
            session = None

    def write_statement_list_update(self, final_statements, table):
        """
            Execute the update statements on the database.
        """
        # TODO: this code needs the update instruction I've written somewhere
        #in databaseaccess.py
        #=> session.query(Supplier).filter_by(id=2).update({"name": u"Mayowa"})
        session = self.Session()
        try:
            #import pdb; pdb.set_trace()
            if final_statements != []:
                #session.add_all(final_statements)
                #session.commit()
                for statement in final_statements:
                    print 'test:', statement
                    # TODO: make trade_id a var? Is that possible?
                    session.query(table).filter_by(
                            trade_id=statement[0]).update(statement[1])
                    print 'test: after query'
                # TODO: commit/flush code in for or outside?
                session.commit()
                print 'test: after commit'
                print "{0} records updated.".format(str(len(final_statements)))
                print ''
        except Exception as ex:
            print Error.UPDATE_DATABASE, ex
        finally:
            session.rollback()
            session = None

    def write_statement_list_delete(self, final_statements, table):
        """
            Write the insert statements to database.
        """
        # TODO: finish this later. Low priority!
        pass

    def assemble_statement_list_insert(self, statements,
        insupdel=StatementType.INSERT):
        """
            Creates list of TABLE_NAME(..., ..., ...) records
            from new statements, that we can use to insert at once.
        """
        # TODO: find a way to refactor this piece of crap code.
        result = []
        inner_part_list = statements.get_statement_list(insupdel)
        if statements.table == T_CURRENCY_EXCHANGE:
            for record in inner_part_list:
                result.append(T_CURRENCY_EXCHANGE(
                    record['currency_exchange_id'],
                    record['currency_from_id'],
                    record['currency_to_id'],
                    record['exchange_rate'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table == T_RATE:
            for record in inner_part_list:
                result.append(T_RATE(
                    record['rate_id'],
                    record['commission'],
                    record['tax'],
                    record['automatic_flag'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table == T_FINANCE:
            for record in inner_part_list:
                result.append(T_FINANCE(
                    record['finance_id'],
                    record['date'],
                    record['year'],
                    record['month'],
                    record['day'],
                    record['account_from_id'],
                    record['account_to_id'],
                    record['amount'],
                    record['comment'],
                    record['currency_exchange_id'],
                    record['rate_id'],
                    record['active'],
                    record['date_created'],
                    record['date_modified']))
        elif statements.table == T_TRADE:
            for record in inner_part_list:
                result.append(T_TRADE(
                    record['trade_id'],
                    record['market_id'],
                    record['commodity_id'],
                    record['date_buy'],
                    record['year_buy'],
                    record['month_buy'],
                    record['day_buy'],
                    record['date_sell'],
                    record['year_sell'],
                    record['month_sell'],
                    record['day_sell'],
                    record['long_flag'],
                    record['price_buy'],
                    record['price_buy_orig'],
                    record['price_sell'],
                    record['price_sell_orig'],
                    record['shares_buy'],
                    record['shares_sell'],
                    record['commission_buy'],
                    record['commission_sell'],
                    record['tax_buy'],
                    record['tax_sell'],
                    record['amount_buy'],
                    record['amount_sell'],
                    record['amount_buy_simple'],
                    record['amount_sell_simple'],
                    record['risk_input'],
                    record['risk_input_percent'],
                    record['risk_initial'],
                    record['risk_initial_percent'],
                    record['risk_actual'],
                    record['risk_actual_percent'],
                    record['cost_total'],
                    record['cost_other'],
                    record['stoploss'],
                    record['stoploss_orig'],
                    record['profit_loss'],
                    record['profit_loss_orig'],
                    record['profit_loss_total'],
                    record['profit_loss_total_percent'],
                    record['r_multiple'],
                    record['win_flag'],
                    record['id_buy'],
                    record['id_sell'],
                    record['drawdown_id'],
                    record['pool_at_start'],
                    record['date_expiration'],
                    record['expired_flag'],
                    record['spread'],
                    record['active'],
                    record['date_created'],
                    record['date_modified']))
        return result

    def assemble_statement_list_update(self, statements,
        insupdel=StatementType.UPDATE):
        """
            Creates list of update records from statements,
            that we can use to update.
        """
        result = []
        #import pdb; pdb.set_trace()
        inner_part_list = statements.get_statement_list(insupdel)
        for record in inner_part_list:
            if statements.table == T_TRADE:
                var_id = record['trade_id']
            else:
                var_id = -1
            result.append(
                [
                    var_id,
                    {
                        "market_id": record["market_id"],
                        "commodity_id": record["commodity_id"],
                        "date_buy": record["date_buy"],
                        "year_buy": record["year_buy"],
                        "month_buy": record["month_buy"],
                        "day_buy": record["day_buy"],
                        "date_sell": record["date_sell"],
                        "year_sell": record["year_sell"],
                        "month_sell": record["month_sell"],
                        "day_sell": record["day_sell"],
                        "long_flag": record["long_flag"],
                        "price_buy": record["price_buy"],
                        "price_buy_orig": record["price_buy_orig"],
                        "price_sell": record["price_sell"],
                        "price_sell_orig": record["price_sell_orig"],
                        "shares_buy": record["shares_buy"],
                        "shares_sell": record["shares_sell"],
                        "commission_buy": record["commission_buy"],
                        "commission_sell": record["commission_sell"],
                        "tax_buy": record["tax_buy"],
                        "tax_sell": record["tax_sell"],
                        "amount_buy": record["amount_buy"],
                        "amount_sell": record["amount_sell"],
                        "amount_buy_simple": record["amount_buy_simple"],
                        "amount_sell_simple": record["amount_sell_simple"],
                        "risk_input": record["risk_input"],
                        "risk_input_percent": record["risk_input_percent"],
                        "risk_initial": record["risk_initial"],
                        "risk_initial_percent": record["risk_initial_percent"],
                        "risk_actual": record["risk_actual"],
                        "risk_actual_percent": record["risk_actual_percent"],
                        "cost_total": record["cost_total"],
                        "cost_other": record["cost_other"],
                        "stoploss": record["stoploss"],
                        "stoploss_orig": record["stoploss_orig"],
                        "profit_loss": record["profit_loss"],
                        "profit_loss_orig": record["profit_loss_orig"],
                        "profit_loss_total": record["profit_loss_total"],
                        "profit_loss_total_percent":
                            record["profit_loss_total_percent"],
                        "r_multiple": record["r_multiple"],
                        "win_flag": record["win_flag"],
                        "id_buy": record["id_buy"],
                        "id_sell": record["id_sell"],
                        "drawdown_id": record["drawdown_id"],
                        "pool_at_start": record["pool_at_start"],
                        "date_expiration": record["date_expiration"],
                        "expired_flag": record["expired_flag"],
                        "spread": record["spread"],
                        "active": record["active"],
                        "date_created": record["date_created"],
                        "date_modified": record["date_modified"]
                    }
                ]
            )
        return result

    def assemble_statement_list_delete(self, statements,
        insupdel=StatementType.DELETE):
        """
            Creates list of from delete statements,
            that we can use to delete at once.
        """
        #NOTE: deleting is not used, because we don't need it.
        # Deleting is done on the table object rows, before pressing execute.
        # When using the app, you need to make sure everything is ok before
        # you press execute.
        return statements.get_statement_list(insupdel)

    def export_records(self, name):
        """
            Return the records from the table or view, defined by name.
        """
        records = None
        session = self.Session()
        try:
            records = session.query(name).all()
        except Exception as ex:
            print "Error in export_records: ", ex
        finally:
            session.rollback()
            session = None
        return records

    def account_id_from_account_name(self,
        account_name, from_account=True):
        """
            Get the account_id from an account.
        """
        result = - 1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            # Get account id, based on account name
            # but first check if the account already exists
            # in T_ACCOUNT. If not, add it to the t_account table.
            obj = session.query(T_ACCOUNT).filter_by(
                name=account_name
            ).first() is not None
            if not obj:
                if from_account:
                    description_list = self.gui.get_account_from().split(':')
                    description = description_list[len(descpription_list) - 1]
                else:
                    description = self.gui.get_account_to().split(':')
                    description = description_list[len(descpription_list) - 1]
                session.add(T_ACCOUNT(
                    account_name,
                    description,
                    date_created,
                    date_modified)
                )
                session.commit()
                for instance in session.query(
                    func.max(T_ACCOUNT.account_id).label('account_id')
                ):
                    result = instance.account_id
            else:
                for instance in session.query(T_ACCOUNT).filter_by(
                    name=account_name
                ):
                    result = str(instance.account_id)
        except Exception as ex:
            print Error.ACCOUNT_ID_FROM_ACCOUNT, ex
        finally:
            session.rollback()
            session = None
        return result

    def commodity_id_from_commodity_name(self, commodity_name, market_id):
        """
            Get the commodity_id from T_COMMODITY.
        """
        result = -1
        session = self.Session()
        try:
            # Get commodity_id, based on commodity_name
            # but first check if the commodity_name already exists
            # in T_COMMODITY. If not, add it to the table.
            first_obj = session.query(V_COMMODITY_INFO).filter_by(
                commodity_name=commodity_name,
                market_id=market_id).first()
            if first_obj is not None:
                result = str(first_obj.commodity_id)
        except Exception as ex:
            print "Error retrieving commodity_id: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def market_id_from_market(self, code):
        """
            Get the market_id from T_MARKET.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            obj = session.query(T_MARKET).filter_by(
                code=code
            ).first() is not None
            if not obj:
                # NOTE: this code means that when new market records
                # have been added during normal usage, a new
                # uninstall/install/import will not be able
                # to fill in the name and country of the market.
                # For now, assume no new ones are added. If there are,
                # add them to the init_tables script!
                # TODO: add extra field in gui for the country code
                # and country name + add this to the input_fields.
                # This way, we can also add new markets.
                # But: perhaps this makes the input too complex and a new
                # button with a dialog window behind it is needed?
                session.add(T_MARKET(
                    None,
                    code,
                    'TBD',
                    '??',
                    1,
                    date_created,
                    date_modified)
                )
                session.commit()
                for instance in session.query(
                    func.max(T_MARKET.market_id).label('market_id')
                ):
                    result = instance.market_id
            else:
                for instance in session.query(T_MARKET).filter_by(code=code):
                    result = str(instance.market_id)
        except Exception as ex:
            print "Error retrieving market_id: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def account_name_from_account_id(self, account_id):
        """
            Get the account_name for a given account_id
            from the T_ACCOUNT table.
        """
        result = ''
        session = self.Session()
        try:
            for instance in session.query(V_ACCOUNT_NAME).filter_by(
                account_id=account_id
            ):
                result = instance.name
        except Exception as ex:
            print "Error retrieving accountname from account_id: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def currency_id_from_currency(self, currency):
        """
            Get the currency_id from a currency string (e.g.'USD').
        """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_CURRENCY).filter_by(
                code=currency
            ).first()
            if first_obj is not None:
                result = str(first_obj.currency_id)
            else:
                raise Exception("Error: currency {0} not found!" +
                " -1 used as a currency_id.".format(currency))
        except Exception as ex:
            print Error.ACCOUNT_ID_FROM_ACCOUNT, ex
        finally:
            session.rollback()
            session = None
        return result

    def get_latest_rate_id(self):
        """
            Gets the latest rate_id.
        """
        result = -1
        session = self.Session()
        try:
            first_obj = session.query(T_RATE).order_by(
                T_RATE.rate_id.desc()
            ).first()
            if first_obj is not None:
                result = first_obj.rate_id
            else:
                # We don't have one yet, so by making the last one 0,
                # a get_latest_rate_id() + 1 would become 1
                result = 0
        except Exception as ex:
            print "Error retrieving latest rate_id from T_RATE: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def get_parameter_value(self, parameter_id):
        """
            Function to get the value that belongs to the given parameter.
        """
        result = DEFAULT_DECIMAL
        session = self.Session()
        try:
            for instance in session.query(T_PARAMETER).filter_by(
                    parameter_id=parameter_id):
                result = str(instance.value)
        except Exception as ex:
            print "Error retrieving parameter value: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def first_currency_exchange_id_from_latest(self):
        """
            Gets the first currency_exchange_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            currency_exchange_created = self.get_latest_date_created(
                Table.CURRENCY_EXCHANGE)
            first_obj = session.query(T_CURRENCY_EXCHANGE).filter_by(
                    date_created=currency_exchange_created).first()
            if first_obj is not None:
                result = first_obj.currency_exchange_id
        except Exception as ex:
            print "Error in first_currency_id_from_latest: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def first_rate_id_from_latest(self):
        """
            Gets the first rate_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            rate_created = self.get_latest_date_created(Table.RATE)
            obj = session.query(T_RATE).filter_by(date_created=rate_created)
            for instance in obj:
                result = instance.rate_id
        except Exception as ex:
            print "Error in first_rate_id_from_latest: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def first_finance_id_from_latest(self):
        """
            Gets the first finance_id from the latest update
            block, which is determined by examining the date_created column.
        """
        result = -1
        session = self.Session()
        try:
            finance_created = self.get_latest_date_created(Table.FINANCE)
            obj = session.query(T_FINANCE).filter_by(
                date_created=finance_created)
            for instance in obj:
                result = instance.finance_id
        except Exception as ex:
            print "Error in first_finance_id_from_latest: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def get_latest_date_created(self, tablename):
        """
            Get's the latest date_created value that was added.
        """
        result = current_date()
        session = self.Session()
        try:
            if tablename == Table.FINANCE:
                first_obj = session.query(T_FINANCE).order_by(
                    T_FINANCE.finance_id.desc()).first()
            elif tablename == Table.RATE:
                first_obj = session.query(T_RATE).order_by(
                    T_RATE.rate_id.desc()).first()
            elif tablename == Table.CURRENCY_EXCHANGE:
                first_obj = session.query(T_CURRENCY_EXCHANGE).order_by(
                    T_CURRENCY_EXCHANGE.currency_exchange_id.desc()).first()
            else:
                first_obj = None
            if first_obj is not None:
                result = first_obj.date_created
        except Exception as ex:
            print 'Error in get_latest_date_created for table', tablename,
            ':', ex
        finally:
            session.rollback()
            session = None
        return result

    def get_finance_record(self, afinance_id):
        """
            Gets the finance_record with the given finance_id.
        """
        result = {}
        session = self.Session()
        try:
            first_obj = session.query(T_FINANCE).filter(T_FINANCE.finance_id ==
                    afinance_id).first()
            if first_obj is not None:
                result = first_obj.__dict__
        except Exception as ex:
            print "Error in get_finance_record: ", ex
        finally:
            session.rollback()
            session = None
            return result

    def get_rep_check_total(self, check_totals):
        """
            Returns a string with the totals per account.
        """
        result = ""
        i = 0
        for entry in check_totals:
            if i == 0:
                result = entry[0] + \
                    '|' + str(entry[1])
            else:
                result = result + ' ' + entry[0] + \
                '|' + str(entry[1])
            i = i + 1
        return result

    def get_rep_check_totals(self):
        """
            Returns a list with the account name and totals.
        """
        pass
        #values = []
        #session = self.Session()
        #try:
        #    #obj = session.query(V_REP_CHECK_TOTAL)
        #    #for instance in obj:
        #    #        values.append([instance.account_name,
        #    #            instance.account_total])
        #except Exception as ex:
        #    print "Error in get_rep_check_totals: ", ex
        #finally:
        #    session.rollback()
        #    session = None
        #return values

    def new_drawdown_record(self):
        """
            Creates a new record in T_DRAWDOWN with a default value of 0.
        """
        result = -1
        session = self.Session()
        try:
            date_created = current_date()
            date_modified = current_date()
            session.add(T_DRAWDOWN(None, 0, 0, date_created, date_modified))
            session.commit()
            for instance in session.query(
                    func.max(T_DRAWDOWN.drawdown_id).label(
                        'drawdown_id')):
                result = instance.drawdown_id
        except Exception as ex:
            print Error.NEW_DRAWDOWN_RECORD, ex
        finally:
            session.rollback()
            session = None
        return result

    def get_pool(self):
        """
            Gets the pool available for trading.
        """
        result = DEFAULT_DECIMAL
        session = self.Session()
        try:
            first_obj = session.query(func.sum(T_FINANCE.amount).label('total')
                    ).filter_by(account_from_id=TRADING_ACCOUNT_ID).first()
            if first_obj.total is not None:
                result = Decimal(first_obj.total)
        except Exception as ex:
            print "Error in get_pool: ", ex
        finally:
            session.rollback()
            session = None
        return result

    def get_specific_finance_record(self, date, account_id, account_from_id,
            account_to_id, amount, comment, commodity_id, shares, price,
            tax, commission):
        """
           Looks for a finance record with the given parameters.
        """
        try:
            session = self.Session()
            result = session.query(T_FINANCE).filter_by(
                            date=date,
                            account_id=account_id,
                            account_from_id=account_from_id,
                            account_to_id=account_to_id,
                            amount=amount,
                            comment=comment,
                            commodity_id=commodity_id,
                            shares=shares,
                            price=price,
                            tax=tax,
                            commission=commission,
                            active=1
                            ).first()
        except Exception as ex:
            print Error.GET_SPECIFIC_FINANCE_RECORD, ex
            session.rollback()
            result = None
        finally:
            session = None
            return result

    def open_trade_position(self, market_id, commodity_id, table_class):
        """
            Check if this trade or investment has already started
            and return it's trade_id (or investment_id).
            Retuns:
            when not found -> -1
            when found -> the id
        """
        result = -1
        try:
            session = self.Session()
            #NOTE: id_buy or id_sell must be -1
            # but both can't be filled in (= finished trade)
            first_obj = session.query(table_class).filter(
                    table_class.market_id == market_id,
                    table_class.commodity_id == commodity_id,
                    table_class.active == 1).filter(
                        or_(
                            table_class.id_buy == -1,
                            table_class.id_sell == -1
                        )).filter(
                            table_class.id_buy != table_class.id_sell
                       ).first()
            if first_obj is not None:
                result = first_obj.trade_id
        except Exception as ex:
            print Error.INVADE_ALREADY_STARTED, ex
        finally:
            session.rollback()
            session = None
            return result

    def get_trade_record(self, atrade_id):
        """
            Gets the trade_record with the given trade_id.
        """
        # TODO: this code can only deal with buying all and selling all for now!
        result = {}
        session = self.Session()
        try:
            first_obj = session.query(T_TRADE).filter(
                        T_TRADE.trade_id == atrade_id,
                        ).first()
            if first_obj is not None:
                result = row_to_dict(first_obj)
        except Exception as ex:
            print "Error in get_trade_record: ", ex
        finally:
            session.rollback()
            session = None
            return result

    def get_tick_size_from_commodity_id(self, commodity_id):
        """
            Get the tick size for a given commodity.
        """
        result = DEFAULT_DECIMAL
        try:
            session = self.Session()
            first_obj = session.query(T_TRADE.spread).filter_by(
                commodity_id=commodity_id).first()
            if first_obj is not None:
                result = Decimal(first_obj.tick_size)
        except Exception as ex:
            print "Error  in get_tick_size_from_commodity_id: ", ex
        finally:
            session.rollback()
            session = None
            return result

    def get_tick_value_from_commodity_id(self, commodity_id):
        """
            Get the tick value for a given commodity.
        """
        result = DEFAULT_DECIMAL
        try:
            session = self.Session()
            first_obj = session.query(T_TRADE.spread).filter_by(
                commodity_id=commodity_id).first()
            if first_obj is not None:
                result = Decimal(first_obj.tick_value)
        except Exception as ex:
            print "Error  in get_tick_value_from_commodity_id: ", ex
        finally:
            session.rollback()
            session = None
            return result

    def get_margin_pool(self):
        """
            Get margin to use on the pool.
        """
        return Decimal(self.get_parameter_value(1))
