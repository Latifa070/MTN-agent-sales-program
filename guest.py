from pathlib import Path

path = Path('guest.txt')
name = input("Enter your name :")
content = path.write_text(name)

print(content)