"""
Skills function assessment.

Please read the instructions first. Your solutions should
go below this docstring.

"""

###############################################################################


# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own.

   # 1.  Write a function that takes a town name as a string and returns
   #     `True` if it is your hometown, and `False` otherwise.

def home_town(town):
   """Evaluates if town is equal to hometown"""
   hometown = 'Petaluma'

   return hometown == town 



def full_name(first_name, last_name):
   """Concatenates first name and last name and returns a full name"""

   return first_name + " " + last_name

  
def greeting(town, first_name, last_name):
   """Prints greeting based on comparison of hometown"""

   user_hometown = home_town(town)
   user_name = full_name(first_name, last_name)
   
   if user_hometown:
      print("Hi {}, we're from the same place!".format(user_name))

   else:
      print("Hi {}, I'd like to visit {}!".format(user_name, town))

 
def is_berry(fruit):
   """Evaluates if fruit is a berry"""

   return fruit in ["strawberry","raspberry","blackberry","currant"]

  
def shipping_cost(fruit):
   """Calculates shipping cost by fruit type"""

   if is_berry(fruit):
      return 0

   else:
      return 5


def fruits(fruit_list, fruit):
   """Returns a new list of fruits with input list and additional fruit"""

   updated_fruits_list = []
   for item in fruit_list:
      updated_fruits_list.append(item)
   updated_fruits_list.append(fruit)

   return updated_fruits_list



def calculate_price(base,state,tax=.05):
   """Calculates total of item based on state taxes and fees"""

   total = base + float(base * tax)
   print(total)

   if state == "CA":
      total = total + float(total * .03)

   elif state == "PA":
      total = total + float(total + 2) 

   elif state == "MA":
      if total < 100:
         total = float(total + 1)
      else:
         total = float(total + 3)

   return total 






