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

class TestKKN():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_kKN(self):
    # Test name: KKN
    # Step # | name | target | value
    # 1 | open | / | 
    self.driver.get("https://pelayanan.kesbangpol.bandung.go.id/")
    # 2 | setWindowSize | 1552x880 | 
    self.driver.set_window_size(1552, 880)
    # 3 | click | id=popover-trigger-:r4: | 
    self.driver.find_element(By.ID, "popover-trigger-:r4:").click()
    # 4 | click | css=a:nth-child(3) .chakra-text | 
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) .chakra-text").click()
    # 5 | mouseOver | css=a:nth-child(3) .chakra-text | 
    element = self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) .chakra-text")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 6 | mouseOut | css=a:nth-child(3) .chakra-text | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 7 | runScript | window.scrollTo(0,428.869873046875) | 
    self.driver.execute_script("window.scrollTo(0,428.869873046875)")
    # 8 | click | id=nama | 
    self.driver.find_element(By.ID, "nama").click()
    # 9 | type | id=nama | Seto
    self.driver.find_element(By.ID, "nama").send_keys("Seto")
    # 10 | click | id=alamat | 
    self.driver.find_element(By.ID, "alamat").click()
    # 11 | type | id=alamat | Seto
    self.driver.find_element(By.ID, "alamat").send_keys("Seto")
    # 12 | click | id=no_identitas | 
    self.driver.find_element(By.ID, "no_identitas").click()
    # 13 | type | id=no_identitas | Seto
    self.driver.find_element(By.ID, "no_identitas").send_keys("Seto")
    # 14 | click | id=anggota | 
    self.driver.find_element(By.ID, "anggota").click()
    # 15 | type | id=anggota | Seto
    self.driver.find_element(By.ID, "anggota").send_keys("Seto")
    # 16 | click | id=jabatan | 
    self.driver.find_element(By.ID, "jabatan").click()
    # 17 | select | id=jabatan | label=Ketua Kelompok
    dropdown = self.driver.find_element(By.ID, "jabatan")
    dropdown.find_element(By.XPATH, "//option[. = 'Ketua Kelompok']").click()
    # 18 | click | id=nama_kampus | 
    self.driver.find_element(By.ID, "nama_kampus").click()
    # 19 | type | id=nama_kampus | Seto
    self.driver.find_element(By.ID, "nama_kampus").send_keys("Seto")
    # 20 | click | id=no_surat_kampus | 
    self.driver.find_element(By.ID, "no_surat_kampus").click()
    # 21 | type | id=no_surat_kampus | Seto
    self.driver.find_element(By.ID, "no_surat_kampus").send_keys("Seto")
    # 22 | click | id=tanggal_surat_kampus | 
    self.driver.find_element(By.ID, "tanggal_surat_kampus").click()
    # 23 | click | id=tanggal_surat_kampus | 
    self.driver.find_element(By.ID, "tanggal_surat_kampus").click()
    # 24 | type | id=tanggal_surat_kampus | 2023-09-12
    self.driver.find_element(By.ID, "tanggal_surat_kampus").send_keys("2023-09-12")
    # 25 | click | id=no_hp | 
    self.driver.find_element(By.ID, "no_hp").click()
    # 26 | type | id=no_hp | Seto
    self.driver.find_element(By.ID, "no_hp").send_keys("Seto")
    # 27 | click | id=nama_dinas_terkait | 
    self.driver.find_element(By.ID, "nama_dinas_terkait").click()
    # 28 | click | id=tanggal_mulai | 
    self.driver.find_element(By.ID, "tanggal_mulai").click()
    # 29 | click | id=tanggal_mulai | 
    self.driver.find_element(By.ID, "tanggal_mulai").click()
    # 30 | type | id=tanggal_mulai | 2023-09-10
    self.driver.find_element(By.ID, "tanggal_mulai").send_keys("2023-09-10")
    # 31 | click | id=tanggal_akhir | 
    self.driver.find_element(By.ID, "tanggal_akhir").click()
    # 32 | type | id=tanggal_akhir | 2023-09-14
    self.driver.find_element(By.ID, "tanggal_akhir").send_keys("2023-09-14")
    # 33 | click | id=attach_ktp | 
    self.driver.find_element(By.ID, "attach_ktp").click()
    # 34 | type | id=attach_ktp | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_ktp").send_keys("C:\\fakepath\\catatan.txt")
    # 35 | click | id=attach_suratKampus | 
    self.driver.find_element(By.ID, "attach_suratKampus").click()
    # 36 | type | id=attach_suratKampus | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_suratKampus").send_keys("C:\\fakepath\\catatan.txt")
    # 37 | click | id=attach_ktm | 
    self.driver.find_element(By.ID, "attach_ktm").click()
    # 38 | type | id=attach_ktm | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_ktm").send_keys("C:\\fakepath\\catatan.txt")
    # 39 | click | id=attach_vaksin | 
    self.driver.find_element(By.ID, "attach_vaksin").click()
    # 40 | type | id=attach_vaksin | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_vaksin").send_keys("C:\\fakepath\\catatan.txt")
    # 41 | click | id=attach_pasFoto | 
    self.driver.find_element(By.ID, "attach_pasFoto").click()
    # 42 | type | id=attach_pasFoto | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_pasFoto").send_keys("C:\\fakepath\\catatan.txt")
    # 43 | click | css=.chakra-stack:nth-child(2) > .chakra-form-control:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".chakra-stack:nth-child(2) > .chakra-form-control:nth-child(3)").click()
    # 44 | click | id=attach_suratDinas | 
    self.driver.find_element(By.ID, "attach_suratDinas").click()
    # 45 | type | id=attach_suratDinas | C:\fakepath\catatan.txt
    self.driver.find_element(By.ID, "attach_suratDinas").send_keys("C:\\fakepath\\catatan.txt")
    # 46 | click | id=tombolKirim | 
    self.driver.find_element(By.ID, "tombolKirim").click()
    # 47 | mouseOver | id=tombolKirim | 
    element = self.driver.find_element(By.ID, "tombolKirim")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 48 | mouseOut | id=tombolKirim | 
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    # 49 | verifyElementPresent | css=.chakra-alert__title | 
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".chakra-alert__title")
    assert len(elements) > 0
  
