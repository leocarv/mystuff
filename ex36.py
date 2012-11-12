# -*- coding: utf-8 -*-
from sys import exit

def dead(why):
    print why, "Good job!"
    exit(0)
    
def start():
    print "Inicio do jogo."
    print "Escolhe esquerda ou direita?."
    
    escolha = raw_input("> ")
    
    if escolha == "esquerda":
        sala_esquerda()
    elif escolha == "direita":
        sala_direita()
    else:
        dead("O jogo acabou!")

def sala_esquerda():
    print "Bem vindo a sala da esquerda"
    print "Deseja ir para onde?"


def sala_direita():
    print "Bem vindo a sala da direita"
    print "Deseja ir para onde?"

        
start()