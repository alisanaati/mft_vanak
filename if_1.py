while 1:
    value = input("please input your number:")
    value = int(value)
    if value % 3 == 0 or value % 5 == 0:
        if value % 5 == 0 and value % 3 == 0:
            print("both")
        else:
            if value % 5 == 0:
                print("five")
            if value % 3 == 0:
                print("three")
    else:
        print("Neither")
