import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO

def get_web_element_by_id(link, element_id, driver = webdriver.Firefox()):
    driver.get(link)
    WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, element_id))
    )
    return driver.find_element(By.ID, element_id)



def get_html_from_web_element(web_element):
    return web_element.get_attribute('outerHTML')


def html_to_pandas_table(html):
    return pd.read_html(StringIO(html))   
 
    
def write_table_to_csv(table,table_id):
    table[0].to_csv(f'{table_id}.csv', index=False)
    print(f"Wrote {table_id} to csv...")


def run_script(link,table_id,driver = webdriver.Firefox()):
    web_element = get_web_element_by_id(link,table_id)
    html = get_html_from_web_element(web_element)
    table = html_to_pandas_table(html)
    write_table_to_csv(table,table_id)
    driver.quit() 


if __name__ == "__main__":    
    link = "https://www.foxsports.com/nba/standings"
    table_ids = ["live-standings-table-1", "live-standings-table-0"]
    [run_script(link,table_id) for table_id in table_ids]