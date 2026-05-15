# function
def greet():
	print ("Welcome")
	print ("Youssef")
greet()
print ("*"*15)
# function : paramenter 
def greet_with_age(name,age,idd):
	print("Hello ",name)
	print("Your age is ",age)
	print("Your idd is ", idd)

greet_with_age("Youssef",16,123)
print("*"*20)
def add(x,y):
	print("result = ",x+y)
	
add(6,4)
add(9,7)
print("*"*25)
def average(num1,num2,num3):
	total = num1+num2+num3
	avg = total/3
	print("Avg",avg)
average(90,80,75)