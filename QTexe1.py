import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)

        self.lbl = QLabel(self)
        self.champ = QLineEdit(self)
        self.bouton = QPushButton(self)
        self.lbl2 = QLabel(self)
        self.bouton2 = QPushButton(self)
        #self.text = text

        # crée une fenêtre

        self.setWindowTitle("Une première fenêtre")
        self.setGeometry(100, 100, 220, 120)

        # on crée le label

        self.lbl.setGeometry(10, 0, 200, 20)
        self.lbl.setText("Saisir votre nom:")

        # crée le champ saisi

        self.champ.setGeometry(10, 20, 200, 20)

        # bouton ok

        self.bouton.setText("OK")
        self.bouton.setGeometry(10, 41, 200, 20)
        self.bouton.clicked.connect(self.action)

        # retour info

        self.lbl2.setGeometry(10, 60, 200, 20)
        self.lbl2.setText(f"")

        # bouton quitter
        self.bouton2.setText("Quitter")
        self.bouton2.clicked.connect(self.actionFermer)
        self.bouton2.setGeometry(10, 80, 200, 20)

    def action(self):
        self.lbl2.setText(self.champ.text())

    def actionFermer(self):
        self.close(app)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()