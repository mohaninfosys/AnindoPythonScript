from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from random import randint
from library.jsonLoader import jsonLoader
import config

config_file = config.config_path
configObj = jsonLoader(config_file).jsonContent

class commonUtils(object):

    def __init__(self):
        self.configObj = configObj

    @staticmethod
    def setdriver(drivertype):
        global driver
        if drivertype == "chrome":
            driver = webdriver.Chrome(executable_path=configObj["driver"]["chrome"])
        elif drivertype == "firefox":
            driver = webdriver.Firefox(executable_path=configObj["driver"]["firefox"])
        else:
            driver = webdriver.Chrome(executable_path=configObj["driver"]["chrome"])

    @staticmethod
    def get(url):        
        #time.sleep(3)
        driver.maximize_window()
        driver.get(url)

    @staticmethod
    def opennewtab(url):
        driver.execute_script("window.open('"+url+"','new window')")
        driver.switch_to_window("new window")

    @staticmethod
    def closenewtab():
        driver.close()
        driver.switch_to_window(driver.window_handles[0])

    @staticmethod
    def closedriver(self):
        driver.close()

    @staticmethod
    def waitforlocator(xpath):
        try:
            first_result = ui.WebDriverWait(driver, 15).until(lambda driver: driver.find_element_by_xpath(xpath))
            we = driver.find_element_by_xpath(xpath)
            return we
        except Exception as e:
            print
            e
            raise
            assert False

    @staticmethod
    def click(xpath):
        webelement = commonUtils.waitforlocator(xpath)
        try:
            if webelement.is_displayed():
                webelement.click()
            else:
                assert False
        except Exception as e:
            print
            e
            raise

    @staticmethod
    def enterkeys(xpath, keystosend):
        webelement = commonUtils.waitforlocator(xpath)
        try:
            webelement.send_keys(keystosend)
        except Exception as e:
            print
            e
            raise

    @staticmethod
    def teardown():
        driver.quit()

    @staticmethod
    def gettext(xpath):
        webelement = commonUtils.waitforlocator(xpath)
        try:
            #commonUtils.highlight(xpath)
            text = webelement.text
            return text

        except Exception as e:
            print
            e
            raise

    @staticmethod
    def highlight(element):
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
            original_style = element.get_attribute('style')
            apply_style("background: yellow; border: 2px solid red;")
            time.sleep(.3)
            apply_style(original_style)

    @staticmethod
    def getattribute(xpath, locatorname):
        webelement = commonUtils.waitforlocator(xpath)
        return webelement.get_attribute(locatorname)

    @staticmethod
    def isdisplayed(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        return webelement.is_displayed()

    @staticmethod
    def isselected(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        return webelement.is_selected()

    @staticmethod
    def isvisible(xpath):
        mwait = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(By.XPATH, xpath))
        return mwait

    @staticmethod
    def isenabled(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        return webelement.is_enabled()

    @staticmethod
    def findelements(xpath):
        listdummy = []
        try:
            webelement = driver.find_elements_by_xpath(xpath)
            count = webelement.size()

            for i in range(count):
                temp = webelement.get(i).text()
                listdummy = listdummy.append(temp)

        except Exception as e:
            assert False

        return listdummy

    @staticmethod
    def actionclick(xpath):
        webelement = commonUtils.waitforlocator(xpath)
        try:
            time.sleep(.1)
            if webelement.is_enabled():
                action = ActionChains(driver)
                action.click(webelement).perform()
            else:
                assert False
        except Exception as e:

            assert False

    @staticmethod
    def actiontype(xpath, keystosend):
        webelement = driver.find_element_by_xpath(xpath)
        try:

            if webelement.is_enabled():
                action = ActionChains(driver)
                action.send_keys(xpath, keystosend).perform()
            else:
                assert False
        except Exception as e:

            assert False

    @staticmethod
    def doubleclick(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        action = ActionChains(driver).double_click(webelement)
        action.perform()

    @staticmethod
    def clear(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        webelement.clear()

    @staticmethod
    def clearandtype(xpath, keystosend):
        try:
            webelement = driver.find_element_by_xpath(xpath)
            webelement.clear()
            webelement.send_keys(keystosend)
        except Exception as e:
            assert False

    @staticmethod
    def mouseover(xpath):
        try:
            webelement = commonUtils.waitforlocator(xpath)
            action = ActionChains(driver)
            action.move_to_element(webelement).perform()
        except Exception as e:
            assert False

    @staticmethod
    def mouseoverandclick(xpath):
        webelement = commonUtils.waitforlocator(xpath)
        try:
            action = ActionChains(driver)
            action.move_to_element(webelement).click().perform()
        except Exception as e:
            assert False

    @staticmethod
    def selectbyvisibletext(xpath, inputdata):
        try:
            select = Select(driver.find_element_by_xpath(xpath))
            select.select_by_visible_text(inputdata)
        except:
            assert False

    @staticmethod
    def selectbyindex(xpath, inputdata):
        webelement = driver.find_element_by_xpath(xpath)
        try:
            if not webelement.is_enabled():
                time.sleep(.2)
                select = Select(webelement)
                select.select_by_index(inputdata)
        except:
            assert False

    @staticmethod
    def selectbyvalue(xpath, text):
        webelement = driver.find_element_by_xpath(xpath)
        try:
            select = Select(webelement)
            select.select_by_value(text)
        except:
            assert False

    @staticmethod
    def deselectbyvalue(xpath, value):
        webelement = driver.find_element_by_xpath(xpath)
        try:
            select = Select(webelement)
            select.deselect_by_value(value)
        except:
            assert False

    @staticmethod
    def deselectbyindex(xpath, index):
        webelement = driver.find_element_by_xpath(xpath)
        try:
            select = Select(webelement)
            select.deselect_by_index(index)
        except:
            assert False

    @staticmethod
    def clickandhold(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        action = ActionChains(driver)
        action.click_and_hold(webelement).perform()

    @staticmethod
    def getcurrenturl():
        try:
            return driver.current_url
        except Exception as e:
            print
            e
            raise

    @staticmethod
    def selectcheckbox(xpath):
        webelement = commonUtils.waitforlocator(xpath)
        if webelement is not None:
            if webelement.is_selected():
                return True
            else:
                webelement.click()
        else:
            return False

    @staticmethod
    def deselectcheckbox(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        if webelement.is_selected():
            webelement.click()
        else:
            return False

    @staticmethod
    def switchtab(self):
        driver.switch_to.window(driver.window_handles[1])

    @staticmethod
    def switchtab2(self):
        driver.switch_to.window(driver.window_handles[2])

    @staticmethod
    def switchwindow(self):
        driver.switch_to.window(driver.window_handles(0))

    @staticmethod
    def switchdefaultcontent(self):
        driver.switch_to.default_content()

    @staticmethod
    def draganddrop(dragxpath, dropxpath):
        webelement = driver.find_element_by_xpath(dragxpath)
        webelement1 = driver.find_element_by_xpath(dropxpath)
        action = ActionChains(driver)
        action.drag_and_drop(webelement, webelement1).perform()

    @staticmethod
    def elementisselected(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        webelement.is_selected()
        return True

    @staticmethod
    def verifyelementispresent(xpath):
        webelement = driver.find_element_by_xpath(xpath)
        commonUtils.highlight(xpath)
        webelement.is_displayed()
        return True

    @staticmethod
    def verifyelementisnotpresent(xpath):
        webelement = driver.find_element_by_xpath()
        mwait = WebDriverWait(driver, 5)

    @staticmethod
    def tab(self):
        action = ActionChains(driver)
        action.send_keys(Keys.TAB).perform()

    @staticmethod
    def randomnumber():
        return (time.strftime('%d%H%M%S'))

    @staticmethod
    def getlogixotp():
        commonUtils.opennewtab(configObj["phpmyadmin"]["url"])
        commonUtils.enterkeys("//input[@id='input_username']", configObj["phpmyadmin"]["user"]);
        commonUtils.enterkeys("//input[@id='input_password']", configObj["phpmyadmin"]["password"]);
        commonUtils.click("//input[@value='Go']");
        userid = commonUtils.gettext("(//table[@id='table_results']/tbody/tr/td[7])[1]")
        if userid == "25":
            loginotp = commonUtils.gettext("(//table[@id='table_results']/tbody/tr/td[6])[1]")
        else:
            for i in range(2, 20):
                userid = commonUtils.gettext("(//table[@id='table_results']/tbody/tr/td[7])[" + i + "]")
                if userid is 25:
                    loginotp = commonUtils.gettext("(//table[@id='table_results']/tbody/tr/td[7])[" + i + "]")
                    break
        commonUtils.closenewtab()
        return loginotp