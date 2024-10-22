# Functions
def take_note():
    note0 = input("Start Taking Notes: ")
    with open("Notes.txt", "a") as Notes:
        Notes.write(note0 + "\n")
    print("Note Saved.")

def show_notes():
    print("Your Notes: \n")
    try:
        with open("Notes.txt", "r") as Notes:
            notes = Notes.readlines()
            for idx, note in enumerate(notes, start=1):
                print(f"{idx}: {note.strip()}")
    except FileNotFoundError:
        print("No notes have been recorded yet.")

def delete_notes():
    show_notes()
    while True:
        try:
            indeks = int(input("Enter the number of the note you want to delete: ")) - 1
            with open("Notes.txt", "r") as Notes:
                Notes0 = Notes.readlines()
            if 0 <= indeks < len(Notes0):
                del Notes0[indeks]
                with open("Notes.txt", "w") as Notes:
                    Notes.writelines(Notes0)
                print("Note deleted.")
                break
            else:
                print("Invalid note number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def delete_all_notes():
    with open("Notes.txt", "w") as Notes:
        pass
    print("All notes deleted.")

def main():
    while True:
        print("""
        1 - Take Note
        2 - Show Notes
        3 - Delete a Note
        4 - Delete All Notes
        5 - Exit
        """)

        choice = input("Select the operation you want to perform: ")

        if choice == "1":
            take_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            delete_all_notes()
        elif choice == "5":
            break
        else:
            print("Invalid Selection! Please try again.")

main()