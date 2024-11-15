from main import getFormObj, getInputsFromFormObj, isDifferentUrl, submitForm, correctValues
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

url = "https://www.bsntecnologia.com.br/TesteQA.html"


def testCase6(value):
    driver = webdriver.Chrome()
    driver.get(url)

    time.sleep(1)

    myForm = getFormObj(driver)
    inputs = getInputsFromFormObj(myForm)
    for index, inputTag in enumerate(inputs):
        inputName = inputTag.get_attribute('name')
        if inputName == 'cep':
            try:
                print(f"Valor a ser inserido no campo 'CEP': {value}")
                inputTag.send_keys(value)
                inputs[index - 1].click()
                alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
                alert.accept()
                print(f"Valor real do campo 'CEP': {inputTag.get_attribute('value')}")
            except TimeoutException:
                pass
        else:
            inputTag.send_keys(correctValues[inputName])

    submitForm(myForm, driver)
    response = isDifferentUrl(url, driver)
    driver.close()

    print(f"Formulario submetido: {response}\n")


incorrectValues = ['66640000', '67120000', '66640%%%', '66640', '666400000', 'aaaaaaaa', '66640aaa']
for incorrectValue in incorrectValues:
    testCase6(incorrectValue)
