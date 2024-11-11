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
        if inputName == 'cpf':
            inputTag.send_keys(value)
        else:
            inputTag.send_keys(correctValues[inputName])

    submitForm(myForm, driver)
    response = isDifferentUrl(url, driver)
    time.sleep(1)
    driver.close()
    print(f"Valor a ser inserido no campo 'CPF': {value}")
    print(f"Formulario submetido: {response}\n")


incorrectValues = ['abcabcabcab', '12%12$12$$%', '1234567891', '123456789123', '12312312312']
for incorrectValue in incorrectValues:
    testCase4(incorrectValue)
