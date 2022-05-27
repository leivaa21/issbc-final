from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QDesktopWidget


class InformResponseDialog(QDialog):
    def __init__(self, evaluation):
        super().__init__()
        self.setWindowTitle('Informes obtenidos')
        MainLayout = QVBoxLayout()
        MainLayout.addWidget(QLabel('Informes Obtenidos'), 1)
        MainLayout.addSpacing(20)
        for inform in evaluation.items():
            informLayout = QVBoxLayout()
            informLayout.setSpacing(10)
            TitlesLayout = QHBoxLayout()
            TitlesLayout.setSpacing(10)

            TitlesLayout.addWidget(QLabel('Identificador'))
            TitlesLayout.addWidget(QLabel('Resultados'))
            informLayout.addLayout(TitlesLayout, 2)

            ValuesLayout = QHBoxLayout()
            ValuesLayout.addWidget(QLabel(inform[0]), 5)

            ResponseLayout = QVBoxLayout()
            results = inform[1]

            failed = False
            for result in results.items():
                ResultValue = ''
                if result[1]:
                    ResultValue = 'ha sido pasada.'
                else:
                    failed = True
                    ResultValue = 'no ha sido pasada.'
                ResponseLayout.addWidget(
                    QLabel(str(result[0]).capitalize() + ' ' + ResultValue))
            if failed:
                ResponseLayout.addWidget(
                    QLabel('¡Este caso NO ha pasado la prueba de valoracion!'))
            else:
                ResponseLayout.addWidget(
                    QLabel('¡Este caso SI ha pasado la prueba de valoracion!'))

            ValuesLayout.addLayout(ResponseLayout, 5)
            informLayout.addLayout(ValuesLayout, 6)
            MainLayout.addLayout(informLayout, 5)
            MainLayout.addSpacing(20)
        self.setLayout(MainLayout)
        self.__set_geometry__()

    def __set_geometry__(self):
        self.resize(500, 200)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
