from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.dell.com/support/home/en-us"
driver.get(url)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "img")))
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

images = driver.find_elements(By.TAG_NAME, "img")
image_data = []
for img in images:
    src = img.get_attribute("src")
    alt = img.get_attribute("alt") or "No Alt Text"
    image_data.append({"src": src, "alt": alt})

links = driver.find_elements(By.TAG_NAME, "a")
link_data = []
for link in links:
    text = link.text.strip() if link.text.strip() else link.get_attribute("aria-label")
    href = link.get_attribute("href")
    if href:
        link_data.append({"href": href, "text": text})

buttons = driver.find_elements(By.TAG_NAME, "button")
button_data = []
for btn in buttons:
    text = btn.text.strip() if btn.text.strip() else btn.get_attribute("aria-label")
    if text:
        button_data.append({"text": text})

driver.quit()

log_file = "dell_support_page_log.txt"

with open(log_file, "w", encoding="utf-8") as f:
    f.write("=== Images ===\n")
    for img in image_data:
        f.write(f"Src: {img['src']}, Alt: {img['alt']}\n")

    f.write("\n=== Hyperlinks ===\n")
    for link in link_data:
        f.write(f"Text: {link['text']}, Href: {link['href']}\n")

    f.write("\n=== Buttons ===\n")
    for btn in button_data:
        f.write(f"Text: {btn['text']}\n")

print(f"Data extracted and saved to {log_file}")