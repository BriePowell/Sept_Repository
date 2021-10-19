#!/usr/bin/env python
# coding: utf-8

# # Exercises - Due 9.23.21

# ### 1) Build a Shopping Cart <br>
# <p><b>You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
# 1) Takes in input <br>
# 2) Stores user input into a dictionary or list <br>
# 3) The User can add or delete items <br>
# 4) The User can see current shopping list <br>
# 5) The program Loops until user 'quits' <br>
# 6) Upon quiting the program, print out all items in the user's list <br>
# </p>

# In[30]:


from IPython.display import clear_output

#IF YOU RUN INTO PROBLEMS: start from the top, ask what this line does,
#How does it relate to the preceeding or following lines
#Is there an unanticipated break/inturuption/missing-start?
#Do I fully understand this process, start to end?

  #Global
     


def prompt():
    ask = input ('Hello shopper! To modify your cart, simply "add" or "remove" items.\n' 'To view your list simply type "show" in the terminal.\n'
      'Reply "quit" to check out.\n')
    
    if ask.lower() == 'add':
        return input('What would you like to add to your cart?')
    
    elif ask.lower() == 'remove':
        return input ('What would you like to remove from your cart?')
    
    elif ask.lower() == 'show':
        print(my_cart)

    elif ask.lower() == 'quit':
        break
    

    def shop():
        my_cart = []

        'ask' == my_cart.append()
        'remove' == my_cart.remove()

            
                
            
return shop()


prompt()


# ### 2) Create a Module in VS Code and Import It into jupyter notebook <br>
# <p><b>Module should have the following capabilities:</b><br><br>
# 1) Has a function to calculate the square footage of a house <br>
#     <b>Reminder of Formula: Length X Width == Area<br>
#         <hr>
# 2) Has a function to calculate the circumference of a circle <br><br>
# <b>Program in Jupyter Notebook should take in user input and use imported functions to calculate a circle's circumference or a houses square footage</b>
# </p>

# In[12]:


import area_module
#print(area_module)

from area_module import circ

circ(9)

from area_module import house_footage

house_footage(75, 90)

