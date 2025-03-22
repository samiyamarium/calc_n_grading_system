from colorama import Fore,Back,Style

choice=[80,70,60,50,40]
while True:
  Percentage=float(input(Style.BRIGHT+Back.LIGHTGREEN_EX+Fore.MAGENTA+"Enter your percentage == "))
  print(Percentage)



  if Percentage>=choice[0]:
    print("You are placed in grade : A+ \n")
  elif Percentage>=choice[1]:
    print("You are placed in grade : A \n")
  elif Percentage>=choice[2]:
    print("You are placed in grade : B \n")
  elif Percentage>=choice[3]:
    print("You are placed in grade : C \n")
  elif Percentage>=choice[4]:
    print("You are placed in grade : D \n")
 
  else:
    print("Try again!!")
 
  




