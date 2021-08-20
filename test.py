from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/driver/chromedriver.exe")
driver.maximize_window()

driver.get("http://localhost/form.php")
driver.find_element_by_name("nip").send_keys("12345")
driver.find_element_by_name("nama").send_keys("Udin")
driver.find_element_by_name("nik").send_keys("07050010")
driver.find_element_by_name("alamat").send_keys("Bogor")
driver.find_element_by_name("perusahaan").send_keys("Creative Computer")
driver.find_element_by_name("tanggal").send_keys("01/01/2020")
driver.find_element_by_name("divisi").send_keys("hrd")
driver.find_element_by_name("posisi").send_keys("staff")
driver.find_element_by_name("gaji").send_keys("1000000")
driver.find_element_by_name("atasan").send_keys("Sari")
driver.find_element_by_name("submit").click()

driver.close()
driver.quit()
print("test selesai...")