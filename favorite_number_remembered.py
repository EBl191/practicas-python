from pathlib import Path
import json

path = Path('favnumber.json')
contents = path.read_text()
number = json.loads(contents)

print(f'Hi again! I remember you. Your favorite number is {number}')