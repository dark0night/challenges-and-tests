#problem 1
try:
    for i in ['a','b','c']:
        print(i**2)
    
except TypeError:
        print("Encounterd an error kindly check the datatypes...")
else:
    print("i always run!!")

#problem 2
try:
    x = 5
    y = 0

    z = x/y
except:
    print("\ndivision by 0 is not defined!! ")
finally:
    print("All done!")

#problem 3

    
while True:
    def ask(userinp):
        print(f"your squared output is {int(userinp) ** 2}")
    
    try:

        userinp = input('\nenter a number : ')
        if userinp == 'q':
            break
        ask(userinp)
    except ValueError:
        print("enter a proper value!")
    else:
        break
