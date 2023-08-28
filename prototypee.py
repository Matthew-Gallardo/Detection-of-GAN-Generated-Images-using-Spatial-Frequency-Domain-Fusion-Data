from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 646)
        MainWindow.setStyleSheet("#centralwidget {\n""background-image: url(resources/Get Started.jpg);\n""}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.setWelcomePage()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.logoName.setText(_translate("MainWindow", "Logo/App Name"))
        self.homeBar.setText(_translate("MainWindow", "Home"))
        self.datasetBar.setText(_translate("MainWindow", "Dataset"))
        self.modelBar.setText(_translate("MainWindow", "Model"))
        self.docuBar.setText(_translate("MainWindow", "Documentation"))
        self.aboutBar.setText(_translate("MainWindow", "About"))

    def setWelcomePage(self):
        self.icon = QtWidgets.QLabel(parent=self.centralwidget)
        self.icon.setGeometry(QtCore.QRect(370, 340, 261, 261))
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("resources/Icon.png"))
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.getStarted = QtWidgets.QPushButton(parent=self.centralwidget)
        self.getStarted.setGeometry(QtCore.QRect(440, 190, 121, 51))
        self.getStarted.setStyleSheet("* {\n""background: transparent;\n""}")
        self.getStarted.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/Button1.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.getStarted.setIcon(icon)
        self.getStarted.setIconSize(QtCore.QSize(110, 110))
        self.getStarted.setObjectName("getStarted")
        self.gallery1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gallery1.setGeometry(QtCore.QRect(660, 510, 171, 121))
        self.gallery1.setText("")
        self.gallery1.setPixmap(QtGui.QPixmap("resources/gallery1.png"))
        self.gallery1.setScaledContents(True)
        self.gallery1.setObjectName("gallery1")
        self.eye1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.eye1.setGeometry(QtCore.QRect(670, 370, 171, 161))
        self.eye1.setText("")
        self.eye1.setPixmap(QtGui.QPixmap("resources/eye.png"))
        self.eye1.setScaledContents(True)
        self.eye1.setObjectName("eye1")
        self.gallery2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.gallery2.setGeometry(QtCore.QRect(180, 370, 171, 171))
        self.gallery2.setText("")
        self.gallery2.setPixmap(QtGui.QPixmap("resources/gallery.png"))
        self.gallery2.setScaledContents(True)
        self.gallery2.setObjectName("gallery2")
        self.eye2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.eye2.setGeometry(QtCore.QRect(170, 510, 171, 121))
        self.eye2.setText("")
        self.eye2.setPixmap(QtGui.QPixmap("resources/eye1.png"))
        self.eye2.setScaledContents(True)
        self.eye2.setObjectName("eye2")
        self.title = QtWidgets.QLabel(parent=self.centralwidget)
        self.title.setGeometry(QtCore.QRect(210, 120, 601, 51))
        self.title.setStyleSheet("* {\n""font: 700 45pt \"Arial\";\n""}")
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("resources/Welcome to App Name.png"))
        self.title.setScaledContents(True)
        self.title.setObjectName("title")
        self.logoName = QtWidgets.QLabel(parent=self.centralwidget)
        self.logoName.setGeometry(QtCore.QRect(50, 30, 111, 16))
        self.logoName.setStyleSheet("*{\n""font: 700 10pt \"Arial\";\n""color:rgb(255, 255, 255);\n""}")
        self.logoName.setObjectName("logoName")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("resources/openAI-logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.socmedIcons = QtWidgets.QLabel(parent=self.centralwidget)
        self.socmedIcons.setGeometry(QtCore.QRect(870, 30, 101, 16))
        self.socmedIcons.setText("")
        self.socmedIcons.setPixmap(QtGui.QPixmap("resources/Group 2.png"))
        self.socmedIcons.setScaledContents(True)
        self.socmedIcons.setObjectName("socmedIcons")
        self.homeBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.homeBar.setGeometry(QtCore.QRect(240, 30, 75, 24))
        self.homeBar.setStyleSheet("* {\n""background: transparent;\n""color: rgb(85, 255, 255)\n""}")
        self.homeBar.setObjectName("homeBar")
        self.datasetBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.datasetBar.setGeometry(QtCore.QRect(340, 30, 75, 24))
        self.datasetBar.setStyleSheet("* {\n""background: transparent;\n""color: rgb(255, 255, 255)\n""}")
        self.datasetBar.setObjectName("datasetBar")
        self.modelBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.modelBar.setGeometry(QtCore.QRect(450, 30, 75, 24))
        self.modelBar.setStyleSheet("* {\n""background: transparent;\n""color: rgb(255, 255, 255)\n""}")
        self.modelBar.setObjectName("modelBar")
        self.docuBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.docuBar.setGeometry(QtCore.QRect(560, 30, 91, 24))
        self.docuBar.setStyleSheet("* {\n""background: transparent;\n""color: rgb(255, 255, 255)\n""}")
        self.docuBar.setObjectName("docuBar")
        self.aboutBar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.aboutBar.setGeometry(QtCore.QRect(690, 30, 51, 24))
        self.aboutBar.setStyleSheet("* {\n""background: transparent;\n""color: rgb(255, 255, 255)\n""}")
        self.aboutBar.setObjectName("aboutBar")

            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())