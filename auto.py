from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from data import email,password,des
import time


class StartBrowser:
    def __init__(self) -> None:
        self.service = Service(executable_path="chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get("https://google.com")
        WebDriverWait(self.driver,10).until(
           EC.presence_of_element_located((By.NAME,"q"))
        )
class Autofill(StartBrowser):
    def __init__(self) -> None:
        super().__init__()
        self.Search = self.driver.find_element(By.NAME,"q")
        self.Search.send_keys("Internshala" + Keys.ENTER)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"LC20lb"))
        )
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Internshala").click()
        time.sleep(10)
        self.driver.find_element(By.CLASS_NAME,"login-cta").click()
        time.sleep(5)
        self.driver.find_element(By.ID,"modal_email").send_keys(email + Keys.ENTER)
        time.sleep(5)
        self.driver.find_element(By.ID,"modal_password").send_keys(password + Keys.ENTER)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.CLASS_NAME,"main-heading"))
        )
        self.driver.get("https://internshala.com/internships/matching-preferences/")
        WebDriverWait(self.driver,15).until(
            EC.presence_of_element_located((By.ID,"open_content_collapse"))
        )
        time.sleep(6)
        while True:
            Internship = self.driver.find_element(By.CLASS_NAME,"job-internship-name")
            Internship.click()
            WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"profile"))
            )
            time.sleep(10)
            self.driver.find_element(By.ID,"continue_button").click()
            self.driver.find_element(By.CLASS_NAME,"ql-editor").send_keys(des)
            self.Relocation()
            time.sleep(5)
                
    
    
    def Relocation(self):
        try:
            Relocation = self.driver.find_element(By.CSS_SELECTOR,"label[for='check']")
            if Relocation.is_displayed():
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='check']"))).click()
                time.sleep(5)
                self.Assesment()
            else:
                self.Assesment()
        except NoSuchElementException:
            self.Assesment()
            
    



    def Assesment(self):
        try:        
            self.driver.execute_script('window.scrollBy(0, 1000)')
            Assessment = self.driver.find_element(By.CLASS_NAME,"additional_question")
            Assessment_Questions = self.driver.find_elements(By.CLASS_NAME,"additional_question")
            if Assessment.is_displayed():
                for i in Assessment_Questions:
                    time.sleep(5)
                    textarea = i.find_element(By.CSS_SELECTOR,"textarea")
                    attr = textarea.get_attribute("id")
                    WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"textarea[id='{attr}']"))).send_keys("This form is submitted by Bot," + "\n" + "sorry!!!:(" + "\n" + "u can check it on Github https://www.github.com/tufailKhan-dev")
                self.EndForm()
            else:
                self.EndForm()
        except Exception as ec:
            print(ec)
            self.EndForm()
    
    def EndForm(self):
        self.driver.find_element(By.ID,"submit").click()
        time.sleep(5)
        self.driver.get("https://internshala.com/internships/matching-preferences/")
        time.sleep(5)
        self.driver.refresh()









if __name__ == "__main__":
    start = Autofill()


