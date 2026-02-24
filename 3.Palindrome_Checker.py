def check_palindrome():
    user_input = input("Enter a string: ").strip().lower()
    clean_text = "".join(char for char in user_input if char.isalnum())
    
    if clean_text == clean_text[::-1]:
        print(f"The string '{user_input}' is a palindrome.")
    else:
        print(f"The string '{user_input}' is not a palindrome.")

if __name__ == "__main__":
    check_palindrome()


    