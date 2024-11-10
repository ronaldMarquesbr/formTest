from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase7(value):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    for inputTag in inputs:
        inputName = inputTag.get_attribute('name')
        if inputName == 'celular':
            inputTag.send_keys(value)
        else:
            inputTag.send_keys(correctValues[inputName])

    submitForm(myForm)
    response = isDifferentUrl(url, driver)
    driver.close()

    print(f"Valor inserido no campo 'celular': {value}")
    print(f"Formulario submetido: {response}")


incorrectValues = ['12341234', '123456789123', '%%123456789', 'aaaaaaaaaaa', 'abc123456789', '12341234123']
for incorrectValue in incorrectValues:
    testCase7(incorrectValue)
