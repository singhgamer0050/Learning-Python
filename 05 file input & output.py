# 1 Create a new file "Sample.txt" using python and add few line
with open("Sample.txt","w") as f:
    f.write("Hii Everyone")
    f.write("\nWe are learning file IO")
    f.write("\nusing java")
    f.write("\nI like programing in java")

# 2 Write a function that replace all the occurance of "java" with "python" in above file
with open("Sample.txt","r") as f:
    data = f.read()

new_data = data.replace("java","Python")
print(new_data)

with open("Sample.txt","w") as f:
    f.write(new_data)

# 3 Search if the word "learning exist in file or not"
with open("Sample.txt","r") as f:
    data = f.read()

if ("learning" in data):
    print("learning is present in file")
else:
    print("It is not present in file")

#4 WAF to find in which line of the file does the word "learning" occur first. Print-1 if word not found
def occur_wrd():
    data = True
    line_no=1
    with open("Sample.txt","r") as f:
        while data:
            data = f.readline()
            if ("learning" in data):
                print("learning is present in file at line:",line_no)
            line_no += 1
        return -1
print(occur_wrd())

#5 From a file containing numbers seprated by comma. Print the count of even numbers
count = 0
with open("nums.txt" , "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for val in nums:
        if (int(val) % 2 == 0):
            count +=1

print("Total even numbers in file:",count)