from PyQt5 import QtWidgets , uic
import random

class telas():
    def __init__(self) :
        app = QtWidgets.QApplication([])

         # Inicialização da tela Inicio
        self.inicio = uic.loadUi("qt/inicio.ui")
        self.inicio.show()

        # Inicialização da tela Tabuleiro
        self.tabuleiro = uic.loadUi("qt/tabuleiro.ui")

        # Inicialização da tela e Atribuição do Método ao Botão (Tela Inicio)
        self.inicio.botao_iniciar.clicked.connect(self.mudar_tela)
        self.inicio.botao_fechar_i.clicked.connect(self.fechar_inicio)

        # Inicialização da tela e Atribuição do Método ao Botão (Tela Ganhou)
        self.ganhou = uic.loadUi("qt/ganhou.ui")
        self.ganhou.botao_fechar_g.clicked.connect(self.fechar_ganhou)
        
        # Inicialização da tela e Atribuição do Método ao Botão (Tela Perdeu)
        self.perdeu = uic.loadUi("qt/perdeu.ui")
        self.perdeu.botao_fechar_p.clicked.connect(self.fechar_perdeu)

        # Declaração e Inicialização de Variaveis (para contabilizar tentativas)
        self.tentativas_max = 15
        self.tentativas = 0

        # Lista de Letras e Números
        coordenadasLetras = ["A", "B", "C", "D", "E", "F", "G", "H"]
        coordenadasNumeros = ["1","2","3","4","5", "6", "7", "8"]

        #Criação de Lista
        sorteio = []
        self.barcos = []

        # Sorteio de Diferentes Letras
        sorteio1 = random.sample(coordenadasLetras, 4)

        # Estrutura de Repetição (sorteia os número conofrme o tamanho dos barcos)
        while True:
            sorteio2 = random.sample(coordenadasNumeros, 4)
            if int(sorteio2[1]) > 2:
                continue
            if int(sorteio2[2]) > 4:
                continue
            if int(sorteio2[3]) > 5:
                continue
            else:
                break
 
        # Estrutura de Repetição (concatena as letras e números sorteados)
        for i in range(len(sorteio1)):
            sorteio.append(f"{sorteio1[i]}{sorteio2[i]}")
 
        # Estrutura de Repetição (adiciona na lista as demais cordenadas de acordo com o tamanho do barco)
        for indice_sorteado in range(len(sorteio)):
            if indice_sorteado == 0:
                for i in range(len(sorteio)):
                    self.barcos.append(sorteio[i])
 
            if indice_sorteado == 1:
                separado = list(sorteio[indice_sorteado])
                self.barcos.append(f"{separado[0]}{int(separado[1])+1}")
               
            if indice_sorteado == 2:
                for i in range(2):
                    separado = list(sorteio[indice_sorteado])
                    self.barcos.append(f"{separado[0]}{int(separado[1])+(i + 1)}")
 
            if indice_sorteado == 3:
                for i in range(3):
                    separado = list(sorteio[indice_sorteado])
                    self.barcos.append(f"{separado[0]}{int(separado[1])+(i+1)}")
 
        print(self.barcos)

        # Estrutura de Repetição (diciona a função de selecionar_botão em todos os botões da tela)
        for button in self.tabuleiro.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.selecionarBotao)

        app.exec()
        
    # Métodos de Alterar Tela
    def mudar_tela(self):
        self.inicio.close()
        self.tabuleiro.show()

    def fechar_inicio(self):
        self.inicio.close()

    def fechar_ganhou(self):
        self.ganhou.close()

    def fechar_perdeu(self):
        self.perdeu.close()

    # Método (lógica do jogo)
    def selecionarBotao(self):
        sender = self.inicio.sender()
        senderCoordenada = sender.objectName()
 
        if self.tentativas < self.tentativas_max:
           
            # Estrutura de Decisão (quando o botão selecionador conter um barco, 
            # a cordenada se torna braazul e o jogador não perde sua tentativa)
            if senderCoordenada in self.barcos:
                sender.setStyleSheet("background-color: #9CDDEE; border: none")
                self.barcos.remove(senderCoordenada)
            
                # Estrutura de Decisão (quando a lista de barco for zero, significa que todos os barcos 
                # foram selecionados na tela e fecha a tela do tabuleiro para abbrir a tela de ganhador)
                if len(self.barcos) == 0:
                    self.tabuleiro.close()
                    self.ganhou.show()
                
            # Estrutura de Decisão (quando o botão selecionado não for correspondente a um barco
            # a cordenada se torna branca e o jogador perde uma tentativa)
            else:
                sender.setStyleSheet("background-color: white; border: none")
                self.tentativas += 1
        
        # Estrutura de Decisão (quando o jogador perde suas chances ou então não acerta as cordenadas do barco,
        # o programa fecha a tela de tabuleiro e abre a tela de perdedor)
        else:
            self.tabuleiro.close()
            self.perdeu.show()


if __name__ == '__main__':
    c = telas()