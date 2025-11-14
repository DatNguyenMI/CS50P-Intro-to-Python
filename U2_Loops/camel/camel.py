

def main():
   snake = []
   camelcase = input ("camelCase: ")
#loop via each char in string
   for char in camelcase:
      if char.isupper():  #return True if you found a capital letter
         snake.append ("_") #first add _
         snake.append (char.lower()) #second add the char as lower case to the list
      else:
         snake.append (char) #just return the char as is
   snake_final = "".join(snake) #join the list to become a string with Join function with ""no space in between
   print (f"snake_case: {snake_final}") #print the comment and the {string variale}

main()

