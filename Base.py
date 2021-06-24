from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://onliner.by/"

    def find_element(self, locator, time=2):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_link(self, link, time=2):
        elem = WebDriverWait(self.driver, time).until(ec.presence_of_element_located(link),
                                                      message=f"Can't find element by link {link}")
        elem.click()
        return elem

    def switch_to_frame(self, frame):
        iframe = self.driver.find_element_by_xpath(frame)
        return self.driver.switch_to.frame(iframe)

    def go_to_site(self):
        return self.driver.get(self.base_url)