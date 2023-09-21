# Get the value of N from user input
n = int(input())

# Initialize the outer loop counter i to 1
i = 1

# Outer loop to iterate from 1 to N
while i <= n:
    # Initialize the inner loop counter j to 1
    j = 1

    # Calculate the character 'a' based on the current value of 'i'
    a = chr(ord('A') + i - 1)

    # Inner loop to print characters in the current row
    while j <= i:
        # Calculate the character 'b' based on 'a' and the current value of 'j'
        b = chr(ord(a) + j - 1)

        # Print the character 'b' without a newline and end with an empty string to prevent a newline
        print(b, end='')

        # Increment the inner loop counter j
        j = j + 1

    # Print a newline to move to the next row
    print()

    # Increment the outer loop counter i
    i = i + 1
