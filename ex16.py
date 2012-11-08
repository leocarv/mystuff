# -*- coding: utf-8 -*-
from sys import argv

#recupera os argumentos
script, filename = argv

#printa as intruções
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)"
print "If you do want that, hit RETURN."

#espera a resposta
raw_input("?")

#caso o usuario escolha continuar, abre o arquivo
print "Opening the file..."
target = open(filename, 'w')

#trunca o arquivo
print "Truncating the file. Goodbye!"
target.truncate()

#pede para o usuario inputar 3 linhas
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

#escreve o arquivo novamente, com as 3 linhas
print "I'm going to write these to the file."
target.write(line1)
target.write("\r\n")
target.write(line2)
target.write("\r\n")
target.write(line3)
target.write("\r\n")

#e fecha o arquivo usado
print "And finally, we close it."
target.close()