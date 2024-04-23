from bs4 import BeautifulSoup
from selenium import webdriver

# Enter A url
url = "https://www.flashscore.com/match/UuEjwOGt/#/match-summary/match-statistics/0"

# Create a new ChromeDriver instance
driver = webdriver.Chrome('C:/Users/DELL/Desktop/chromedriver/chromedriver')
# Navigate to the webpage
driver.get(url)

# Get the HTML content of the webpage
html = driver.page_source

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all <strong> tags
strong_tags = soup.find_all('strong')

# Extract and print the contents within the <strong> tags
for tag in strong_tags:
    print(tag.get_text())

# Close the browser
driver.quit()
