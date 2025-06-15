from pathlib import Path

print("Enter 'q' to quit the program anytime.\n")
guest_book = ''
while True:
    guest = input("What is your name? ")
    guest_book += f"{guest}\n"
    if guest == 'q':
        break

guest_book = guest_book.replace('q', '')
path = Path('guest_book.txt')
path.write_text(guest_book)
