from os import path
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtGui import QIcon
from view.components.domainSelectorDialog import DomainDialog

from controller.domain import DomainController
from controller.evalue import EvaluatorController
from controller.storage import StorageController


class AppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__domain_controller = DomainController('footballPlayer')
        self.__storage_controller = StorageController()
        self.__evaluator_controller = EvaluatorController(
            self.__domain_controller, self.__storage_controller)

        self.__initUI__()

    def __initUI__(self):
        self.__set_geometry__()
        self.__set_basics__()
        self.show()
        self.__show_domain_dialog()

    # Geometria de la aplicación
    # 1024 width || 576 height || 16:9 aspect ratio
    # Center widow
    def __set_geometry__(self):
        self.resize(1024, 576)
        # Center
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def __set_basics__(self):
        self.setWindowTitle(
            'ISSBC TFP - Valorar - i92leroa | i92loden | i92arcaj')
        icon_path = path.dirname(__file__) + '/../../images/icon.ico'
        print(icon_path)
        self.setWindowIcon(QIcon(icon_path))

    def __set_layout__(self):
        VMainLayout = QVBoxLayout()

        VMainLayout.addLayout(self.__top_bar_layout(), 1)
        VMainLayout.addLayout(self.__main_app_layout(), 9)
        self.setLayout(VMainLayout)
        pass

    def __top_bar_layout(self):
        TopBarLayout = QHBoxLayout()
        TopBarLayout.addWidget(
            QLabel('Domain ' + self.__domain_controller._domain), 2)
        return TopBarLayout

    def __main_app_layout(self):
        MainAppLayout = QHBoxLayout()
        self.__init_case_list()
        MainAppLayout.addWidget(self.__case_list, 3)
        MainAppLayout.addLayout(self.__options_widget(), 7)
        return MainAppLayout

    def __init_case_list(self):
        self.__case_list = QListWidget()
        QListWidgetItem(self.__domain_controller._domain +
                        ' Item1', self.__case_list)
        QListWidgetItem(self.__domain_controller._domain +
                        ' Item2', self.__case_list)
        QListWidgetItem(self.__domain_controller._domain +
                        ' Item3', self.__case_list)

    def __options_widget(self):
        optionsLayout = QVBoxLayout()

        topOptionsLayout = QHBoxLayout()
        topOptionsLayout.addWidget(QPushButton('Añadir caso'))
        topOptionsLayout.addWidget(QPushButton('Eliminar caso'))
        topOptionsLayout.addWidget(QPushButton('Valorar seleccionado'))
        topOptionsLayout.addWidget(QPushButton('Valorar todos'))

        optionsLayout.addLayout(topOptionsLayout, 2)

        formLayout = self.__generate_case_form()

        optionsLayout.addLayout(formLayout, 8)

        return optionsLayout

    def __generate_case_form(self):
        print('Generating form for domain: ' +
              self.__domain_controller._domain)
        return QFormLayout()

    def __show_domain_dialog(self):
        dlg = DomainDialog()
        if dlg.exec():
            print("Domain selected => '" + dlg.response + "' !")
            self.__domain_controller = DomainController(dlg.response)
            self.__storage_controller = StorageController()
            self.__evaluator_controller = EvaluatorController(
                self.__domain_controller, self.__storage_controller)
            self.setWindowTitle(
                'Valorar | Domain selected > ' + self.__domain_controller._domain)
            self.__set_layout__()
        else:
            self.closeEvent()
