test_cloudflare_url = 'https://www.shinsei.e-aichi.jp/pref-aichi-police-u/profile/userLogin'
# test_cloudflare_url = 'https://batdongsan.com.vn'
url = f'https://facebook.com/l.php?u={test_cloudflare_url}'
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeService
from selenium.webdriver import ChromeOptions
_service = ChromeService(r'C:\Users\lemon\Desktop\New folder\chromedriver.exe')

options = ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-extensions')
options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-browser-side-navigation')
options.add_argument('--disable-gpu')
driver = Chrome(service=_service)

def open_link_js(driver,link):
    driver.execute_script(f"window.open('{link}', '_blank')")

open_link_js(driver,url)
input("Close")
driver.close()
