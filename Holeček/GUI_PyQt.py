# Popis kódu je v .pdf - odkaz na Moodle a v připnutých zprávách na Discord

from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])

hlavni_okno = QtWidgets.QWidget()  # hlavní okno co je vidět
hlavni_okno.setWindowTitle('Můj supr program')  # změní název okna

usporadani = QtWidgets.QHBoxLayout()  # QHBoxLayeout skádá prvky vedle sebe, je spousta jinech možností layoutu
hlavni_okno.setLayout(usporadani)

napis = QtWidgets.QLabel('Teď už tlačítko funguje...')  # popisek
usporadani.addWidget(napis)

tlacitko = QtWidgets.QPushButton('Klikni na mě')  # tlačítko
usporadani.addWidget(tlacitko)

# validator_celych_cisel = QtGui.QIntValidator()
vstup = QtWidgets.QLineEdit()  # input
# vstup.setValidator(validator_celych_cisel)
usporadani.addWidget(vstup)


def zmen_napis():
    vstupni_text = vstup.text()  # vzeme input, přečte z něj text
    napis.setText("Toto jsi napal: " + vstupni_text)  # přepíše label "napis"


def soucet():
    vstupni_text = vstup.text()  # vzeme input, přečte z něj text
    pole_souctu = vstupni_text.split(" ")
    vysledek = 0
    try:
        for prvek in pole_souctu:
            cislo = int(prvek)
            vysledek += cislo

    except ValueError:
        vysledek = "Neumím počítat s písmenkama"

    napis.setText(f"Součet je {vysledek}")


# tlacitko.clicked.connect(zmen_napis)  # propojí zmen_napis a tlacitko
tlacitko.clicked.connect(soucet)

hlavni_okno.show()

app.exec()
