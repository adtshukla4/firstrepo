def ask():
    while True:
        try:  #try block
            n=int(input("Enter a number: "))
        except:  #except block
            print("This isn't a number,please enter a NUMBER")
            continue
        else:
            break
            
    print("The square of your number is ")
    print(n**2)
    print('Good work ')
    print("This is by akash")

    print("Bye")
ask()