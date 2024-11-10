from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase3():
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    for inputTag in inputs:
        inputName = inputTag.get_attribute('name')
        if inputName in ['nome', 'sobrenome', 'estado', 'cidade']:
            inputTag.send_keys('0000$$$$.....')
        else:
            inputTag.send_keys(correctValues[inputName])

    time.sleep(1)
    submitForm(myForm)
    response = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print(f"Formulario submetido: {response}")


testCase3()
