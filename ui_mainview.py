# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainview.ui'
#
# Created: Sat Jul 30 22:53:41 2011
#      by: pyside-uic 0.2.9 running on PySide 1.0.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_mainForm(object):
    def setupUi(self, mainForm):
        mainForm.setObjectName("mainForm")
        mainForm.resize(924, 500)
        self.verticalLayout_2 = QtGui.QVBoxLayout(mainForm)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainWidget = QtGui.QWidget(mainForm)
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.mainWidget)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.mainWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.editItemCode = QtGui.QLineEdit(self.mainWidget)
        self.editItemCode.setFrame(True)
        self.editItemCode.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.editItemCode.setObjectName("editItemCode")
        self.horizontalLayout_2.addWidget(self.editItemCode)
        self.btnSearch = QtGui.QPushButton(self.mainWidget)
        self.btnSearch.setObjectName("btnSearch")
        self.horizontalLayout_2.addWidget(self.btnSearch)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.tableSale = QtGui.QTableWidget(self.mainWidget)
        self.tableSale.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableSale.sizePolicy().hasHeightForWidth())
        self.tableSale.setSizePolicy(sizePolicy)
        self.tableSale.setMinimumSize(QtCore.QSize(0, 150))
        self.tableSale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableSale.setStyleSheet("")
        self.tableSale.setFrameShape(QtGui.QFrame.StyledPanel)
        self.tableSale.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.tableSale.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableSale.setTabKeyNavigation(False)
        self.tableSale.setProperty("showDropIndicator", True)
        self.tableSale.setDragDropOverwriteMode(True)
        self.tableSale.setAlternatingRowColors(False)
        self.tableSale.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableSale.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableSale.setShowGrid(False)
        self.tableSale.setCornerButtonEnabled(False)
        self.tableSale.setObjectName("tableSale")
        self.tableSale.setColumnCount(5)
        self.tableSale.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableSale.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableSale.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableSale.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableSale.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableSale.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tableSale)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.group_PaymentClient = QtGui.QGroupBox(self.mainWidget)
        self.group_PaymentClient.setMinimumSize(QtCore.QSize(400, 0))
        self.group_PaymentClient.setMaximumSize(QtCore.QSize(16777215, 120))
        self.group_PaymentClient.setObjectName("group_PaymentClient")
        self.gridLayout_2 = QtGui.QGridLayout(self.group_PaymentClient)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkCash = QtGui.QRadioButton(self.group_PaymentClient)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkCash.sizePolicy().hasHeightForWidth())
        self.checkCash.setSizePolicy(sizePolicy)
        self.checkCash.setMaximumSize(QtCore.QSize(200, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/images/money.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkCash.setIcon(icon)
        self.checkCash.setChecked(True)
        self.checkCash.setObjectName("checkCash")
        self.verticalLayout_4.addWidget(self.checkCash)
        self.checkCard = QtGui.QRadioButton(self.group_PaymentClient)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkCard.sizePolicy().hasHeightForWidth())
        self.checkCard.setSizePolicy(sizePolicy)
        self.checkCard.setMinimumSize(QtCore.QSize(0, 0))
        self.checkCard.setMaximumSize(QtCore.QSize(200, 16777215))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/icons/images/card.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkCard.setIcon(icon1)
        self.checkCard.setObjectName("checkCard")
        self.verticalLayout_4.addWidget(self.checkCard)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.frame = QtGui.QFrame(self.group_PaymentClient)
        self.frame.setMinimumSize(QtCore.QSize(80, 80))
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblClientPhoto = QtGui.QLabel(self.frame)
        self.lblClientPhoto.setMinimumSize(QtCore.QSize(48, 48))
        self.lblClientPhoto.setMaximumSize(QtCore.QSize(48, 48))
        self.lblClientPhoto.setText("")
        self.lblClientPhoto.setObjectName("lblClientPhoto")
        self.verticalLayout_3.addWidget(self.lblClientPhoto)
        self.lblClientName = QtGui.QLabel(self.frame)
        self.lblClientName.setObjectName("lblClientName")
        self.verticalLayout_3.addWidget(self.lblClientName)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.group_PaymentClient)
        self.frameStatus = QtGui.QFrame(self.mainWidget)
        self.frameStatus.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frameStatus.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameStatus.setObjectName("frameStatus")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.frameStatus)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblStatus = QtGui.QLabel(self.frameStatus)
        self.lblStatus.setObjectName("lblStatus")
        self.horizontalLayout_3.addWidget(self.lblStatus)
        self.verticalLayout.addWidget(self.frameStatus)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupTotals = QtGui.QGroupBox(self.mainWidget)
        self.groupTotals.setTitle("")
        self.groupTotals.setObjectName("groupTotals")
        self.gridLayout = QtGui.QGridLayout(self.groupTotals)
        self.gridLayout.setObjectName("gridLayout")
        self.lblSubtotalPre = QtGui.QLabel(self.groupTotals)
        self.lblSubtotalPre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSubtotalPre.setObjectName("lblSubtotalPre")
        self.gridLayout.addWidget(self.lblSubtotalPre, 0, 0, 1, 1)
        self.lblSubtotal = QtGui.QLabel(self.groupTotals)
        self.lblSubtotal.setText("")
        self.lblSubtotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSubtotal.setObjectName("lblSubtotal")
        self.gridLayout.addWidget(self.lblSubtotal, 0, 1, 1, 1)
        self.lblSaleTaxesPre = QtGui.QLabel(self.groupTotals)
        self.lblSaleTaxesPre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSaleTaxesPre.setObjectName("lblSaleTaxesPre")
        self.gridLayout.addWidget(self.lblSaleTaxesPre, 1, 0, 1, 1)
        self.lblSaleTaxes = QtGui.QLabel(self.groupTotals)
        self.lblSaleTaxes.setText("")
        self.lblSaleTaxes.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblSaleTaxes.setObjectName("lblSaleTaxes")
        self.gridLayout.addWidget(self.lblSaleTaxes, 1, 1, 1, 1)
        self.labelTotalpre = QtGui.QLabel(self.groupTotals)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTotalpre.sizePolicy().hasHeightForWidth())
        self.labelTotalpre.setSizePolicy(sizePolicy)
        self.labelTotalpre.setMinimumSize(QtCore.QSize(180, 40))
        self.labelTotalpre.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelTotalpre.setFont(font)
        self.labelTotalpre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelTotalpre.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelTotalpre.setScaledContents(True)
        self.labelTotalpre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTotalpre.setIndent(0)
        self.labelTotalpre.setObjectName("labelTotalpre")
        self.gridLayout.addWidget(self.labelTotalpre, 2, 0, 1, 1)
        self.lblTotal = QtGui.QLabel(self.groupTotals)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTotal.sizePolicy().hasHeightForWidth())
        self.lblTotal.setSizePolicy(sizePolicy)
        self.lblTotal.setMinimumSize(QtCore.QSize(300, 40))
        self.lblTotal.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblTotal.setFont(font)
        self.lblTotal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTotal.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblTotal.setText("")
        self.lblTotal.setScaledContents(True)
        self.lblTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout.addWidget(self.lblTotal, 2, 1, 1, 1)
        self.labelChangepre = QtGui.QLabel(self.groupTotals)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelChangepre.sizePolicy().hasHeightForWidth())
        self.labelChangepre.setSizePolicy(sizePolicy)
        self.labelChangepre.setMinimumSize(QtCore.QSize(180, 40))
        self.labelChangepre.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelChangepre.setFont(font)
        self.labelChangepre.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelChangepre.setFrameShape(QtGui.QFrame.NoFrame)
        self.labelChangepre.setScaledContents(True)
        self.labelChangepre.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelChangepre.setMargin(0)
        self.labelChangepre.setIndent(0)
        self.labelChangepre.setObjectName("labelChangepre")
        self.gridLayout.addWidget(self.labelChangepre, 3, 0, 1, 1)
        self.lblChange = QtGui.QLabel(self.groupTotals)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChange.sizePolicy().hasHeightForWidth())
        self.lblChange.setSizePolicy(sizePolicy)
        self.lblChange.setMinimumSize(QtCore.QSize(300, 40))
        self.lblChange.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblChange.setFont(font)
        self.lblChange.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblChange.setFrameShape(QtGui.QFrame.NoFrame)
        self.lblChange.setText("")
        self.lblChange.setScaledContents(True)
        self.lblChange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblChange.setObjectName("lblChange")
        self.gridLayout.addWidget(self.lblChange, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupTotals)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.mainWidget)
        self.label.setBuddy(self.editItemCode)

        self.retranslateUi(mainForm)
        QtCore.QMetaObject.connectSlotsByName(mainForm)

    def retranslateUi(self, mainForm):
        mainForm.setWindowTitle(QtGui.QApplication.translate("mainForm", "lemonPy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("mainForm", "&Code:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSearch.setText(QtGui.QApplication.translate("mainForm", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSale.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("mainForm", "Qty", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSale.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("mainForm", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSale.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("mainForm", "Price", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSale.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("mainForm", "Discount", None, QtGui.QApplication.UnicodeUTF8))
        self.tableSale.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("mainForm", "Total", None, QtGui.QApplication.UnicodeUTF8))
        self.group_PaymentClient.setTitle(QtGui.QApplication.translate("mainForm", "Payment Options", None, QtGui.QApplication.UnicodeUTF8))
        self.checkCash.setText(QtGui.QApplication.translate("mainForm", "Ca&sh", None, QtGui.QApplication.UnicodeUTF8))
        self.checkCard.setText(QtGui.QApplication.translate("mainForm", "Credit/Debit", None, QtGui.QApplication.UnicodeUTF8))
        self.lblClientName.setText(QtGui.QApplication.translate("mainForm", "Client Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lblStatus.setText(QtGui.QApplication.translate("mainForm", "Cashier: Jonh Doe.  |  Mon 15, 20:10", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSubtotalPre.setText(QtGui.QApplication.translate("mainForm", "Subtotal:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSaleTaxesPre.setText(QtGui.QApplication.translate("mainForm", "Taxes:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTotalpre.setText(QtGui.QApplication.translate("mainForm", "Total:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelChangepre.setText(QtGui.QApplication.translate("mainForm", "Change:", None, QtGui.QApplication.UnicodeUTF8))

import mainview_rc