import re

with open('id-dashboard.svg', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace texts
replacements = {
    'FRONTEND DEVELOPER': 'FULL STACK DEV',
    'FRONTEND': 'FULL STACK',
    'Noida, IN': 'India',
    'Wiley': 'Kodeleaf',
    'MM-0920': 'SC-19',
    '2022': '2023'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open('id-dashboard.svg', 'w', encoding='utf-8') as f:
    f.write(content)
print("ID dashboard updated")
