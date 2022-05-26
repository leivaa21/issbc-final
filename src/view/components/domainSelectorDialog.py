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
        for domain in domainList:
            button = QPushButton('Dominio = ' + domain)

            def setDomain():
                self.response = domain
                self.accept()

            button.clicked.connect(setDomain)
            self.buttonBox.addButton(button, QDialogButtonBox.ActionRole)

        self.layout = QVBoxLayout()
        message = QLabel("Selecciona el dominio:")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
