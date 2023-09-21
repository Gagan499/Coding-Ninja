    choice = int(input())

    if choice == 6:
        break

    if choice < 1 or choice > 5:
        print()
        continue

    if choice == 1:
        
        num1 = int(input())
        num2 = int(input())
        print(num1 + num2)
    elif choice == 2:
        
        num1 = int(input())
        num2 = int(input())
        print(num1 - num2)
    elif choice == 3:
        
        num1 = int(input())
        num2 = int(input())
        print(num1 * num2)
    elif choice == 4:
        
        num1 = int(input())
        num2 = int(input())
        if num2 == 0:
            print("Invalid Operation")
        else:
            print(num1 / num2)
    elif choice == 5:
        
        num1 = int(input())
        num2 = int(input())
        if num2 == 0:
            print("Invalid Operation")
        else:
            print(num1 % num2)