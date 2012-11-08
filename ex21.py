# -*- coding: utf-8 -*-
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
	
def substract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
	
print "Let's do some math with just functions!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


#A puzzle for the extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

#extra credit (remontar a formula acima)
print "Remontando a formula sem usar as funções"
print age + (height - (weight * (iq / 2)))

#extra credit (criar outra formula qualquer)
print "Criando outra formula"
print height - (age + (weight * 2))

#extra credit (refazer a formula criada, usando as funcoes)
print "Refazer a formula criada"
print substract(height, add(age , multiply(weight, 2)))
