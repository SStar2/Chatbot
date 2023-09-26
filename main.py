print("Welcome to my Elite 101 Chatbox!")

name = input("Please enter your name: ")
user_name = str(name)
print("Hello " + name +"!")


age = input("How old are you? ")
user_age = int(age)
print("So "+ name + ", you're " + str(user_age) + " years old!")
print("Thank you for the information. How can I help you today?")

print("\nPlease choose from the following options")

print("1. Placeholder Option 1")
print("2. Placeholder Option 2")
print("3. Placeholder Option 3")
print("4. Exit the conversation")

def user_selection():
  user_option = int(input("Enter the number of your choice: "))
  if user_option == 4:
    print("You have choosen to exit the Chatbox. Goodbye and have a nice day!")
  elif user_option == 1:
    print('You have choosen Option 1 and here is the response.')
  elif user_option == 2:
    print("You have choosen Option 2 and here is the response.")
  elif user_option == 3:
    print("You have choosen Option 3 and here is the response.")
  else:
    print("That is not a valid option. Please choose one of the four given options.")
user_selection()
    
#For the pull request 




