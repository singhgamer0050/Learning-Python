# store word meaning in a dict
dict={
    "cat":"a small animal",
    "table":["a piece of furniture" , "list if facts and figure" ]
}
print(dict)

# Count all subject
set={ "python", "java", "C++", "python", "javascript", "java","python", "java", "C++", "c"}
print(len(set))

# Enter marks and save in empty dict 
stu={}
m1= int(input("Enter your marks in Maths:"))
m2= int(input("Enter your marks in Chem:"))
m3= int(input("Enter your marks in Phy:"))
stu.update({"Maths": m1})
stu.update({"Chem": m2})
stu.update({"Phy": m3})
print(stu)

# Store 9 and 9.0
val= {9,"9.0"}
print(val)