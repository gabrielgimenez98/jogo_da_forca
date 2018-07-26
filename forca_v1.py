# -*- coding: UTF8 -*-
# Jogo da forca feito para estudo de POO
# Feito por Gabriel Gimenez de Lima

# Aqui ficam os imports
import random

# Criação da lista cujos elementos são a fase do tabuleiro do jogo
lista_tabuleiro = [
    '''
    +---------+
    |         |
    |
    |
    |
    ======

    ''',
    '''
        +---------+
                  |
        |         0
        |
        |
        |
        ======

        ''',
    '''
            +---------+
                      |
            |         0
            |         |
            |         
            |
            ======

            ''',
    '''
                +---------+
                          |
                |         0
                |        /|
                |
                |
                ======

                ''',
    '''
                +---------+
                          |
                |         0
                |        /|\\
                |
                |
                ======

                ''',
    '''
                    +---------+
                              |
                    |         0
                    |        /|\\
                    |        /
                    |
                    ======

                    ''',
    '''
                        +---------+
                                  |
                        |         0
                        |        /|\\
                        |        / \\
                        |
                        ======

                        '''
]


# função que pega uma palavra do arquivo txt préviamente gravado
def pega_palavra():
    with open("palavras.txt", "rt") as arquivo:
        banco = arquivo.readlines()

    return banco[random.randint(0, len(banco)-1)].strip()

#função para cadastrar palavras
def cadastrar_palavra():
    palavra = input('Qual palavra deseja cadastrar?')
    with open("palavras.txt","at") as arquivo:
        arquivo.write('\n'+palavra)
    print('Palavra Cadastrada!!')
    menu()

#Função que cria o menu de opções
def menu():
    opc = int(input('Qual opção?\n1-Cadastrar Palavras 2-Jogar'))

    if opc == 1:
        cadastrar_palavra()
    else:
        main()


#Criação da classe do jogo
class Forca:
    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_corretas = []

    #Método que executa a parte de advinhar a letra
    def advinha_letra(self,letra):
        if letra in self.palavra and letra not in self.letras_corretas :
            self.letras_corretas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True

    #Método que retorna true se o jogo acabou
    def fim_de_jogo(self):
        return self.jogo_ganho() or (len(self.letras_erradas) == 6)

    #método que verifica se o jogador ganhou
    def jogo_ganho(self):
        return '_' not in self.esconde_palavra()

    #Método que esconde a palavra
    def esconde_palavra(self):
        palavra_escondida = ''
        for letra in self.palavra:
            if letra not in self.letras_corretas:
                palavra_escondida += '_ '
            else:
                palavra_escondida += letra
        return palavra_escondida

    #Método que retorna o status do jogo
    def status_jogo(self):
        print(lista_tabuleiro[len(self.letras_erradas)])
        print(self.esconde_palavra())
        print('Letras corretas:\n', self.letras_corretas)
        print('Letras erradas:\n', self.letras_erradas)

#função main para iniciar o jogo
def main():
    enforcado = Forca(pega_palavra())

    while ( not enforcado.fim_de_jogo()):
        enforcado.status_jogo()
        enforcado.advinha_letra(input('Qual letra você acha que tem na palavra? '))

    #verifica se o jogador ganhou ou não
    if enforcado.jogo_ganho():
        print('Parabéns!!! você venceu, adorei jogar com você.')
    else:
        print('que pena!! parece que eu venci\n a palavra escondida era: ', enforcado.palavra)

#executando o programa
menu()

