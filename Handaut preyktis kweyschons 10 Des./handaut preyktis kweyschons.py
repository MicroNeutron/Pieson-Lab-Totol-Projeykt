#1
print("Q1")
name1 = input("Enter your name: ")
print("Hello, " + name1)

#2
print("Q2")
a = 5
b = 3
sum = a + b
print("a = " + str(a))
print("b = " + str(b))
print("a + b = " + str(sum))

#3
print("Q3")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")

#4
print("Q4")
my_list = [0, 2, 4, 6, 8]
print("The array is: ")
for item in my_list:
    print(item)
print("The second is: ")
print(my_list[2])

#5
print("Q5")
print("Numbers 1-10")
for i in range(1, 11):
    print(i)