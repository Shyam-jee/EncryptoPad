import os

def display_menu():
    print("\nEnter:\n")
    print("1. Create a new file")
    print("2. Open and read a file")
    print("3. Edit an existing file")
    print("4. Encrypt a file")
    print("5. Decrypt a file")
    print("6. Find and replace in a file")
    print("7. Delete a file")
    print("8. Exit")
    choice = input("Choose an option (1-8): ")
    return choice
# ------------------------------------------------------------------------------------------------------------------------------------
def create_file():
    filename = input("Enter the filename (with extension, e.g., file.txt): ")
    if os.path.exists(filename):
        print("File already exists. Please choose another name.")
    else:
        with open(filename, 'w') as file:
            print("Enter your text (type 'EOF' on a new line to save and exit):")
            while True:
                line = input()
                if line == "EOF":
                    break
                file.write(line + "\n")
        print(f"File '{filename}' created successfully.")
# ------------------------------------------------------------------------------------------------------------------------------------
def read_file():
    filename = input("Enter the filename to read: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            print("\nFile content:")
            print(file.read())
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def edit_file():
    filename = input("Enter the filename to edit: ")
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            print("Enter text to append (type 'EOF' on a new line to save and exit):")
            while True:
                line = input()
                if line == "EOF":
                    break
                file.write(line + "\n")
        print(f"Changes saved to '{filename}'.")
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def encrypt_file():
    filename = input("Enter the filename to encrypt: ")
    if os.path.exists(filename):
        shift=int(input("Enter your key to Encrypt the file : "))
        with open(filename, 'r') as file:
            text = file.read()
            result = ""
            for i in range(len(text)):
                char = text[i]
                if char.isupper():
                    result += chr((ord(char) + shift - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) + shift - 97) % 26 + 97)
                else:
                    result += char
        with open(filename, 'w') as file:
            file.write(result)
        print(f"File '{filename}' encrypted successfully!")
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def decrypt_file():
    filename = input("Enter the filename to decrypt: ")
    if os.path.exists(filename):
        shift=int(input("Enter your key to Decrypt the file : "))
        with open(filename, 'r') as file:
            text = file.read()
            result = ""
            for i in range(len(text)):
                char = text[i]
                if char.isupper():
                    result += chr((ord(char) - shift - 65) % 26 + 65)
                elif char.islower():
                    result += chr((ord(char) - shift - 97) % 26 + 97)
                else:
                    result += char
        with open(filename, 'w') as file:
            file.write(result)
        print(f"File '{filename}' decrypted successfully!")
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def find_and_replace():
    filename = input("Enter the filename to find and replace text in: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        
        find_text = input("Enter the text to find: ")
        if find_text not in content:
            print(f"'{find_text}' not found in the file.")
            return
        
        replace_text = input("Enter the text to replace it with: ")
        updated_content = content.replace(find_text, replace_text)

        with open(filename, 'w') as file:
            file.write(updated_content)

        print(f"All occurrences of '{find_text}' have been replaced with '{replace_text}' in '{filename}'.")
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def delete_file():
    filename=input("Enter filename to Delete : ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully!")
    else:
        print("File not found.")
# ------------------------------------------------------------------------------------------------------------------------------------
def main():
    print("Welcome to EncryptoPad")
    while True:
        choice = display_menu()
        if choice == "1":
            create_file()
        elif choice == "2":
            read_file()
        elif choice == "3":
            edit_file()
        elif choice == "4":
            encrypt_file()
        elif choice == "5":
            decrypt_file()
        elif choice == "6":
            find_and_replace()
        elif choice == "7":
            delete_file()
        elif choice == "8":
            print("Exiting EncryptoPad. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()