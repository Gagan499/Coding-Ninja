def swapAlternate(arr, n):
    length = len(arr)
    if length == 1:
        print(arr)
    else:
        for i in range(0, length-1, 2):
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = temp
#r.strip   strip() is a string method that is used to remove leading and trailing characters from a string.
# The strip() method returns a copy of the string with any specified leading (spaces by default) and trailing characters removed


#Here, input() is used to take user input. rstrip() is then called on the input string. 
#This removes any leading or trailing whitespace characters (like spaces, tabs, or newlines) before converting the input to an integer using int()
def takeInput():
    n = int(input().rstrip())

    if n == 0:
        return list(), 0

    arr = list(map(int, input().rstrip().split(" ")))#Overall, this line of code is taking a space-separated input from the user,
                                                                      #converting it into a list of integers, and assigning it to the variable arr. 
                                                                      #For example, if the user enters "1 2 3", arr will be [1, 2, 3].
    return arr, n

def printList(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

t = int(input().rstrip())

while t > 0:
    arr, n = takeInput()
    if n != 0:
        swapAlternate(arr, n)
        printList(arr, n)
    t -= 1
