# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#   print("esse é o primeiro print")
#   print ("esse é o segundo print")
#   print("Finalmente o terceiro print")
#
#
# greet()

# function that allows for input

# def greet_with_name(name):
#   print(f"hello {name}")
#   print(f"How do you fo {name}")
#
# greet_with_name("Marco")

#Functions with more than 1 input

# def greet_with(name, location):
#     print(f"Helo {name}")
#     print(f"What is it like in {location}")
#
# greet_with(location="santos", name="marco")
#
#
#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
#'name' is the parameter.
#'Jack Bauer' is the argument.
def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
greet_with_name("Jack Bauer")

#Functions with more than 1 input
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}?")

#Calling greet_with() with Positional Arguments
greet_with("Jack Bauer", "Nowhere")
#vs.
greet_with("Nowhere", "Jack Bauer")


#Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")