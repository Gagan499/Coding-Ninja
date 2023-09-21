n = (input())                    # not   n = int(input())   as 'int' object is not iterable
even_sum = 0
odd_sum = 0

for digit in n:                  #iterating n
    if int(digit) % 2 == 0:       
        even_sum += int(digit)
    else:
        odd_sum += int(digit)

print(f" {even_sum}  {odd_sum}")
