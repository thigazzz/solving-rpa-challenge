from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By

class MyListener(AbstractEventListener):
    def after_click(self, element, driver) -> None:
        if element.tag_name == 'input':
            print(dir(element))
            print('Depois do clique no Input')
            print(driver.find_element(By.TAG_NAME, 'label').text)


browser = Firefox()
browser.implicitly_wait(10)

wrapper = EventFiringWebDriver(browser, MyListener())
wrapper.get("https://selenium.dunossauro.live/exercicio_07")

input_el = wrapper.find_element(By.TAG_NAME, 'input').click()


browser.quit()