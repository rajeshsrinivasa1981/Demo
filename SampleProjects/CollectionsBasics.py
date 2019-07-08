my_list = ["tokyo","london","Paris","new york"]

print(my_list)
my_list[3] = "New Delhi"
print(my_list)

my_list.append("Toronto")
print(my_list)

my_list.append("Paris")
print(my_list)


for val in my_list:
    print(val)

my_list_2 = ["apples",[1,2,3],["a","b","c"]]
my_list_2[1][1] = 5
print(my_list_2)

print("Paris" in my_list)
print("Banana" in my_list)



my_tuple = ("apples","oranges","grapes")
print(my_tuple.count("apples"))



my_set = {"Chalk", "Duster", "Bo*rd"}
print(my_set)
for x in my_set:
    print(x)
print("Chalk" in my_set)
my_set.add("Pen")
print(my_set)
my_set.update(["Pencil", "Er*ser"])
print(my_set)
len(my_set)




my_dict = {
    "class":"animal",
     "Car" : "Creta",
     "Make": "Hyundai"
}

print(my_dict)

print((my_dict["class"]))
print(my_dict.get("Car"))
print(my_dict.values())

for val in my_dict:
    print(val)

for att,val in my_dict.items():
    print(att,val)

my_dict["color"] = "grey"
print(my_dict)

print(my_dict.items())

my_dict.pop("color")
print(my_dict)

my_dict.popitem()
print(my_dict)

del my_dict["class"]
print(my_dict)

my_dict["color"] = "grey"
print(my_dict)

my_dict["game"] = "cricket"
print(my_dict)








