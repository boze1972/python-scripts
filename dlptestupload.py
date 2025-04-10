import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up paths
FOLDER_PATH = "C:\Users\fergu\Downloads\dlp"
FILENAME = "sample-data.pdf"
FILE_PATH = os.path.join(FOLDER_PATH, FILENAME)

# Path to ChromeDriver (update this path if necessary)
CHROME_DRIVER_PATH = "C:\Users\fergu\AppData\Local\Programs\Python\Python312\chromedriver_win32"

# Start Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Navigate to DLPT test page
    driver.get("https://dlptest.com/https-post/")

    # Wait for file input element to be present
    wait = WebDriverWait(driver, 10)
    file_input = wait.until(EC.presence_of_element_located((By.NAME, "fileupload")))

    # Upload file (sends the file path directly to the input)
    file_input.send_keys(FILE_PATH)
    print(f"Uploaded: {FILE_PATH}")

    # Click the "Submit" button
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()
    print("Form submitted.")

    # Wait and print the result
    time.sleep(3)
    print("Upload complete. Check browser for result.")

finally:
    # Keep browser open for 10 seconds to see the result, then close
    time.sleep(10)
    driver.quit()
