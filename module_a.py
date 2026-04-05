from module_b import *


def main():
    print("module_a: main() is running")

print("module_a: __name__ =", __name__)

if __name__ == '__main__':
    print("module_a: I am executed directly")
    main()

con = details()
details.printName(any) 