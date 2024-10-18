# Get the user's name
name = input("Enter name: ")

# Display the menu
menu = """(H)ello
(G)oodbye
(Q)uit"""
print(menu)

choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    print(menu)
    choice = input(">>> ").upper()
print("Finished.")
