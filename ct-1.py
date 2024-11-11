from main import getFormObj, isDifferentUrl, submitForm
from selenium import webdriver
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase1():
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)
    myForm = getFormObj(driver)
    submitForm(myForm, driver)
    res = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print("Formulário submetido: ", res)


testCase1()
