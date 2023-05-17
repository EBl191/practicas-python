from pathlib import Path
import json

path = Path('favnumber.json')
contents = input('What is your favorite number?: ')
path.write_text(contents)
favnumber = json.dumps(contents)

print(f"Now we know which is your favorite number: {favnumber}, we'll remember it when you come back!")