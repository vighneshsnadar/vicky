name = "Vighnesh"
temperature = 2000.1
print("Name:", name)           # Outputs: Name: 
print("Temperature:", temperature)  # Outputs: Temperature:
a = 2
b = a
c = 2
print (a is b) # between -5 and 256, python uses optimization, hence I got all as True, because small integer. If it was array, I would get False, like [1,2,3]
print (b is c)
print (a is c)
#age = 16
# age = int(input("Input your age :"))
# if age < 16:
#     print ("You cannot drive.")
# elif age == 16:
#     print ("Drive next year.")
# else :
#     print ("You can drive.")


def greet() : 
    name = input("Input your name: ")
    age = int(input("Input your age :"))
    if age < 16:
        print (f"{name} You cannot drive.")
    elif age == 16:
        print (f"{name} You can drive next year.")
    else :
        print (f"{name} You can drive.")

greet()

