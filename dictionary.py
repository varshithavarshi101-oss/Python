#dictionary is a key value pair and it is unord"ered and mutable
student = {"Name" : "varshitha", "marks" : "98", "subject" : "python"}
print(student)
print(student. keys())
print(student.values())
print(student. items())

#access the elements in the dictionary
student = {"name":"varshitha","age":"17","subject":"python"}
print(student["name"])
print(student["age"])
print(student["subject"])

#change values in a dictionary
student["age"] = 11
print(student["age"])

#add new data to the dictionary
student["city"] = "punganur"
print(student)

#remove data
student.pop("city")
print(student)
student = {"name":"varshitha","marks":"98","course":"python"}
print(student.get('name'))
print(student.get('marks'))
print(student.get('course'))
#update the values of specified key
student.update({"marks":18})
print(student)
#pop removes the specified key and its value
student.pop("marks")
print(student)
#popitem()
student={"name":"varshitha","marks":"98","subject":"python"}
student.popitem()
print(student)

#self default
student = {"name":"varshitha"}
student.setdefault("age",18)
print(student)

#clear method
student.clear()
print(student)
student = {"name":"varshitha","age":18}
new_student = student.copy()
print(new_student)
#order of evalutionon(bodmas)
result = 2+13*2
print(result)
