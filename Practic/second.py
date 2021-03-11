text_1 = "\nВыберите дополнение к пицце!"
text_1 += "\n(Если хотите завершить введите 'quit'): "
topping = ""
active = True
while active == True:
	topping = input(text_1)
	if topping != 'quit':
		print("Вы добавили " + topping.title() + "!")
	elif topping == 'quit':
		active = False
	
