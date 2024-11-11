from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase4(value):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    for inputTag in inputs:
        inputName = inputTag.get_attribute('name')
        if inputName == 'numero':
            inputTag.send_keys(value)
        else:
            inputTag.send_keys(correctValues[inputName])

    submitForm(myForm, driver)
    response = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print(f"Valor a ser inserido no campo 'numero': {value}")
    print(f"Formulario submetido: {response}")


incorrectValues = ['abc', '12%', '1234567891789', '%$#', '10']
for incorrectValue in incorrectValues:
    testCase4(incorrectValue)
