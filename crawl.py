import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_pdf(url, save_directory):
    response = requests.get(url, stream=True, verify=False)  # Disable SSL certificate verification
    if response.status_code == 200:
        file_name = os.path.basename(url)
        file_path = os.path.join(save_directory, file_name)
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        print("Downloaded: {}".format(url))
    else:
        print("Failed to download: {}".format(url))

def crawl_website_for_pdfs(base_url, save_directory):
    response = requests.get(base_url, verify=False)  # Disable SSL certificate verification
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            link_url = urljoin(base_url, link['href'])
            if link_url.lower().endswith('.pdf'):
                download_pdf(link_url, save_directory)
    else:
        print("Failed to fetch website: {}".format(base_url))

if __name__ == "__main__":
    website_url = "https://congbobanan.toaan.gov.vn/0tat1cvn/ban-an-quyet-dinh"  # Replace with the URL of the website you want to crawl
    save_directory = "pdf_files"  # Replace with the directory where you want to save the downloaded PDFs

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    crawl_website_for_pdfs(website_url, save_directory)
