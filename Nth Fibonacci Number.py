n=int(input())       #n = int(input()): This line takes an input integer n from the user,
                            # representing the position of the Fibonacci number to be calculated.
a=1      #a is initialized to 1, representing the Fibonacci number at position 1
b=1      #b is initialized to 1 as well, representing the Fibonacci number at position 2
c=1      #c is initialized to 1; this will be used to calculate the next Fibonacci number.
i=3     #Initialize i to 3. This variable will be used to keep track of the position of the 
          #Fibonacci number currently being calculated.
while i<=n: #Enter a while loop that continues until i is greater than n. This loop will 
                  #calculate Fibonacci numbers until the desired position n is reached.
   c=a+b
   a=b
   b=c
   i=i+1
print(c)
# #Inside the loop:
# Calculate the next Fibonacci number c as the sum of the previous two Fibonacci numbers
#  a and b.This corresponds to the Fibonacci recurrence relation: F(n) = F(n-1) + F(n-2).

# Update a and b to hold the values of the last two Fibonacci numbers for the next iteration.

# Increment i by 1 to move to the next position