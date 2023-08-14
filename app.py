import tkinter as tk
import subprocess
import os
from datetime import datetime
import webbrowser

from bs4 import BeautifulSoup

# Define the function to handle the button click
def get_url():
    url = entry.get()
    # Generate a unique filename based on the current timestamp
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'article_{now}.html'
    # Run the curl command in the terminal to save the response as an HTML file
     
    fileUrlToSaveTo = os.path.join(os.path.abspath(os.getcwd()),'articles', filename)

    command = f'curl {url} >> {fileUrlToSaveTo}'
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f'Error: {e}')
    print(f'Response saved as {fileUrlToSaveTo}')
    filepath = os.path.join(os.path.abspath(os.getcwd()),'articles', filename)
    webbrowser.open(filepath)

    # Remove script tags from the saved HTML file
    with open(fileUrlToSaveTo, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    soup = BeautifulSoup(html_content, 'html.parser')
    for script in soup.find_all('script'):
        script.extract()
    
    cleaned_html = str(soup)
    
    with open(fileUrlToSaveTo, 'w', encoding='utf-8') as file:
        file.write(cleaned_html)
    
    filepath = os.path.join(os.path.abspath(os.getcwd()),'articles', filename)
    webbrowser.open(filepath)

# Create the GUI window
window = tk.Tk()
window.title('Get URL')

# Create the input field for the URL
entry = tk.Entry(window, width=50)
entry.pack()

# Create the button to submit the URL
button = tk.Button(window, text='Submit', command=get_url)
button.pack()

# Start the main event loop
window.mainloop()
