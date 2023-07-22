import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def download_pdf(url, save_directory):
    driver = webdriver.Chrome()  # Replace 'Chrome' with 'Firefox' if you're using Firefox
    driver.get(url)
    
    # Wait for the page to load and render dynamic content (adjust the wait time as needed)
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'a')))

    # Get all the links on the page
    #links = driver.find_elements_by_tag_name('a')

    for link in links:
        link_url = link.get_attribute('href')
        if link_url and link_url.lower().endswith('.pdf'):
            file_name = os.path.basename(link_url)
            file_path = os.path.join(save_directory, file_name)
            link.click()  # Click the link to trigger the download
            time.sleep(2)  # Wait for the download to complete (adjust the wait time as needed)

            # Move the downloaded file to the desired location
            os.rename(os.path.expanduser('~') + '/Downloads/' + file_name, file_path)

            print("Downloaded: {}".format(link_url))

    driver.quit()

if __name__ == "__main__":
    website_url = "https://congbobanan.toaan.gov.vn/0tat1cvn/ban-an-quyet-dinh"  # Replace with the URL of the website you want to crawl
    save_directory = "pdf_files"  # Replace with the directory where you want to save the downloaded PDFs

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    download_pdf(website_url, save_directory)
