import os
from bs4 import BeautifulSoup

def remove_scripts_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup.find_all('script'):
        script.extract()
    return str(soup)

def process_html_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            cleaned_html = remove_scripts_from_html(html_content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_html)
                
            print(f"Processed: {filename}")

def clean_files():
    folder_path = "articles"
    process_html_files(folder_path)
    print("Script removal complete.")

if __name__ == "__main__":
    clean_files()