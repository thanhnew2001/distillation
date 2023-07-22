from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test_case():
    # Set up the WebDriver instance (in this example, we'll use Chrome)
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Open the URL
        driver.get("https://congbobanan.toaan.gov.vn/0tat1cvn/ban-an-quyet-dinh")

        # Find the element using JavaScript and click on it
        element = driver.find_element(By.ID, "ctl00_Content_home_Public_ctl00_Rad_DATE_FROM_top")
        driver.execute_script("arguments[0].click();", element)

        # Command: type
        element.clear()
        element.send_keys("01/01/2000")

        # Command: type
        element.clear()
        element.send_keys("01/01/2013")

        # Command: click
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".row:nth-child(6) > .col-sm-4:nth-child(3)")))
        element.click()

        # Wait for the modal to be hidden or removed
        wait.until(EC.invisibility_of_element_located((By.ID, "popModal")))

        # Command: click
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_Content_home_Public_ctl00_Drop_CASES_STYLES_SEARCH_top")))
        element.click()

        # Command: select
        element = wait.until(EC.element_to_be_clickable((By.ID, "ctl00_Content_home_Public_ctl00_Drop_CASES_STYLES_SEARCH_top")))
        element.find_element(By.XPATH, "//option[text()='Dân sự']").click()

        # Rest of the commands...

    finally:
        # Close the browser after the test is complete
        driver.quit()

# Run the test case
run_test_case()
