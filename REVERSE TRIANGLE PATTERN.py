# Get the number of rows from the user
n = int(input())

# Initialize an empty string to store the pattern


# Loop from n to 1
for i in range(0, n, +1):       #if done 1 istead 0 error will come
  # Loop from 1 to i
  for j in range(1,n+1-i,+1 ):
    # Append j to the pattern
    print(j,end="")
  # Append a newline character to the pattern
  print()

#   OR

# # Get the number of rows from the user
# n = int(input())

# # Initialize an empty string to store the pattern
# pattern = ""

# # Loop from n to 1
# for i in range(n, 0, -1):
#   # Loop from 1 to i
#   for j in range(1, i+1):
#     # Append j to the pattern
#     pattern += str(j)
#   # Append a newline character to the pattern
#   pattern += "\n"

# # Print the pattern
# print(pattern)
