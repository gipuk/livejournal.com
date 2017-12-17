from selenium import webdriver

from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Browser(object):
    driver = webdriver.Chrome()
    locator_dictionary = {}

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def __getattr__(self, k):
        if k in self.locator_dictionary:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(
                    self.locator_dictionary[k]
                )
            )
            return self.find_element(*self.locator_dictionary[k])
        else:
            raise AttributeError

    def open_home_page(self):
        self.driver.get('http://www.livejournal.com')

    def hover_over(self, element):
        hover = ActionChains(self.driver)
        hover.move_to_element(element).perform()

    def select(self, dropdown, element):
        myselect = Select(dropdown)
        myselect.select_by_visible_text(element)

    def quit(self):
        self.driver.quit()