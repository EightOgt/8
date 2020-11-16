from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import subprocess
import pandas as pd
import datetime
import re


def main(url):
    # Setting Selenium Options
    options = Options()
    options.add_argument('--disable-extensions')  # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
    options.add_argument('--proxy-server="direct://"')  # Proxy経由ではなく直接接続する
    options.add_argument('--proxy-bypass-list=*')  # すべてのホスト名
    options.add_argument('--start-maximized')  # 起動時にウィンドウを最大化する

    # Paths
    Cwd_Path = __file__.replace('Data_Consumption_Extraction.py', '')
    Driver_Path = '/usr/local/bin/chromedriver'
    SaveFile_Path = Cwd_Path + 'Data_Consumption_Report_<time>.csv'

    # Result variable
    Result_df = pd.DataFrame({'Data_Pool': '', 'Data_Connection': '', 'Table': '', 'Size(B)': '', 'Last_Updated': ''},
                             index=[1])
    # Counter
    Counter_Data = 1
    Counter_Table_Row = 1
    Counter_Page = 1
    Counter_SearchPage = 1
    Counter_SearchLoop = 0

    # Button Xpath
    Button_EventCollection = '/html/body/process-mining-app/process-mining/home/ce-main-layout/ce-burger-content/div' \
                             '/div[1]/div/div/div/ce-cloud-header/ce-app-switcher/div/ul/li[3] '
    Button_DataConsumption = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce' \
                             '-burger-content/div/div[2]/div/div/div[1]/ce-burger-content/div/div[' \
                             '1]/div/div/div/ce-main-side-nav/nav/div/ul/div/ce-main-side-nav-link[3]/li '
    Button_Page = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger-content' \
                  '/div/div[2]/div/div/div[2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                  '2]/div/div/ce-burger-content/div/div[3]/div/ce-pagination/button[<Num>] '
    Button_Page_First = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                        '-content/div/div[2]/div/div/div[' \
                        '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                        '2]/div/div/ce-burger-content/div/div[3]/div/ce-pagination/div[1]/button[1] '
    Button_Page_Last = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                       '-content/div/div[2]/div/div/div[' \
                       '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                       '2]/div/div/ce-burger-content/div/div[3]/div/ce-pagination/div[2]/button[2] '
    Button_Page_5th = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                      '-content/div/div[2]/div/div/div[' \
                      '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                      '2]/div/div/ce-burger-content/div/div[3]/div/ce-pagination/button[5] '
    Details = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger-content/div' \
              '/div[2]/div/div/div[2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
              '2]/div/div/ce-burger-content/div/div[1]/div/div '
    Column_DataPool = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                      '-content/div/div[2]/div/div/div[' \
                      '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                      '2]/div/div/ce-burger-content/div/div[' \
                      '2]/div/ce-data-source-table/ce-table-grid/div/div/ce-table-grid-item[' \
                      '<Num>]/ce-table-grid-column[1] '
    Column_DataConnection = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce' \
                            '-burger-content/div/div[2]/div/div/div[' \
                            '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                            '2]/div/div/ce-burger-content/div/div[' \
                            '2]/div/ce-data-source-table/ce-table-grid/div/div/ce-table-grid-item[' \
                            '<Num>]/ce-table-grid-column[2] '
    Column_Table = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                   '-content/div/div[2]/div/div/div[2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                   '2]/div/div/ce-burger-content/div/div[' \
                   '2]/div/ce-data-source-table/ce-table-grid/div/div/ce-table-grid-item[<Num>]/ce-table-grid-column[' \
                   '3] '
    Column_Size = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger-content' \
                  '/div/div[2]/div/div/div[2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                  '2]/div/div/ce-burger-content/div/div[' \
                  '2]/div/ce-data-source-table/ce-table-grid/div/div/ce-table-grid-item[<Num>]/ce-table-grid-column[4] '
    Column_LastUpdated = '/html/body/integration-app/ng-component/ng-component/ng-component/ce-main-layout/ce-burger' \
                         '-content/div/div[2]/div/div/div[' \
                         '2]/ce-data-consumption/ce-main-content/ce-burger-content/div/div[' \
                         '2]/div/div/ce-burger-content/div/div[' \
                         '2]/div/ce-data-source-table/ce-table-grid/div/div/ce-table-grid-item[' \
                         '<Num>]/ce-table-grid-column[5] '

    # Get Start Time
    now = datetime.datetime.now()

    # Start Browser
    driver = webdriver.Chrome(executable_path=Driver_Path, chrome_options=options)
    wait = WebDriverWait(driver, 15)
    driver.get(url)
    
    # Login to Celonis Manually
    print('Please Login to Celonis. Then Press [Enter] key to Resume.')
    subprocess.run('read reply', shell=True)

    # Transition to Event Collection
    wait.until(EC.visibility_of_element_located((By.XPATH, Button_EventCollection)))
    driver.find_element_by_xpath(Button_EventCollection).click()
    # Transition to Data Consumption
    wait.until(EC.visibility_of_element_located((By.XPATH, Button_DataConsumption)))
    driver.find_element_by_xpath(Button_DataConsumption).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, Details)))

    # Read Last Page Number
    driver.find_element_by_xpath(Button_Page_Last).click()
    Last_Page = int(driver.find_element_by_xpath(Button_Page_5th).text)
    driver.find_element_by_xpath(Button_Page_First).click()

    # Get Table Data
    print('Loading Page No.' + str(Counter_Page) + ' ' + str(datetime.datetime.now()))
    while Counter_Page < Last_Page + 1:
        try:
            Result_df['Data_Pool'][Counter_Data] = driver.find_element_by_xpath(
                Column_DataPool.replace('<Num>', str(Counter_Table_Row))).text
            Result_df['Data_Connection'][Counter_Data] = driver.find_element_by_xpath(
                Column_DataConnection.replace('<Num>', str(Counter_Table_Row))).text
            Result_df['Table'][Counter_Data] = driver.find_element_by_xpath(
                Column_Table.replace('<Num>', str(Counter_Table_Row))).text
            Size = driver.find_element_by_xpath(Column_Size.replace('<Num>', str(Counter_Table_Row))).text
            if 'MB' == Size[-2:]:
                Size = float(''.join(re.findall(r'\d*\.\d+|\d+', Size))) * 1048576
            elif 'kB' == Size[-2:]:
                Size = float(''.join(re.findall(r'\d*\.\d+|\d+', Size))) * 1024
            else:
                Size = float(''.join(re.findall(r'\d*\.\d+|\d+', Size)))
            Result_df['Size(B)'][Counter_Data] = Size
            Result_df['Last_Updated'][Counter_Data] = driver.find_element_by_xpath(
                Column_LastUpdated.replace('<Num>', str(Counter_Table_Row))).text + ':00'
            Counter_Table_Row += 1
            Counter_Data += 1
            Result_df.loc[Counter_Data] = ['', '', '', '', '']
        except Exception:
            Counter_Table_Row = 1
            Counter_Page += 1
            Counter_SearchLoop = 0

            # Search Page
            while Counter_Page != Counter_SearchPage:
                try:
                    Counter_SearchLoop += 1
                    Counter_SearchPage = int(
                        driver.find_element_by_xpath(Button_Page.replace('<Num>', str(Counter_SearchLoop))).text)
                except Exception:
                    break

            # Select Page
            if Counter_Page < Last_Page + 1:
                try:
                    driver.find_element_by_xpath(Button_Page.replace('<Num>', str(Counter_SearchLoop))).click()
                    print('Loading Page No.' + str(Counter_Page) + ' ' + str(datetime.datetime.now()))
                except Exception as e:
                    print(e)
                    print('Processing Failure' + ' ' + str(datetime.datetime.now()))
            else:
                break

    # End Processing
    print('All Pages Loaded' + ' ' + str(datetime.datetime.now()))
    driver.close()

    Result_df.to_csv(SaveFile_Path.replace('<time>', now.strftime('%Y%m%d%H%M%S')), index=False)
    print('Finish! Press [Enter] Key to End')
    subprocess.run('read reply', shell=True)

if __name__ == "__main__":
    url = 'https://abeam-sandbox-dcp.eu-1.celonis.cloud/process-mining/ui'
    main(url)
