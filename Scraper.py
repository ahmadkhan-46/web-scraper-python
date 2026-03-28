import time
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

base_url = "https://example.com/regions"
driver.get(base_url)
time.sleep(3)

regions = driver.find_elements(By.CLASS_NAME, "region-link")

data = []

for region in regions:
    region.click()
    time.sleep(2)

    companies = driver.find_elements(By.CLASS_NAME, "company-link")

    for company in companies:
        company.click()
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        name = soup.find("h1").text
        industry = soup.find("div", class_="industry").text

        data.append({
            "name": name,
            "industry": industry
        })

        driver.back()
        time.sleep(1)

    driver.back()

# Save CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

# Save JSON
with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

driver.quit()
