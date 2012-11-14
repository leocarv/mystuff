# -*- coding: utf-8 -*-
from sys import exit
from random import randint

class Game(object):

    def __init__(self):
        self.msg_game_over = [
            "Você morreu.",
            "Sua mãe ficaria orgulhosa.",
            "Eu tenho um cachorro pequeno que é melhor nisso"        
        ]
    
    def inicio(self):
        args = {"sala": "sala_principal"}       #recupera a sala inicial
        while True:
            print "\n", "-" * 50                      # printa uma quebra de linha
            args = getattr(self, args['sala'])(args)  # executa o metodo dinamicamente, passando argumentos
    
    def sala_principal(self, parametros):
        print "Estamos na sala inicial"        
        print "Escolha entre 1, 2 e 3"        
        action = raw_input("> ")
        
        if action == "1":
            print "Escolheu 1"
            return {"sala": "corredor_direita"}
        elif action == "2":
            print "Escolheu 2"
            return {"sala": "game_over"}
        elif action == "3":
            print "Escolheu 3"
            return {"sala": "corredor_esquerda"}     
        else:
            return {"sala": "sala_principal"}
                
    def corredor_direita(self, parametros):
        print "Estamos no corredor da direita"
        print "Escolha entre 1, 2 e 3"        
        action = raw_input("> ")
        
        if action == "1":
            print "Escolheu 1"
            return {"sala": "game_over"}
        elif action == "2":
            print "Escolheu 2"
            return {"sala": "acerte_numero",
                    "max": "100",
                    "tentativas": "7",
                    "sala_acerto": "sala_final"}
        elif action == "3":
            print "Escolheu 3"
            return {"sala": "game_over"}   
        else:
            return {"sala": "corredor_direita"}
            
    def corredor_esquerda(self, parametros):
        print "Estamos no corredor da esquerda"
        print "Escolha entre 1, 2 e 3"        
        action = raw_input("> ")
        
        if action == "1":
            print "Escolheu 1"
            return {"sala": "game_over"}
        elif action == "2":
            print "Escolheu 2"
            return {"sala": "acerte_numero",
                    "max": "500",
                    "tentativas": "12",
                    "sala_acerto": "sala_final"}
        elif action == "3":
            print "Escolheu 3"
            return {"sala": "game_over"}   
        else:
            return {"sala": "corredor_esquerda"}
    
    def acerte_numero(self, parametros):
        numero = randint(1, int(parametros['max']))
        total_tentativas = int(parametros['tentativas'])
        tentativas = 0
        escolha = 0
        while (escolha != numero) and (total_tentativas > tentativas):
            escolha = input("Escolha um número entra 1 e %s (%s tentativa(s)):" % (parametros['max'], (total_tentativas - tentativas)))
            tentativas += 1
            if escolha < numero:
                print "%s é menor." % escolha
            elif escolha > numero:
                print "%s é maior." % escolha
        if total_tentativas != tentativas:
            print "Parabéns!"
            print "Você acertou com %s tentativas" % tentativas
            return {"sala": parametros['sala_acerto']}
        else:
            return {"sala": "game_over"}
    
    def sala_final(self, parametros):
        print "Estamos na sala final"
        print "Escolha entre 1, 2 e 3"        
        action = raw_input("> ")
        
        if action == "1":
            print "Escolheu 1"
            return {"sala": "game_over"}
        elif action == "2":
            print "VOCÊ GANHOU!"
            exit(0)
        elif action == "3":
            print "Escolheu 3"
            return {"sala": "game_over"}   
        else:
            return {"sala": "sala_final"}
        
    def game_over(self, parametros):
        print self.msg_game_over[randint(0,len(self.msg_game_over) - 1)]
        exit(1)