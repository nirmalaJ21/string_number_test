#1.1

str1 ='\tExercise 1.1 Print Text'
print(str1.title())
print('*' * 50)
user_str = input('\nPlease enter any string')
print(user_str.capitalize())
print('*' * 50)
#1.2
str1 ='\tExercise 1.2 take number and print added with 1'
print(str1.title())
num = int(input('\nEnter a number:'))
print('Sum is:{} '.format(num+1).strip())
print('*' * 50)
#1.3
str1 ='\tExercise 1.3 take float number and print added with .5'
print(str1.title())
print('*' * 50)
float_num = float(input('\nEnter a float number'))
print('Result number is:{} '.format(float_num+.5).strip())
print('*' * 50)

#1.4
str1 ='\tExercise 1.4 take 2 float numbers and print sum'
print(str1.title())
print('*' * 50)
float_num1 = float(input('\nPlease enter first float number>>'))
float_num2 = float(input('Please enter second float number>>'))
print('Sum of float  numbers are : {}  '.format(float_num1 + float_num2).strip())
print('*' * 50)
#1.5
str1 ='\tExercise 1.5 take 2 numbers and print product'
print(str1.title())
print('*' * 50)
float_num3 = float(input('\nplease enter first  number>>'))
float_num4 = float(input('please enter second  number>>'))
print('Product of  numbers are :{}  '.format(float_num3 * float_num4).strip())
print('*' * 50)

#1.6
str1 ='\tExercise 1.6 take 2 numbers and print division result'
print(str1.title())
print('*' * 50)
num1 = float(input('\nplease enter first number>>'))
num2 = float(input('please enter second  number>>'))
print('The result  is:{} : '.format(num1 / num2).strip())
print('*' * 50)

#1.7
str1 ='\tExercise 1.7 take boolean value and print opposite of it'
print(str1.title())
print('*' * 50)
bol_val = bool(input('\n Please enter boolean value'))

print('You entered >{}'.format(bol_val))
print('The opposite of what you entered is>{}:'.format(bol_val))



