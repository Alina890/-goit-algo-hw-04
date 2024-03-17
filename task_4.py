
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
        name, phone = args
        if name not in contacts:
            contacts[name] = phone 
            return "Contact added."
        else:
            print ("Перевірте вірність введених даних")
      

def change_contact(args, contacts):
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated." 
        else:
            print ("Перевірте вірність введених даних")
     

def show_phone(args,contacts):
        name = args[0]
        if name in contacts:
            print (contacts[name])
        else: 
            print ("Користувача з таким іменем не знайдено, перевірте вірність введених даних")
    

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
            return (contacts)
    else:
        print ("Список контактів порожній")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

