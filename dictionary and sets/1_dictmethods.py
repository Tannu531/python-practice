marks= {
    "Tannu":98,
    "Harsh":97,
    "Kanishka":95
}
print(marks.items())
print(marks.values())
print(marks.keys())
marks.update({"Kanishka" : 100,"harry":99})
print(marks)
print(marks.get("harry"))
print(marks.get("harry1")) #prints none
print(marks["harry1"])#returns an error
