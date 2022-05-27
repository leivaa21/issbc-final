from os import path
from types import NoneType
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QListWidget, QListWidgetItem, QPushButton, QLineEdit, QComboBox, QCheckBox
from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator
from view.components.domainSelectorDialog import DomainDialog

from controller.domain import DomainController
from controller.evalue import EvaluatorController
from controller.storage import StorageController
from view.components.informResponseDialog import InformResponseDialog


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
        self.__case_list = QListWidget()
        self.__show_cases_on_list()
        MainAppLayout.addWidget(self.__case_list, 3)
        MainAppLayout.addLayout(self.__options_widget(), 7)
        return MainAppLayout

    def __show_cases_on_list(self):
        self.__case_list.clear()
        for case in self.__storage_controller.getCases():
            QListWidgetItem(case.identificator(), self.__case_list)

    def __options_widget(self):
        optionsLayout = QVBoxLayout()

        topOptionsLayout = self.__generate_top_options()
        optionsLayout.addLayout(topOptionsLayout, 2)

        formLayout = self.__generate_case_form()
        optionsLayout.addLayout(formLayout, 6)
        optionsLayout.addLayout(self.__rule_selector_layout(), 2)

        return optionsLayout

    def __generate_top_options(self):
        topOptionsLayout = QHBoxLayout()

        addCaseBtn = QPushButton('Añadir caso')

        def addCaseBtnAction():
            def formatFormField(FieldWidget):
                fieldType = type(FieldWidget).__name__
                fieldValue = ''
                if fieldType == 'QLineEdit':
                    fieldValue = FieldWidget.text()
                if fieldType == 'QComboBox':
                    fieldValue = FieldWidget.currentText()
                return fieldValue
            i = 0
            params = {}

            for i in range(self.__form_layout.rowCount()):
                Label = self.__form_layout.itemAt(
                    i, QFormLayout.LabelRole).widget().text()
                FieldWidget = self.__form_layout.itemAt(
                    i, QFormLayout.FieldRole).widget()
                FieldValue = formatFormField(FieldWidget)
                if str(FieldValue) == '':
                    # Error
                    print('Not all params were given!')
                    return
                params[Label] = FieldValue

            case = self.__domain_controller.generateCase(params)
            self.__storage_controller.saveOne(case)
            self.__show_cases_on_list()

        addCaseBtn.clicked.connect(addCaseBtnAction)
        topOptionsLayout.addWidget(addCaseBtn)

        deleteCaseBtn = QPushButton('Eliminar caso seleccionado')

        def deleteCaseBtnAction():
            if type(self.__case_list.currentItem()) == NoneType:
                return
            selectedCaseIdentificator = self.__case_list.currentItem().text()
            self.__storage_controller.removeCase(selectedCaseIdentificator)
            self.__show_cases_on_list()

        deleteCaseBtn.clicked.connect(deleteCaseBtnAction)
        topOptionsLayout.addWidget(deleteCaseBtn)

        valueOneBtn = QPushButton('Valorar seleccionado')

        def valueOneBtnAction():
            if type(self.__case_list.currentItem()) == NoneType:
                return
            selectedCaseIdentificator = self.__case_list.currentItem().text()
            ruleApplyArray = [
                self.__rule1_checkBox.isChecked(),
                self.__rule2_checkBox.isChecked(),
                self.__rule3_checkBox.isChecked()
            ]
            evaluation = self.__evaluator_controller.evalueOne(
                selectedCaseIdentificator, ruleApplyArray)
            self.__display_inform_dialog(evaluation)

        valueOneBtn.clicked.connect(valueOneBtnAction)
        topOptionsLayout.addWidget(valueOneBtn)

        valueAllBtn = QPushButton('Valorar todos')

        def valueAllBtnAction():
            if self.__storage_controller.getCases().__len__() == 0:
                return
            ruleApplyArray = [
                self.__rule1_checkBox.isChecked(),
                self.__rule2_checkBox.isChecked(),
                self.__rule3_checkBox.isChecked()
            ]
            evaluation = self.__evaluator_controller.evalueAll(ruleApplyArray)
            self.__display_inform_dialog(evaluation)

        valueAllBtn.clicked.connect(valueAllBtnAction)
        topOptionsLayout.addWidget(valueAllBtn)

        return topOptionsLayout

    def __display_inform_dialog(self, evaluation):
        inform_dlg = InformResponseDialog(evaluation)
        inform_dlg.exec()
        pass

    def __generate_case_form(self):
        print('Generating form for domain: ' +
              self.__domain_controller._domain)
        paramsDic = self.__domain_controller.getDomainParamsDict().items()
        self.__form_layout = QFormLayout()
        for key, val in paramsDic:
            self.__add_row(key, val)
        return self.__form_layout

    def __add_row(self, label, paramType):
        inputField = QLineEdit()

        if paramType == 'int':
            inputField.setValidator(QIntValidator())

        if paramType == 'float':
            inputField.setValidator(QDoubleValidator())

        if paramType == 'bool':
            inputField = QComboBox()
            inputField.addItems(['True', 'False'])

        return self.__form_layout.addRow(label, inputField)

    def __rule_selector_layout(self):
        ruleSelectorLayout = QHBoxLayout()
        ruleSelectorLayout.addWidget(
            QLabel('Selecciona las reglas a evaluar:'))
        self.__rule1_checkBox = QCheckBox('Rule 1')
        self.__rule2_checkBox = QCheckBox('Rule 2')
        self.__rule3_checkBox = QCheckBox('Rule 3')
        ruleSelectorLayout.addWidget(self.__rule1_checkBox)
        ruleSelectorLayout.addWidget(self.__rule2_checkBox)
        ruleSelectorLayout.addWidget(self.__rule3_checkBox)
        return ruleSelectorLayout

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
