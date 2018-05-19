school = [
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{"school_class": "5b", "scores": [4,3,5,4,5]},
{"school_class": "3a", "scores": [5,5,5,4,3]}]

school_sum = 0
school_count = 0
for a in school:
	scores = a['scores']
	class_sum = sum(scores)
	class_count= len(scores)
	print(a.get("school_class"), class_sum/class_count)

	school_sum += class_sum
	school_count += class_count

print(school_sum/school_count)

