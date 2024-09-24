import requests
from bs4 import BeautifulSoup

url = 'http://122.102.49.131/audition/abm/' 

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

file_names = []

for link in soup.find_all('a'):
    file_name = link.get('href')
    if file_name:
        file_names.append(file_name)

output_file = 'Result ABM.txt'

with open(output_file, 'w') as file:
    for file_name in file_names:
        file.write(file_name + '\n')
        
file_path = 'Result ABM.txt'

with open(file_path, 'r') as file:
    content = file.read()

replacements = {
    '/audition/abm/': '',
    '/audition/': '',
    'PackageInfo.txt': '',
    'music.amp': '',
}

new_content = content
for old_text, new_text in replacements.items():
    new_content = new_content.replace(old_text, new_text)
    
lines = new_content.split('\n')
non_empty_lines = [line for line in lines if line.strip() != '']
new_content = '\n'.join(non_empty_lines)

with open(file_path, 'w') as file:
    file.write(new_content)

print(f"Scraping successfully !\n\nOutput file saved in {output_file}")
input()