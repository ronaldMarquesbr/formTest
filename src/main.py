import time
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


correctValues = {
    'nome':  'Ronald',
    'sobrenome': 'Marques',
    'cpf': '12345678912',
    'cep': '66640000',
    'endereco': 'algum endereco',
    'numero': '10',
    'cidade': 'belem',
    'estado': 'Pa',
    'email': 'algum@email.com',
    'celular': '91912341234'
}


def getFormObj(driver):
    formElement = driver.find_element(By.ID, "cadastroForm")

    return formElement


def getInputsFromFormObj(formElement):
    inputs = formElement.find_elements(By.TAG_NAME, "input")

    return inputs


def submitForm(formElement):
    submitButton = formElement.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submitButton.click()


def insertValueInAllInputs(value, inputs, driver):
    try:
        for index, inputTag in enumerate(inputs):
            inputTag.send_keys(value)

            if inputTag.get_attribute('name') == 'cep':
                inputs[index - 1].click()
                alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert.accept()


    except TimeoutException:
        print('Nenhum alerta encontrado')


def isDifferentUrl(url, driver):
    time.sleep(2)

    currentUrl = driver.current_url
    if currentUrl == url:
        return False
    else:
        return True

