import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


df = pd.read_csv(f"update_harga.csv")
list_product = df.to_dict('index')

print("Update Harga")
print(df)

# create webdriver object
driver = webdriver.Edge(service=EdgeService(
    EdgeChromiumDriverManager().install()))
driver.maximize_window()
driver.get("http://117.102.115.218:8031/web-teleshoph2h-v3/login.html")


def updatePrice(kode_internal, mitra, biller, harga_jual, harga_enduser, harga_f1, harga_f2, harga_f3):
    select = Select(driver.find_element(By.NAME, 'mykunci'))
    select.select_by_value('b.product_name')
    search = driver.find_element_by_name("search")
    driver.execute_script(f"arguments[0].value = '{kode_internal}';", search)
    driver.find_element_by_css_selector('.form-control.btn-danger').click()
    time.sleep(1)
    # todo
    # show 1000 entries
    row = driver.find_elements_by_css_selector(
        ".table.table-bordered.table-striped.dataTable.no-footer>tbody>tr")
    for i in row:
        x = i.find_elements_by_tag_name("td")
        if x[2].text == mitra and x[5].text == kode_internal and x[4].text == biller:
            i.find_element(
                By.XPATH, "./td/div/button[@title='Ubah Produk Cluster']").click()
            time.sleep(1)
            hj = driver.find_element(By.ID, "value")
            driver.execute_script(f"arguments[0].value = '{harga_jual}';", hj)
            he = driver.find_element(By.ID, "list_value")
            driver.execute_script(
                f"arguments[0].value = '{harga_enduser}';", he)
            hf1 = driver.find_element(By.ID, "f1")
            driver.execute_script(f"arguments[0].value = '{harga_f1}';", hf1)
            hf2 = driver.find_element(By.ID, "f2")
            driver.execute_script(f"arguments[0].value = '{harga_f2}';", hf2)
            hf3 = driver.find_element(By.ID, "f3")
            driver.execute_script(f"arguments[0].value = '{harga_f3}';", hf3)
            driver.find_element_by_css_selector(
                '.btn.btn-primary.modal-action').click()
            time.sleep(1)
            driver.find_element_by_css_selector('.confirm').click()
            break
    time.sleep(2)


while True:
    if not driver.current_url == "http://117.102.115.218:8031/web-teleshoph2h-v3/login.html":
        driver.get("http://117.102.115.218:8031/web-teleshoph2h-v3/teleshop/master/produk_cluster_url/core/fb925yXGJMNH15U8efJYWEqOLT2B6JXGTUHLtgztgh2mnLQw")
        time.sleep(2)
        for dt in list_product:
            kode_internal = list_product[dt]['kode_internal']
            mitra = list_product[dt]['mitra']
            biller = list_product[dt]['biller']
            harga_jual = list_product[dt]['harga_jual']
            harga_enduser = list_product[dt]['harga_enduser']
            f1 = list_product[dt]['f1']
            f2 = list_product[dt]['f2']
            f3 = list_product[dt]['f3']
            updatePrice(kode_internal, mitra, biller,
                        harga_jual, harga_enduser, f1, f2, f3)
        break
driver.close()
driver.quit()
