import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel, QGridLayout, QWidget, QMessageBox
from PyQt5.QtCore import QSize
import subprocess

class Janela(QMainWindow): #MainWindow
    def __init__(self):
        super(Janela, self).__init__()        
        self.setup_main_window()
        self.carregarJanela() #initUI

    def setup_main_window(self):
        self.x = 800
        self.y = 600
        self.setMinimumSize(QSize(self.x, self.y))
        self.setWindowTitle("Processamento Digital de Imagens - IFTM")
        self.wid = QWidget(self)
        self.setCentralWidget(self.wid)
        self.layout = QGridLayout() 
        self.wid.setLayout(self.layout)

    def carregarJanela(self): #initUI
        #Cria os componentes (Label, Button, Text, Image)

        #Cria a barra de menu
        self.barraMenu = self.menuBar()

        #Cria o menu
        self.menuArquivo = self.barraMenu.addMenu("Arquivo")
        self.menuTransformacao = self.barraMenu.addMenu("Transformação")
        self.menuSobre = self.barraMenu.addMenu("Sobre")

        # Criar actions
        self.acaoOpen = self.menuArquivo.addAction("Abrir")
        self.acaoOpen.triggered.connect(self.botaoOpen)

        self.acaoClose = self.menuArquivo.addAction("Fechar")
        self.acaoClose.triggered.connect(self.close)

        self.acaoTransform1 = self.menuTransformacao.addAction("Contour") # Add o botao no menu transformacao
        self.acaoTransform1.triggered.connect(self.botaoTransform1) # Ação
        self.menuTransformacao.addSeparator()

        self.acaoTransform2 = self.menuTransformacao.addAction("Emboss")
        self.acaoTransform2.triggered.connect(self.botaoTransform2)
        self.menuTransformacao.addSeparator()

        self.acaoTransform3 = self.menuTransformacao.addAction("Blur")
        self.acaoTransform3.triggered.connect(self.botaoTransform3)
        self.menuTransformacao.addSeparator()

        self.acaoTransform4 = self.menuTransformacao.addAction("Detail")
        self.acaoTransform4.triggered.connect(self.botaoTransform4)
        self.menuTransformacao.addSeparator()

        self.acaoTransform5 = self.menuTransformacao.addAction("Edge Enhance")
        self.acaoTransform5.triggered.connect(self.botaoTransform5)
        self.menuTransformacao.addSeparator()

        self.acaoTransform6 = self.menuTransformacao.addAction("Edge Enhance More")
        self.acaoTransform6.triggered.connect(self.botaoTransform6)
        self.menuTransformacao.addSeparator()

        self.acaoTransform7 = self.menuTransformacao.addAction("Find Edges")
        self.acaoTransform7.triggered.connect(self.botaoTransform7)
        self.menuTransformacao.addSeparator()

        self.acaoTransform8 = self.menuTransformacao.addAction("Sharpen")
        self.acaoTransform8.triggered.connect(self.botaoTransform8)
        self.menuTransformacao.addSeparator()

        self.acaoTransform9 = self.menuTransformacao.addAction("Smooth")
        self.acaoTransform9.triggered.connect(self.botaoTransform9)
        self.menuTransformacao.addSeparator()

        self.acaoTransform10 = self.menuTransformacao.addAction("Smooth More")
        self.acaoTransform10.triggered.connect(self.botaoTransform10)
        self.menuTransformacao.addSeparator()

        self.acaoTransform11 = self.menuTransformacao.addAction("Filtro com Borda - Kernel 1")
        self.acaoTransform11.triggered.connect(self.botaoTransform11)
        self.menuTransformacao.addSeparator()

        self.acaoTransform12 = self.menuTransformacao.addAction("Filtro com Borda - Kernel 2")
        self.acaoTransform12.triggered.connect(self.botaoTransform12)
        self.menuTransformacao.addSeparator()

        self.acaoTransform13 = self.menuTransformacao.addAction("Filtro com Borda - Kernel 3")
        self.acaoTransform13.triggered.connect(self.botaoTransform13)
        self.menuTransformacao.addSeparator()

        self.acaoTransform14 = self.menuTransformacao.addAction("Filtro Negativo")
        self.acaoTransform14.triggered.connect(self.botaoTransform14)
        self.menuTransformacao.addSeparator()

        self.acaoTransform15 = self.menuTransformacao.addAction("Filtro Gama (0.25)")
        self.acaoTransform15.triggered.connect(self.botaoTransform15)
        self.menuTransformacao.addSeparator()

        self.acaoTransform16 = self.menuTransformacao.addAction("Filtro Gama (0.50)")
        self.acaoTransform16.triggered.connect(self.botaoTransform16)
        self.menuTransformacao.addSeparator()

        self.acaoTransform17 = self.menuTransformacao.addAction("Filtro Gama (1.00)")
        self.acaoTransform17.triggered.connect(self.botaoTransform17)
        self.menuTransformacao.addSeparator()

        self.acaoTransform18 = self.menuTransformacao.addAction("Filtro Gama (2.00)")
        self.acaoTransform18.triggered.connect(self.botaoTransform18)
        self.menuTransformacao.addSeparator()

        self.acaoTransform19 = self.menuTransformacao.addAction("Filtro Gama (3.00)")
        self.acaoTransform19.triggered.connect(self.botaoTransform19)
        self.menuTransformacao.addSeparator()

        self.acaoTransform20 = self.menuTransformacao.addAction("Filtro Escala de Cinza")
        self.acaoTransform20.triggered.connect(self.botaoTransform20)
        self.menuTransformacao.addSeparator()

        self.acaoTransform21 = self.menuTransformacao.addAction("Filtro Camada RED")
        self.acaoTransform21.triggered.connect(self.botaoTransform21)
        self.menuTransformacao.addSeparator()

        self.acaoTransform22 = self.menuTransformacao.addAction("Filtro Camada GREEN")
        self.acaoTransform22.triggered.connect(self.botaoTransform22)
        self.menuTransformacao.addSeparator()

        self.acaoTransform23 = self.menuTransformacao.addAction("Filtro Camada BLUE")
        self.acaoTransform23.triggered.connect(self.botaoTransform23)
        self.menuTransformacao.addSeparator()

        self.acaoSobre = self.menuSobre.addAction("Sobre")
        self.acaoSobre.triggered.connect(self.botaoSobre)

        #Imagem 1
        self.imagem1 = QLabel(self) 
        self.endereco1 = 'img/bird1A.jpeg'
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)
        self.imagem1.setAlignment(QtCore.Qt.AlignCenter)

        #Imagem 2
        self.imagem2 = QLabel(self) 
        self.endereco2 = 'img/bird1A.jpeg'
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

        #Organizando os componentes Widgets dentro do GridLayout
        self.layout.addWidget(self.imagem1, 1, 0)
        self.layout.addWidget(self.imagem2, 1, 1)

    #OpenFileDialog
    def botaoOpen(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, caption='Abrir arquivo', 
                                                            directory=QtCore.QDir.currentPath(), 
                                                            filter='All files (*.*);; Imagens (*.jpg; *.jpeg; *.png)',
                                                            initialFilter='Imagens (*.jpg; *.jpeg; *.png)')
        self.endereco1 = fileName
        self.pixmap1 = QtGui.QPixmap(self.endereco1) 
        self.pixmap1 = self.pixmap1.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem1.setPixmap(self.pixmap1)

    def botaoTransform1(self):
        self.imgOriginal = self.endereco1
        self.contour = 'img/contorno.jpeg'
        self.script = '.\contour.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.contour
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.contour
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform2(self):
        self.imgOriginal = self.endereco1
        self.emboss = 'img/emboss.jpeg'
        self.script = '.\emboss.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.emboss
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.emboss
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform3(self):
        self.imgOriginal = self.endereco1
        self.Blur = 'img/Blur.jpeg'
        self.script = '.\Blur.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.Blur
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.Blur
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform4(self):
        self.imgOriginal = self.endereco1
        self.detail = 'img/detail.jpeg'
        self.script = '.\detail.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.detail
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.detail
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform5(self):
        self.imgOriginal = self.endereco1
        self.edgeEnhance = 'img/edgeEnhance.jpeg'
        self.script = '.\edge_Enhance.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.edgeEnhance
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.edgeEnhance
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform6(self):
        self.imgOriginal = self.endereco1
        self.edgeEnhanceMore = 'img/edgeEnhanceMore.jpeg'
        self.script = '.\edge_Enhance_More.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.edgeEnhanceMore
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.edgeEnhanceMore
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform7(self):
        self.imgOriginal = self.endereco1
        self.findEdges = 'img/findEdges.jpeg'
        self.script = '.\Find_Edges.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.findEdges
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.findEdges
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform8(self):
        self.imgOriginal = self.endereco1
        self.sharpen = 'img/findEdges.jpeg'
        self.script = '.\sharpen.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.sharpen
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.sharpen
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform9(self):
        self.imgOriginal = self.endereco1
        self.smooth = 'img/smooth.jpeg'
        self.script = '.\smooth.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.smooth
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.smooth
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform10(self):
        self.imgOriginal = self.endereco1
        self.smoothMore = 'img/smoothMore.jpeg'
        self.script = '.\smooth_More.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.smoothMore
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.smoothMore
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform11(self):
        self.imgOriginal = self.endereco1
        self.kernelA = 'img/kernelA.jpeg'
        self.script = '.\FiltroBorda1.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.kernelA
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.kernelA
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform12(self):
        self.imgOriginal = self.endereco1
        self.kernelB = 'img/kernelB.jpeg'
        self.script = '.\FiltroBorda2.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.kernelB
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.kernelB
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform13(self):
        self.imgOriginal = self.endereco1
        self.kernelC = 'img/kernelC.jpeg'
        self.script = '.\FiltroBorda3.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.kernelC
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.kernelC
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform14(self):
        self.imgOriginal = self.endereco1
        self.imgNegativo = 'img/negativo.jpeg'
        self.script = '.\efeitoNegativo.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgNegativo
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgNegativo
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)
    
    def botaoTransform15(self):
        self.imgOriginal = self.endereco1
        self.imgGama025 = 'img/efeitoGama025.jpeg'
        self.script = '.\efeitoGama025.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgGama025
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgGama025
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform16(self):
        self.imgOriginal = self.endereco1
        self.imgGama050 = 'img/efeitoGama050.jpeg'
        self.script = '.\efeitoGama050.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgGama050
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgGama050
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform17(self):
        self.imgOriginal = self.endereco1
        self.imgGama100 = 'img/efeitoGama100.jpeg'
        self.script = '.\efeitoGama100.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgGama100
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgGama100
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform18(self):
        self.imgOriginal = self.endereco1
        self.imgGama200 = 'img/efeitoGama200.jpeg'
        self.script = '.\efeitoGama200.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgGama200
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgGama200
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform19(self):
        self.imgOriginal = self.endereco1
        self.imgGama300 = 'img/efeitoGama300.jpeg'
        self.script = '.\efeitoGama300.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgGama300
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgGama300
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform20(self):
        self.imgOriginal = self.endereco1
        self.imgEscalaCinza = 'img/efeitoEscalaCinza.jpeg'
        self.script = '.\efeitoEscalaCinza.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgEscalaCinza
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgEscalaCinza
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform21(self):
        self.imgOriginal = self.endereco1
        self.imgCamadaRed = 'img/efeitoCamadaRed.jpeg'
        self.script = '.\camadaRed.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgCamadaRed
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgCamadaRed
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform22(self):
        self.imgOriginal = self.endereco1
        self.imgCamadaGreen = 'img/efeitoCamadaGreen.jpeg'
        self.script = '.\camadaGreen.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgCamadaGreen
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgCamadaGreen
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoTransform23(self):
        self.imgOriginal = self.endereco1
        self.imgCamadaBlue = 'img/efeitoCamadaBlue.jpeg'
        self.script = '.\camadaBlue.py'
        self.programa = 'python ' + self.script + ' \"' + self.imgOriginal + '\" ' + self.imgCamadaBlue
        print(self.programa)
        subprocess.run(self.programa, shell=True)
        self.endereco2 = self.imgCamadaBlue
        self.pixmap2 = QtGui.QPixmap(self.endereco2) 
        self.pixmap2 = self.pixmap2.scaled(342, 533, QtCore.Qt.KeepAspectRatio)
        self.imagem2.setPixmap(self.pixmap2)
        self.imagem2.setAlignment(QtCore.Qt.AlignCenter)

    def botaoSobre(self):
        self.menssagem = QMessageBox()
        self.menssagem.setWindowTitle("Sobre")
        self.menssagem.setText("Desenvolvido por Andressa e Leandro Vilarinho Guimarães\nAplicativo de transformação de imagens\n Ituiutaba, 28 de junho de 2021.")
        self.menssagem.setDetailedText("Filtro:\nBlur: borra a imagem.\nContour: contorna a imagem.\nDetail: realça os detalhes da imagem. \nEdge_Enhance: é um filtro de processamento de imagem que aprimora o contraste da borda de uma imagem ou vídeo na tentativa de melhorar sua acutância (nitidez aparente).\nEdge_Enhance_More: é um filtro de processamento de imagem que aprimora mais o contraste da borda de uma imagem ou vídeo na tentativa de melhorar sua acutância (nitidez aparente).\nEmboss: Faz com que uma seleção pareça elevada ou marcada, convertendo sua cor de preenchimento em cinza e traçando as bordas com a cor de preenchimento original.\nFind_Edges: Identifica áreas da imagem com transições significativas e enfatiza as bordas. Também delineia as bordas de uma imagem com linhas escuras contra um fundo branco e cria uma borda ao redor de uma imagem.\nSharpen:  É um filtro de nitidez no processamento de imagem que melhora a resolução espacial ao realçar os limites do objeto.\nSmooth: Suaviza a imagem.\nSmooth: Suaviza a imagem.")
        self.menssagem.exec_()

aplicacao = QApplication(sys.argv)        
j = Janela()
j.show()
sys.exit(aplicacao.exec_())