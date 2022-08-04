import sys
import cmd
import pandas as pd
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

df = pd.read_csv(f"product_translasi.csv")
list_product = df.to_dict('index')

cmd.header()
print("Open/Close Produk Translasi")
print("Silakan pilih function :")
print("1.Close Produk")
print("2.Open Produk")

option = int(input("Pilih : "))

# create webdriver object
driver = webdriver.Edge()
driver.maximize_window()
driver.get("http://117.102.115.218:8031/web-teleshoph2h-v3/login.html")

def closeProduk(kode_internal,mitra,biller):
    select = Select(driver.find_element(By.NAME, 'mykunci'))
    select.select_by_value('3')
    search = driver.find_element_by_name("search")
    driver.execute_script(f"arguments[0].value = '{kode_internal}';",search)
    driver.find_element_by_css_selector('.form-control.btn-danger').click()
    time.sleep(1)

    row = driver.find_elements_by_css_selector("#transproduct>tbody>tr")
    for i in row:
        x = i.find_elements_by_tag_name("td")
        aktif = i.find_element_by_css_selector('.alert h7').get_attribute('innerHTML')
        if x[3].text == mitra and x[6].text == kode_internal and aktif == 'YES' and x[9].text == biller:
            i.find_element(By.XPATH,"./td/div/button[@title='Aktif Translasi Produk']").click()
            time.sleep(1)
            driver.find_element_by_css_selector('.confirm').click()
            break
    time.sleep(2)
    
def openProduk(kode_internal,mitra,biller):
    select = Select(driver.find_element(By.NAME, 'mykunci'))
    select.select_by_value('3')
    search = driver.find_element_by_name("search")
    driver.execute_script(f"arguments[0].value = '{kode_internal}';",search)
    driver.find_element_by_css_selector('.form-control.btn-danger').click()
    time.sleep(1)

    row = driver.find_elements_by_css_selector("#transproduct>tbody>tr")
    for i in row:
        x = i.find_elements_by_tag_name("td")
        aktif = i.find_element_by_css_selector('.alert h7').get_attribute('innerHTML')
        if x[3].text == mitra and x[6].text == kode_internal and aktif == 'NO' and x[9].text == biller:
            i.find_element(By.XPATH,"./td/div/button[@title='Aktif Translasi Produk']").click()
            time.sleep(1)
            driver.find_element_by_css_selector('.confirm').click()
            break
    time.sleep(2)
while True:
    if not driver.current_url == "http://117.102.115.218:8031/web-teleshoph2h-v3/login.html":
        driver.get("http://117.102.115.218:8031/web-teleshoph2h-v3/teleshop/translation/transproduct_url/core/fb925yXGJMNH15U8efJYWEqOLT2B6JXGTUHLtgztgh2mnLQw") 
        time.sleep(2)
        for y,x in enumerate(list_product):
            kode_internal = list_product[x]['kode_internal']
            mitra = list_product[x]['mitra']
            biller = list_product[x]['biller']
            if option == 1 :
                closeProduk(kode_internal,mitra,biller)
            elif option == 2 :
                openProduk(kode_internal,mitra,biller)
        break
driver.close()
driver.quit()