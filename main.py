from ExceptList import ExceptList

def get_menu_choice():
  def print_menu():
    print('')
    print(28 * "-", "ERROR MENU", 28 * "-")
    print("1. Exceptions")
    print("2. Generator Exit")      
    print("3. System Exit")
    print("4. Keyboard Interrupt")
    print("5. Exit from the Program")
    print(73 * "-")


  while True:
    exceptlist = ExceptList()
    print_menu()
    choice = input("Enter your choice [1-5]: ")

    if choice == '1':
      exceptlist.get_exceptmenu_choice()
    elif choice == '2':
      print('This section is currently under development. Please check back at another time.\n')
    elif choice == '3':
      print('This section is currently under development. Please check back at another time.\n')
    elif choice == '4':
      print('This section is currently under development. Please check back at another time.\n')
    elif choice == '5':
      print("\nExiting..")
      return '\n'
      break
    else:
      print("\nWrong menu selection. Please enter a number from 1-5")
  

print(get_menu_choice())








