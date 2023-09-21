# Get the value of N from user input
N = int(input())

# Outer loop to iterate from 1 to N
for i in range(1, N + 1):
    # Calculate the character 'a' based on the current value of 'i'
    a = chr(ord('A') + i - 1)

    # Inner loop to print characters in the current row
    for j in range(1, i + 1):
        # Calculate the character 'b' based on 'a' and the current value of 'j'
        b = chr(ord(a) + j-1 )

        # Print the character 'b' without a newline and end with an empty string to prevent a newline
        print(b, end='')

    # Print a newline to move to the next row
    print()
