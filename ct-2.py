from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def submitNoValuesForm():
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    for inputTag in inputs:
        inputTag.send_keys(' ')

    submitForm(myForm, driver)
    response = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print(f"Formulario submetido: {response}")


def submitMinimumForm():
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    for inputTag in inputs:
        if inputTag.get_attribute('name') in ['cep', 'email']:
            inputTag.send_keys(correctValues[inputTag.get_attribute('name')])
        else:
            inputTag.send_keys(' ')

    submitForm(myForm, driver)
    response = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print(f"Formulario submetido: {response}")


submitNoValuesForm()
submitMinimumForm()
