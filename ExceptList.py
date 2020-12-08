class ExceptList:
  def get_exceptmenu_choice(self): 
    def print_exceptmenu():
      print('')
      print(28 * "-", "EXCEPTIONS MENU", 28 * "-")
      print("Options 1, 8, and 10 currently operational.\n")
      print("1. Type Error")
      print("2. Stop Async Iteration")      
      print("3. Stop Iteration")
      print("4. Import Error")
      print("5. OS Error")
      print("6. EOF Error")
      print("7. Runtime Error")      
      print("8. Name Error")
      print("9. AttributeError")
      print("10. Syntax Error")
      print("11. Lookup Error")
      print("12. Value Error")      
      print("13. Assertion Error")
      print("14. Arithmetic Error")
      print("15. System Error")
      print("16. Reference Error")
      print("17. Memory Error")      
      print("18. Buffer Error")
      print("19. Warning")
      print("20. _Option Error")
      print("21. error")
      print("22. Verbose")
      print("23. Error")
      print("24. Token Error")
      print("25. Stop Tokenizing")
      print("26. End of Block")
      print("27. Back to Main Menu")
      print(73 * "-")
      print("\n")


    while True:
      print_exceptmenu()
      choice = input("Enter your choice [1-27]: ")

      if choice == '1':
        print("""
        code:
          run = 1
          while run == 1:      
            
            while True:
              try:
                blocks = int(input("Enter the number of blocks: "))
                break
              except ValueError:
                print("The value entered was not an integer. Please reenter your value.")
            
            height = 0
            inLayer = 1

            while inLayer <= blocks:
              height += 1
              blocks -= inLayer
              inLayer += 1

            print("The height of the pyramid:", height)
            redo = (input('Would you like to recalculate?(y/n): '))
            redo = redo.upper()
            while redo not in 'YN':
              
                redo = input('Please enter either "y" to run the program again, or "n" to stop the program.','\\nWould you like to recalculate?(y/n): ').upper()

            if redo == 'Y':
                run = 1
            elif redo == 'N':
                run = 0


        Error message:
          Traceback (most recent call last):
            File "main.py", line 21, in <module>
              labs.runlab3_1_2_14()
            File "/home/runner/ClassFall2020/Labs.py", line 340, in runlab3_1_2_14
            redo = input('Please enter either "y" to run the program again, or "n" to stop the program.','\\nWould you like to recalculate?(y/n): ').upper()
          TypeError: input expected at most 1 argument, got 2


        Solution: Remove the comma from inside the input statement and take away the middle 2 apostrephes.\n""")
      elif choice == '8':
        print("""
        Code:
          print(Kane)
        Error message:
              Traceback (most recent call last):
            File "main.py", line 6, in <module>
              labs.runlab2_1_1_7()
            File "/home/runner/DaringAwfulAggregators/Labs.py", line 11, in runlab2_1_1_7
              print(Kane)
          NameError: name 'Kane' is not defined
        Solution: Add quotations around the word Kane, and inside of the parenthesis.


        Code:
          Print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\n'*2)
        Error message:
                Traceback (most recent call last):
            File "main.py", line 8, in <module>
              labs.runlab2_1_1_20()
            File "/home/runner/DaringAwfulAggregators/Labs.py", line 50, in runlab2_1_1_20
              Print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\\n'*2)
          NameError: name 'Print' is not defined
        Solution: Uncapitalize the print statement command.\n""")
      elif choice == '10':
        print("""
        Code:
          print'Kane'
        Error message:
              Traceback (most recent call last):
            File "main.py", line 2, in <module>
              from Labs import Labs
            File "/home/runner/DaringAwfulAggregators/Labs.py", line 22
              print'Kane'
                  ^
          SyntaxError: invalid syntax
        Solution: Add parenthesis encasing the apostrphes.


        Code:
          print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,****       *****2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\\n'*2)
        Error message:
              Traceback (most recent call last):
            File "main.py", line 2, in <module>
              from Labs import Labs
            File "/home/runner/DaringAwfulAggregators/Labs.py", line 50
              print("       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,****       *****2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\\n'*2)
                                                                                                      ^
          SyntaxError: invalid syntax
        Solution: Add parenthesis around stars after fourth comma.


        Code:
          print"       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\\n'*2
        Error message:
                Traceback (most recent call last):
            File "main.py", line 2, in <module>
              from Labs import Labs
            File "/home/runner/DaringAwfulAggregators/Labs.py", line 50
              print"       *       "*2,"    *     *    "*2,"  *         *  "*2," *           * "*2,"****       ****"*2,"   *       *   "*2,"   *       *   "*2,"   *********   "*2, sep='\\n'*2
                  ^
          SyntaxError: invalid syntax
        Solution: Add parenthesis around entire print statment.


        code:
          hatList = [1, 2, 3, 4, 5]

          print('Please choose a number to add to the hat: '), newHatNum = input()
          hatList[2] = newHatNum
          

          # Step 3: write a line of code here that prints the length of the existing list.

          print(hatList)
        Error message:
              Traceback (most recent call last):
            File "main.py", line 2, in <module>
              from Labs import Labs
            File "/home/runner/ClassFall2020/Labs.py", line 356
              print('Please choose a number to add to the hat: '), newHatNum = input()
              ^
          SyntaxError: cannot assign to function call
        Solution: Add a statement asking for a kind of input followed by a comma all inside the parenthesis.\n""")
        
      elif choice == '2':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '3':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '4':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '5':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '6':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '7':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '9':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '10':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '11':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '12':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '13':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '14':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '15':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '16':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '17':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '18':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '19':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '20':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '21':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '22':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '23':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '24':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '25':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '26':
        print('This section is currently under development. Please check back at another time.\n')
      elif choice == '27':
        print("\nExiting..")
        return '\n'
        break
      else:
        print("\nWrong menu selection. Please enter a number from 1-27")
    


