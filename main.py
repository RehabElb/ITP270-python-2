#print("hello print")


# my_name = "Rehab"

#how to print an aoutput to the terminal
print("Rehab")

#how to declare or initiate a variable
#name_of_the_variable = value
name = "Rehab"
age = 7
instructor = True
credits = 12.00

# if instructor:
#   print("Yes!")

# an_int=2
# a_float=2.2

# sum=an_int + a_float
# divisions = a_float/an_int
# modules=an_int % a_float

#print(divisions)
#decide=int(divisions)
#print(decide)
#print(modules)
#print(sum)
# if decide == 1.0:
#   print("go out and the decision value is " + str(decide))
# else:
#   print("stay at home")

#check the type of the data
an_integ=6
#print(type(an_integ))

a_float=6.80
#print(type(a_float))

a_bool=False
#print(type(a_bool))

a_string= "Rehab"
#print(type(a_string))

first= "hello "
second="world"
greetings= first + second
#print(greetings)


#print(int(25*68+13/28))

#print(6**2)
#print(2**4)


#if condition1:
#  print("message")
#elif condition2:
#  print("message 2")
#else:
   #print("another message")

age_x=17
age_y=9
age_z=11

#>, <, >=, <=, ==, !=
# and, or, not

if age_x > age_y:
  if age_x > age_z:
    print("oldest is x")
  else:
    print("oldest is z")
else:
  if age_y > age_z:
    print("oldest is y")
  else:
    print("oldest is z")


if age_x > age_y and age_x > age_z:
  print("oldest is x")
elif age_y > age_x and age_y > age_z:
  print("oldest is y")
else:
  print("oldest is z")