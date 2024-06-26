
def print_menu():
    print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
""")


def main():
    encoded = ""
    while True:
        print_menu()
        choice = input("Please enter an option: ")
        if choice == "1":
            password = input("Please enter your password to encode: ")
            for char in password:
                encoded += str(int(char) + 3)
            print("Your password has been encoded and stored")
        if choice == "2":
            decode = ""
            for char in encoded:
                decode += str(int(char) - 3)
            print(f"the encoded password is {encoded}, the original password is {decode}")
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
