
def find_person(person):
	names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
	while names:
		name = names.pop(0)
		if name == person:
			print("{} нашелся".format(person))
			return
	print("{} не нашелся".format(person))

find_person("Валера")
find_person("Валера3")



