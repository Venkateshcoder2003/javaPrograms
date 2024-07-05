import pyperclip

class MultiClipboard:
    def __init__(self):
        self.clipboard_entries = []

    def copy_selected(self, index):
        if 0 <= index < len(self.clipboard_entries):
            entry = self.clipboard_entries[index]
            pyperclip.copy(entry)
            print("Copied:", entry)

    def paste_selected(self):
        entry = pyperclip.paste()
        self.add_to_list(entry)
        print("Pasted and added to clipboard:", entry)

    def clear_list(self):
        self.clipboard_entries.clear()
        print("Clipboard cleared.")

    def add_to_list(self, entry):
        if entry:
            self.clipboard_entries.append(entry)
            print("Added:", entry)
            self.print_list()

    def print_list(self):
        print("\nClipboard Entries:")
        for index, entry in enumerate(self.clipboard_entries):
            print(f"{index}. {entry}")

def main():
    clipboard = MultiClipboard()

    while True:


        choice = input("Enter your choice: ")

        if choice == "1":
            index = int(input("Enter the index of the entry to copy: "))
            clipboard.copy_selected(index)
        elif choice == "2":
            clipboard.clear_list()
        elif choice == "3":
            entry = input("Enter the new entry: ")
            clipboard.add_to_list(entry)
        elif choice == "0":
            #print_list()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()