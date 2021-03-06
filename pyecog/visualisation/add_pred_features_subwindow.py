# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_prediction_features.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_make_features(object):
    def setupUi(self, make_features):
        make_features.setObjectName("make_features")
        make_features.resize(790, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(make_features.sizePolicy().hasHeightForWidth())
        make_features.setSizePolicy(sizePolicy)
        make_features.setMinimumSize(QtCore.QSize(790, 0))
        make_features.setMaximumSize(QtCore.QSize(16777215, 600))
        self.gridLayout = QtWidgets.QGridLayout(make_features)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 32))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.run_peakdet_checkBox = QtWidgets.QCheckBox(make_features)
        self.run_peakdet_checkBox.setText("")
        self.run_peakdet_checkBox.setObjectName("run_peakdet_checkBox")
        self.gridLayout_2.addWidget(self.run_peakdet_checkBox, 3, 1, 1, 1)
        self.h5_display = QtWidgets.QLineEdit(make_features)
        self.h5_display.setMinimumSize(QtCore.QSize(300, 0))
        self.h5_display.setObjectName("h5_display")
        self.gridLayout_2.addWidget(self.h5_display, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 32))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 32))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.chunk_len_box = QtWidgets.QLineEdit(make_features)
        self.chunk_len_box.setObjectName("chunk_len_box")
        self.gridLayout_2.addWidget(self.chunk_len_box, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 32))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.cores_to_use = QtWidgets.QLineEdit(make_features)
        self.cores_to_use.setObjectName("cores_to_use")
        self.gridLayout_2.addWidget(self.cores_to_use, 2, 1, 1, 1)
        self.set_h5_folder = QtWidgets.QPushButton(make_features)
        self.set_h5_folder.setEnabled(True)
        self.set_h5_folder.setObjectName("set_h5_folder")
        self.gridLayout_2.addWidget(self.set_h5_folder, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.extract_features_button = QtWidgets.QPushButton(make_features)
        self.extract_features_button.setObjectName("extract_features_button")
        self.gridLayout.addWidget(self.extract_features_button, 2, 0, 1, 1)
        self.hidden_label = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hidden_label.sizePolicy().hasHeightForWidth())
        self.hidden_label.setSizePolicy(sizePolicy)
        self.hidden_label.setMinimumSize(QtCore.QSize(600, 0))
        self.hidden_label.setText("")
        self.hidden_label.setObjectName("hidden_label")
        self.gridLayout.addWidget(self.hidden_label, 3, 0, 1, 1)
        self.progress_bar_label = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_bar_label.sizePolicy().hasHeightForWidth())
        self.progress_bar_label.setSizePolicy(sizePolicy)
        self.progress_bar_label.setMinimumSize(QtCore.QSize(0, 32))
        self.progress_bar_label.setObjectName("progress_bar_label")
        self.gridLayout.addWidget(self.progress_bar_label, 4, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(make_features)
        self.progressBar.setMinimumSize(QtCore.QSize(700, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 1)
        self.logpath_dsplay = QtWidgets.QLabel(make_features)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logpath_dsplay.sizePolicy().hasHeightForWidth())
        self.logpath_dsplay.setSizePolicy(sizePolicy)
        self.logpath_dsplay.setObjectName("logpath_dsplay")
        self.gridLayout.addWidget(self.logpath_dsplay, 6, 0, 1, 1)

        self.retranslateUi(make_features)
        QtCore.QMetaObject.connectSlotsByName(make_features)

    def retranslateUi(self, make_features):
        _translate = QtCore.QCoreApplication.translate
        make_features.setWindowTitle(_translate("make_features", "Dialog"))
        self.label_4.setText(_translate("make_features", "** EVENTUALLY WILL IMPLEMENT EXTRACTION FROM NDFs **"))
        self.label.setText(_translate("make_features", "Timewindow length (s)"))
        self.label_2.setText(_translate("make_features", "Use peakdet features?"))
        self.chunk_len_box.setText(_translate("make_features", "5"))
        self.label_3.setText(_translate("make_features", "Number of CPU cores to use"))
        self.cores_to_use.setText(_translate("make_features", "all"))
        self.set_h5_folder.setText(_translate("make_features", "Choose h5 folder"))
        self.extract_features_button.setText(_translate("make_features", "Extract Features"))
        self.progress_bar_label.setText(_translate("make_features", "Progress:"))
        self.logpath_dsplay.setText(_translate("make_features", "Path to Logfile:"))

