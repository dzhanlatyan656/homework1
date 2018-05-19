
def user_input(user_input1, user_input2):
	if user_input1 == user_input2:
		print(1)
	elif len(user_input1) > len(user_input2):
		print(2)
	elif len(user_input1) > len(user_input2) and  user_input2 == "learn":
			print(3)

	else:
		print("ошибка")

def user_input2(user_input1, user_input2):
	if user_input1 == user_input2:
		return 1
	elif len(user_input1) > len(user_input2):
		return 2
	elif len(user_input1) > len(user_input2) and  user_input2 == "learn":
		return 3
	else:
		print("ошибка")


a = user_input2("12345", "12d")

user_input1 = input("введите первое слово ")
user_input2 = input("введите второе слово ")

user_input(user_input1, user_input2)
print(a)