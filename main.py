import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox


def opcao_selecionada():
    opcao = combo.currentText()
    match opcao:
        case "Comprimento":
            # Limpa as opções anteriores
            combo1.clear()
            combo2.clear()

            # opções
            combo1.addItem("", janela)
            combo1.addItem("Km", janela)
            combo1.addItem("Metros", janela)
            combo1.addItem("Cm", janela)

            combo2.addItem("", janela)
            combo2.addItem("Km", janela)
            combo2.addItem("Metros", janela)
            combo2.addItem("Cm", janela)

            le1.clear()
            le2.clear()


def se_iguais():
    if le1.hasFocus():
        le2.setText(le1.text())
    else:
        le1.setText(le2.text())


def calculo():
    unidade1 = combo1.currentText()
    unidade2 = combo2.currentText()

    if unidade1 == "Km":
        # Km para Km
        if unidade2 == "Km":
            se_iguais()
        # Km para Metros
        elif unidade2 == "Metros":
            if le1.hasFocus():
                try:
                    km = float(le1.text())
                    metros = km * 1000
                    le2.setText(str(metros))
                except ValueError:
                    le2.clear()
            else:
                try:
                    metros = float(le2.text())
                    km = metros / 1000
                    le1.setText(str(km))
                except ValueError:
                    le1.clear()
        # Km para Cm
        elif unidade2 == "Cm":
            if le1.hasFocus():
                try:
                    km = float(le1.text())
                    centimetros = km * 100000
                    le2.setText(str(centimetros))
                except ValueError:
                    le2.clear()
            else:
                try:
                    centimetros = float(le2.text())
                    km = centimetros / 100000
                    le1.setText(str(km))
                except ValueError:
                    le1.clear()

    elif unidade1 == "Metros":
        # Metros para Km
        if unidade2 == "Km":
            if le1.hasFocus():
                try:
                    metros = float(le1.text())
                    km = metros / 1000
                    le2.setText(str(km))
                except ValueError:
                    le2.clear()
            else:
                try:
                    km = float(le2.text())
                    metros = km * 1000
                    le1.setText(str(metros))
                except ValueError:
                    le1.clear()
        # Metros para Metros
        elif unidade2 == "Metros":
            se_iguais()
        # Metros para Cm
        elif unidade2 == "Cm":
            if le1.hasFocus():
                try:
                    metros = float(le1.text())
                    centimetros = metros * 100
                    le2.setText(str(centimetros))
                except ValueError:
                    le2.clear()
            else:
                try:
                    centimetros = float(le2.text())
                    metros = centimetros / 100
                    le1.setText(str(metros))
                except ValueError:
                    le1.clear()

    elif unidade1 == "Cm":
        # Cm para Metros
        if unidade2 == "Metros":
            if le1.hasFocus():
                try:
                    centimetros = float(le1.text())
                    metros = centimetros / 100
                    le2.setText(str(metros))
                except ValueError:
                    le2.clear()
            else:
                try:
                    metros = float(le2.text())
                    centimetros = metros * 100
                    le1.setText(str(centimetros))
                except ValueError:
                    le1.clear()
        # Cm para Km
        elif unidade2 == "Km":
            if le1.hasFocus():
                try:
                    centimetros = float(le1.text())
                    km = centimetros / 100000
                    le2.setText(str(km))
                except ValueError:
                    le2.clear()
            else:
                try:
                    km = float(le2.text())
                    centimetros = km * 100000
                    le1.setText(str(centimetros))
                except ValueError:
                    le1.clear()
        elif unidade2 == "Cm":
            se_iguais()


# Criação do objeto da aplicação
app = QApplication(sys.argv)
# Criação do objeto da janela
janela = QWidget()
janela.resize(400, 600)  # Redefinindo tamanho da janela
janela.setWindowTitle("Conversor de Unidades")  # Definição do título da janela

# Escolha do tipo de conversão
label = QLabel("Escolha o tipo de conversão abaixo", janela)
label.move(45, 35)
label.setStyleSheet('font-size:20px')

combo = QComboBox(janela)
combo.resize(320, 25)
combo.move(40, 80)
combo.addItem("", janela)
combo.addItem("Comprimento", janela)
combo.currentIndexChanged.connect(opcao_selecionada)

# Primeira Unidade
label1 = QLabel("Unidade 1", janela)
label1.move(220, 150)
label1.setStyleSheet('font-size:30px')

combo1 = QComboBox(janela)
combo1.resize(85, 25)
combo1.move(43, 190)

le1 = QLineEdit("", janela)
le1.setGeometry(45, 150, 150, 40)
le1.textChanged.connect(calculo)

# Segunda Unidade
label2 = QLabel("Unidade 2", janela)
label2.move(220, 230)
label2.setStyleSheet('font-size:30px')

combo2 = QComboBox(janela)
combo2.resize(85, 25)
combo2.move(43, 270)

le2 = QLineEdit("", janela)
le2.setGeometry(45, 230, 150, 40)
le2.textChanged.connect(calculo)

janela.show()  # exibição da janela
app.exec()  # Execução do aplicativo
