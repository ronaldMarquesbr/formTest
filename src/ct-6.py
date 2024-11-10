from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
from selenium.common import TimeoutException
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase6(value):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)

    try:
        for inputTag in inputs:
            inputName = inputTag.get_attribute('name')
            if inputName == 'cep':
                print(f"Valor a ser inserido no campo 'CEP': {value}")
                inputTag.send_keys(value)
                print(f"Valor real do campo 'CEP': {inputTag.get_attribute('value')}")
            else:
                inputTag.send_keys(correctValues[inputName])


    except TimeoutException:
        print('Nenhum Alerta encontrado')

    submitForm(myForm)
    response = isDifferentUrl(url, driver)
    driver.close()

    print(f"Formulario submetido: {response}\n")


incorrectValues = ['66640000', '67120000', '66640%%%', '66640', '666400000', 'aaaaaaaa', '66640aaa']
for incorrectValue in incorrectValues:
    testCase6(incorrectValue)
