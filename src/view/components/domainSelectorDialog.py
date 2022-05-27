from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton, QDesktopWidget

from model.shared.domainList import domainList


class DomainDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.response = domainList[0]
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setWindowTitle("Selector de dominio")

        self.buttonBox = QDialogButtonBox()
        button1 = QPushButton('Dominio = ' + domainList[0])

        def setDomainFootball():
            self.response = domainList[0]
            self.accept()
        button1.clicked.connect(setDomainFootball)
        self.buttonBox.addButton(button1, QDialogButtonBox.ActionRole)

        button2 = QPushButton('Dominio = ' + domainList[1])

        def setDomainF1():
            self.response = domainList[1]
            self.accept()
        button2.clicked.connect(setDomainF1)

        self.buttonBox.addButton(button2, QDialogButtonBox.ActionRole)

        self.layout = QVBoxLayout()
        message = QLabel("Selecciona el dominio:")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
