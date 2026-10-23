from pathlib import Path

path = Path('learning_python.txt')

content = path.read_text()

for line in content.splitlines():

 change = line.replace('python', 'c')

 print(change)

