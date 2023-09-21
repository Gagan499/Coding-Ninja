def check_palindrome(string):
   reversed_string=string[::-1]
      if string==reversed_string:
         print(string, "is a palindrome")
      else:
         print(string, "is not a Palindrome")

if name=='main':
   check_palindrome("RADAR")
   check_palindrome("PythonPool")