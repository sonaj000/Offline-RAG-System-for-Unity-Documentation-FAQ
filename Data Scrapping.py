from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import requests
from bs4 import BeautifulSoup

# Set up WebDriver
options = webdriver.ChromeOptions()
#options.add_argument('--headless') for headless mode for efficiency
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")
service = Service("C:\\Users\\Jason\\Downloads\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

url = "https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Classes"

driver.get(url)

# Wait up to 10 seconds for the page to load and links to become available
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a[href^='/documentation/en-us/unreal-engine/API/']"))
)

html = driver.page_source
#now to iterate over 

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(html, "html.parser")
print("soup is parsed to beautiful soup")
# Find all class links
class_links = soup.find_all("a", href=True)
print(f"Total links found: {len(class_links)}")
# Filter links that point to class documentation

filtered_links = [link for link in class_links if "/documentation" in link['href']]
test = filtered_links[1]
class_name = test.text.strip()
class_url = test['href']
if not class_url.startswith("http"):
    class_url = "https://dev.epicgames.com" + class_url
 #print(f"Class Name: {class_name}, URL: {class_url}")
    driver.get(class_url)
        # Random delay to mimic human behavior

    time.sleep(random.uniform(2, 5))

    # Wait for the page to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.TAG_NAME, "references"))
    )

    # Parse the page
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")

    # Try to find the 'p' tag with id 'references'
    reference_element = soup.find('p', id='references')

    # Extract and strip text if the element is found
    if reference_element:
        class_name = reference_element.text.strip()
    else:
        class_name = "No Class Name"

    print(f"Class Name: {class_name}")

            # Extract class name or description
    class_name = soup.find("h1").text.strip() if soup.find("h1") else "No Class Name"
    print(f"Class Name: {class_name}")

