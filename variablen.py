a : int = 8
b : int = 60

print(123 ,f"ss{a}")
print('Hello\nWorld...') 
print(2+3j)
print(b%a)


if a > 20:
   pass
else:
    print("Small number")
print(type(a))

print("He said that \"Tom will not come\"")
name = "Sajith"
age = 30


print("Name\t:", name)
print("Age\t:", age)
print(b//a)
# print('Enter your Name \t:', end='')
# name = input()
# print('Enter your Age \t:', end='')
# age = input()
class A:
    @staticmethod
    def new_func():
        while True:
            name = input("Enter your Name: ")
            age = input("Enter your Age: ")

            if age.strip() == "":
                print("Age cannot be empty. Try again.\n")
                continue

            try:
                age = int(age)
                print("Hello", name, "You are", age, "years old")
                break
            except ValueError:
                print("Age should be a number. Try again.\n") 
        
A.new_func()