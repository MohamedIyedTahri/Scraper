from bs4 import BeautifulSoup
from selenium import webdriver

# Enter A url
url = "Some URL"
# Navigate to the webpage
driver.get(url)

# Get the HTML content of the webpage
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <strong> tags(Data are stored in <strong> tag ) 
strong_tags = soup.find_all('strong')

# Extract and print the contents within the <strong> tags
for tag in strong_tags:
    print(tag.get_text())

# Close the browser
driver.quit()
