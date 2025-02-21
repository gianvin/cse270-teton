# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options

class TestSmokeTest():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
    
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_navigatetheAdminPage(self):
    self.driver.get("http://127.0.0.1:5500/cse270/teton/1.6/index.html")
    self.driver.set_window_size(1151, 1040)
    self.driver.find_element(By.LINK_TEXT,"Admin").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Username:"
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("incorrect")
    self.driver.find_element(By.ID, "password").send_keys("incorrect")
    self.driver.find_element(By.CSS_SELECTOR, ".admin-main").click()
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."

  def test_navigatetheDirectoryPage(self):
    self.driver.get("http://127.0.0.1:5500/cse270/teton/1.6/index.html")
    self.driver.set_window_size(1151, 1040)
    self.driver.find_element(By.LINK_TEXT,"Directory").click()
    self.driver.find_element(By.ID,"directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(odd) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, "gold-member:nth-child(odd) > p:nth-child(2)").text == "Teton Turf and Tree"

  def test_navigatetheHomePage(self):
    self.driver.get("http://127.0.0.1:5500/cse270/teton/1.6/index.html")
    self.driver.set_window_size(1151, 1040)
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
    assert len(elements) > 0

  def test_navigatetheJoinPage(self):
   self.driver.get("http://127.0.0.1:5500/cse270/teton/1.6/index.html")
   self.driver.set_window_size(1151, 1040)
   self.driver.find_element(By.LINK_TEXT,"Join").click()
   assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "First Name"
   elements = self.driver.find_elements(By.NAME, "fname")
   assert len(elements) > 0
   self.driver.find_element(By.NAME, "fname").click()
   self.driver.find_element(By.NAME, "fname").send_keys("Gina")
   self.driver.find_element(By.NAME, "lname").send_keys("Ong")
   self.driver.find_element(By.NAME, "bizname").send_keys("Teton Travel and Tours")
   self.driver.find_element(By.NAME, "biztitle").send_keys("Travel Agency")
   self.driver.find_element(By.NAME, "submit").click()
   assert self.driver.find_element(By.CSS_SELECTOR, ".myinput:nth-child(2)").text == "Email"
   elements = self.driver.find_elements(By.NAME, "email")
   assert len(elements) > 0