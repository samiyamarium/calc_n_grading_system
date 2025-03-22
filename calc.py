from colorama import Fore,Back,Style,colorama_text
a=float(input(Fore.GREEN+"First number=="))
b=float(input(Fore.LIGHTMAGENTA_EX+"Second number=="))
def display_menu():
  
    print(Fore.YELLOW+Back.WHITE+"==== ****CALCULATOR**** ====")
    print("1. Add ")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exit")
    print("======================")

def main():
    """Main function to run the menu and handle user input"""
    while True:
       
        
        choice = input(Back.LIGHTYELLOW_EX+"Please select an option (1-5): ")

        if choice == '1':
            print(f"Addition ==> {a} + {b} == ",a+b)
        elif choice == '2':
            print(f"Subtraction==>{a} - {b} == ",a-b)
        
        elif choice == '3':
            print(f"Multiplication==>{a}*{b} == ",a*b)
        elif choice == '4':
            print(f"Division==> {a}/{b} ==",a/b)
        elif choice == "5":
            print(f"Modulus==> {a}%{b} == ", a%b)
        elif choice == '6':
            print(Style.DIM+"Exit...")
            break
        else:
            print("Try again!!")

display_menu()
main()