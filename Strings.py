# to try: https://dbader.org/blog/bpython-a-better-python-repl
# concatenate strings
s = 'spam'
t = 'egg'
u = 'bacon'

print(s + t)
print(s + t + u)
print('lalalala ' + 'song')

# Multiply string

n = 8
s * 8

print(n*s)

# This will result with empty string:

print(s * -7)
print(s * 0)

# The in and not in operators provide boolean testing of membership within a string:

print(s in 'spam am am spam lam spam')

print(s not in 'spam am am spam lam spam')

# Built-in string functions
# chr() - converts an integer to a character
# ord() converts a char to an int
# len() 
# str() - creates a new string object from the given object

print(ord('a')) # returns unicode value
print(ord(' '))

print(chr(97)) # returns unicode char

print(len('Lambada'))

print(str(49.2))
a = (str(3 + 29))
print(a)
print(type(a))