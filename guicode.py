# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lisagui.ui'
#
# Created: Wed Jul 27 11:11:03 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        frm_main.setObjectName(_fromUtf8("frm_main"))
        frm_main.setEnabled(True)
        frm_main.resize(1000, 615)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frm_main.sizePolicy().hasHeightForWidth())
        frm_main.setSizePolicy(sizePolicy)
        frm_main.setMinimumSize(QtCore.QSize(1000, 600))
        frm_main.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        frm_main.setFont(font)
        self.layoutWidget = QtGui.QWidget(frm_main)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 2, 981, 611))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.cmb_account = QtGui.QComboBox(self.layoutWidget)
        self.cmb_account.setObjectName(_fromUtf8("cmb_account"))
        self.gridLayout_8.addWidget(self.cmb_account, 0, 2, 1, 1)
        self.lbl_account = QtGui.QLabel(self.layoutWidget)
        self.lbl_account.setObjectName(_fromUtf8("lbl_account"))
        self.gridLayout_8.addWidget(self.lbl_account, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_add = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_add.setFont(font)
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.horizontalLayout_2.addWidget(self.btn_add)
        self.btn_clear = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_clear.setFont(font)
        self.btn_clear.setObjectName(_fromUtf8("btn_clear"))
        self.horizontalLayout_2.addWidget(self.btn_clear)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_new_product = QtGui.QPushButton(self.layoutWidget)
        self.btn_new_product.setObjectName(_fromUtf8("btn_new_product"))
        self.horizontalLayout_2.addWidget(self.btn_new_product)
        self.btn_new_stock = QtGui.QPushButton(self.layoutWidget)
        self.btn_new_stock.setObjectName(_fromUtf8("btn_new_stock"))
        self.horizontalLayout_2.addWidget(self.btn_new_stock)
        self.btn_new_marketcode = QtGui.QPushButton(self.layoutWidget)
        self.btn_new_marketcode.setObjectName(_fromUtf8("btn_new_marketcode"))
        self.horizontalLayout_2.addWidget(self.btn_new_marketcode)
        self.btn_new_account = QtGui.QPushButton(self.layoutWidget)
        self.btn_new_account.setObjectName(_fromUtf8("btn_new_account"))
        self.horizontalLayout_2.addWidget(self.btn_new_account)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_execute = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_execute.setFont(font)
        self.btn_execute.setObjectName(_fromUtf8("btn_execute"))
        self.horizontalLayout_2.addWidget(self.btn_execute)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.btn_exit = QtGui.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.horizontalLayout_2.addWidget(self.btn_exit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lbl_date = QtGui.QLabel(self.layoutWidget)
        self.lbl_date.setObjectName(_fromUtf8("lbl_date"))
        self.gridLayout_4.addWidget(self.lbl_date, 0, 0, 1, 1)
        self.dt_date = QtGui.QDateEdit(self.layoutWidget)
        self.dt_date.setCalendarPopup(True)
        self.dt_date.setObjectName(_fromUtf8("dt_date"))
        self.gridLayout_4.addWidget(self.dt_date, 0, 1, 1, 1)
        self.lbl_product = QtGui.QLabel(self.layoutWidget)
        self.lbl_product.setObjectName(_fromUtf8("lbl_product"))
        self.gridLayout_4.addWidget(self.lbl_product, 0, 2, 1, 1)
        self.cmb_product = QtGui.QComboBox(self.layoutWidget)
        self.cmb_product.setObjectName(_fromUtf8("cmb_product"))
        self.gridLayout_4.addWidget(self.cmb_product, 0, 3, 1, 1)
        self.lbl_amount = QtGui.QLabel(self.layoutWidget)
        self.lbl_amount.setObjectName(_fromUtf8("lbl_amount"))
        self.gridLayout_4.addWidget(self.lbl_amount, 0, 6, 1, 1)
        self.spn_amount = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.spn_amount.setLocale(QtCore.QLocale(QtCore.QLocale.C, QtCore.QLocale.AnyCountry))
        self.spn_amount.setMaximum(999999.99)
        self.spn_amount.setProperty(_fromUtf8("value"), 0.0)
        self.spn_amount.setObjectName(_fromUtf8("spn_amount"))
        self.gridLayout_4.addWidget(self.spn_amount, 0, 7, 1, 1)
        self.lbl_comment = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.lbl_comment.setFont(font)
        self.lbl_comment.setObjectName(_fromUtf8("lbl_comment"))
        self.gridLayout_4.addWidget(self.lbl_comment, 0, 8, 1, 1)
        self.txt_comment = QtGui.QLineEdit(self.layoutWidget)
        self.txt_comment.setEnabled(True)
        self.txt_comment.setObjectName(_fromUtf8("txt_comment"))
        self.gridLayout_4.addWidget(self.txt_comment, 0, 9, 1, 1)
        self.cmb_object = QtGui.QComboBox(self.layoutWidget)
        self.cmb_object.setObjectName(_fromUtf8("cmb_object"))
        self.gridLayout_4.addWidget(self.cmb_object, 0, 5, 1, 1)
        self.lbl_object = QtGui.QLabel(self.layoutWidget)
        self.lbl_object.setObjectName(_fromUtf8("lbl_object"))
        self.gridLayout_4.addWidget(self.lbl_object, 0, 4, 1, 1)
        self.gridLayout_4.setColumnStretch(3, 2)
        self.gridLayout_4.setColumnStretch(7, 1)
        self.gridLayout_4.setColumnStretch(9, 2)
        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tab_details = QtGui.QTabWidget(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.tab_details.setFont(font)
        self.tab_details.setTabPosition(QtGui.QTabWidget.North)
        self.tab_details.setTabShape(QtGui.QTabWidget.Rounded)
        self.tab_details.setElideMode(QtCore.Qt.ElideNone)
        self.tab_details.setUsesScrollButtons(True)
        self.tab_details.setDocumentMode(True)
        self.tab_details.setObjectName(_fromUtf8("tab_details"))
        self.tab_page_summary = QtGui.QWidget()
        self.tab_page_summary.setObjectName(_fromUtf8("tab_page_summary"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_page_summary)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 971, 381))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.glo_summary = QtGui.QGridLayout(self.layoutWidget1)
        self.glo_summary.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.glo_summary.setMargin(0)
        self.glo_summary.setObjectName(_fromUtf8("glo_summary"))
        self.tbl_summary = QtGui.QTableWidget(self.layoutWidget1)
        self.tbl_summary.setObjectName(_fromUtf8("tbl_summary"))
        self.tbl_summary.setColumnCount(0)
        self.tbl_summary.setRowCount(0)
        self.glo_summary.addWidget(self.tbl_summary, 0, 0, 1, 1)
        self.tab_details.addTab(self.tab_page_summary, _fromUtf8(""))
        self.tab_page_stocks = QtGui.QWidget()
        self.tab_page_stocks.setObjectName(_fromUtf8("tab_page_stocks"))
        self.gridLayoutWidget_5 = QtGui.QWidget(self.tab_page_stocks)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 20, 251, 151))
        self.gridLayoutWidget_5.setObjectName(_fromUtf8("gridLayoutWidget_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.cmb_marketcode = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.cmb_marketcode.setObjectName(_fromUtf8("cmb_marketcode"))
        self.gridLayout_5.addWidget(self.cmb_marketcode, 0, 4, 1, 1)
        self.spn_price = QtGui.QDoubleSpinBox(self.gridLayoutWidget_5)
        self.spn_price.setMaximum(999999.99)
        self.spn_price.setObjectName(_fromUtf8("spn_price"))
        self.gridLayout_5.addWidget(self.spn_price, 3, 4, 1, 1)
        self.spn_quantity = QtGui.QSpinBox(self.gridLayoutWidget_5)
        self.spn_quantity.setMaximum(999999)
        self.spn_quantity.setObjectName(_fromUtf8("spn_quantity"))
        self.gridLayout_5.addWidget(self.spn_quantity, 2, 4, 1, 1)
        self.lbl_marketcode = QtGui.QLabel(self.gridLayoutWidget_5)
        self.lbl_marketcode.setObjectName(_fromUtf8("lbl_marketcode"))
        self.gridLayout_5.addWidget(self.lbl_marketcode, 0, 0, 1, 1)
        self.lbl_stockname = QtGui.QLabel(self.gridLayoutWidget_5)
        self.lbl_stockname.setObjectName(_fromUtf8("lbl_stockname"))
        self.gridLayout_5.addWidget(self.lbl_stockname, 1, 0, 1, 1)
        self.lbl_quantity = QtGui.QLabel(self.gridLayoutWidget_5)
        self.lbl_quantity.setObjectName(_fromUtf8("lbl_quantity"))
        self.gridLayout_5.addWidget(self.lbl_quantity, 2, 0, 1, 1)
        self.lbl_price = QtGui.QLabel(self.gridLayoutWidget_5)
        self.lbl_price.setObjectName(_fromUtf8("lbl_price"))
        self.gridLayout_5.addWidget(self.lbl_price, 3, 0, 1, 1)
        self.cmb_stockname = QtGui.QComboBox(self.gridLayoutWidget_5)
        self.cmb_stockname.setObjectName(_fromUtf8("cmb_stockname"))
        self.gridLayout_5.addWidget(self.cmb_stockname, 1, 4, 1, 1)
        self.tab_details.addTab(self.tab_page_stocks, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tab_details)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lbl_infofinance = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.lbl_infofinance.setFont(font)
        self.lbl_infofinance.setObjectName(_fromUtf8("lbl_infofinance"))
        self.horizontalLayout.addWidget(self.lbl_infofinance)
        self.lbl_infodetails = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Envy Code R"))
        self.lbl_infodetails.setFont(font)
        self.lbl_infodetails.setObjectName(_fromUtf8("lbl_infodetails"))
        self.horizontalLayout.addWidget(self.lbl_infodetails)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(frm_main)
        self.tab_details.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frm_main)

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QtGui.QApplication.translate("frm_main", "LISA", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_account.setText(QtGui.QApplication.translate("frm_main", "Account", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setText(QtGui.QApplication.translate("frm_main", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_clear.setText(QtGui.QApplication.translate("frm_main", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_product.setText(QtGui.QApplication.translate("frm_main", "New Product", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_stock.setText(QtGui.QApplication.translate("frm_main", "New Stock", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_marketcode.setText(QtGui.QApplication.translate("frm_main", "New Market Code", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_new_account.setText(QtGui.QApplication.translate("frm_main", "New Account", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_execute.setText(QtGui.QApplication.translate("frm_main", "Execute", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_exit.setText(QtGui.QApplication.translate("frm_main", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_date.setText(QtGui.QApplication.translate("frm_main", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.dt_date.setDisplayFormat(QtGui.QApplication.translate("frm_main", "yyyy-MM-dd", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_product.setText(QtGui.QApplication.translate("frm_main", "Product", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_amount.setText(QtGui.QApplication.translate("frm_main", "Amount", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_comment.setText(QtGui.QApplication.translate("frm_main", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_object.setText(QtGui.QApplication.translate("frm_main", "Object", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_details.setTabText(self.tab_details.indexOf(self.tab_page_summary), QtGui.QApplication.translate("frm_main", "Summary", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_marketcode.setText(QtGui.QApplication.translate("frm_main", "Market code", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_stockname.setText(QtGui.QApplication.translate("frm_main", "Stock name", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_quantity.setText(QtGui.QApplication.translate("frm_main", "Quantity", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_price.setText(QtGui.QApplication.translate("frm_main", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_details.setTabText(self.tab_details.indexOf(self.tab_page_stocks), QtGui.QApplication.translate("frm_main", "Stocks", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_infofinance.setText(QtGui.QApplication.translate("frm_main", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.lbl_infodetails.setText(QtGui.QApplication.translate("frm_main", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

