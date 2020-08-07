from time import time
import random
import csv
import os

words_pm = 0
errors = 0

with open("C:/Users/rianl/Desktop/miguel/texto.txt","r") as file:
		leer = csv.reader(file)
		lista = list(leer)

end = time()+60

while time() < end:
	number = random.randint(0,70)
	word = lista[0][number]
	print(word)
	typee = input("")
	if word == typee:
		words_pm += 1
	else:
		errors += 1
	os.system("cls")

print("Words per minuite: ", words_pm)
print("Errors: ", errors)



