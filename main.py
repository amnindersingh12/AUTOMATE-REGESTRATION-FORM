import time
import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# 653614758457
delay = 3
web = webdriver.Chrome()
web.get('http://www.scholarships.punjab.gov.in/')


for _ in range(2):
    registeration = web.find_element_by_id("studentreglnk")
    registeration.click()


# selecting quoto
quota = Select(web.find_element_by_id("ddlQuota"))
quota.select_by_visible_text('Non-Management Quota')
print("Success !")

# entering aadhar number
aadar = web.find_element_by_xpath('//*[@id="txtCardno"]')
aadar.send_keys(input("Enter aadhar card number : "))
print("Success !")

# entering DOB number
dob_is = input("Enter Date Of Birth (25/12/2000): ")
for _ in range(2):
    dob = web.find_element_by_xpath('//*[@id="TxtDOB"]')
    dob.send_keys(dob_is)
print("Success !")

# entering First  name
first_name = web.find_element_by_xpath('//*[@id="txtFirstName"]')
first_name.send_keys(input("Enter Your First Name : "))
print("Success !")

# entering MIDDLE  name
MIDDLE_name = web.find_element_by_xpath('//*[@id="txtMiddleName"]')
MIDDLE_name.send_keys(
    input("Enter Your MIDDLE Name : (LEAVE EMPTY IF YOU DON'T HAVE ANY)"))
print("Success !")

# entering LAST  name
LAST_name = web.find_element_by_xpath('//*[@id="txtSurname"]')
LAST_name.send_keys(input("Enter Your LAST Name : "))
print("Success !")

# selecting Gender
Gender = Select(web.find_element_by_id("ddlGender"))
Gender.select_by_visible_text(input("Enter YOur Gender : "))
print("Success !")

# agree ?

proceed = web.find_element_by_xpath('//*[@id="btnconsentAgree"]')
txt = input("Type 'Y' if above info is correct else 'N' : ")
if(txt == 'Y'):
    proceed.click()
    print("Success !")
else:
    print("Run Script again !")
    
# if(web.find_element_by_xpath('//*[@id="txtFatherName"]').is_enabled() == False):
#     web.close()
# else:
# entering father name 
father_name = web.find_element_by_xpath('//*[@id="txtFatherName"]')
father_name.send_keys(input("Enter YOur Father's Name : "))

# entering Mother name 
Mother_name = web.find_elemen653614758457t_by_xpath('//*[@id="txtMotherName"]')
Mother_name.send_keys(input("Enter YOur Mother's Name : "))

# selecting Religion
Religion = Select(web.find_element_by_id("ddlReligion"))
Religion.select_by_visible_text(input("Enter YOur Religion (Hindu/Christian/Muslim/Sikhism) : "))
print("Success !")

# selecting Category
Category = Select(web.find_element_by_id("ddlCategory"))
Category.select_by_visible_text(input("Enter YOur Category (SC/OBC) : "))
print("Success !")

# selecting IsDtribes
IsDtribes = Select(web.find_element_by_id("ddlIsDtribes"))
IsDtribes.select_by_visible_text("No")

# enter your mobile number
Mobile_Number = web.find_element_by_xpath('//*[@id="txtPMobile"]')
Mobile_Number.send_keys(input("Enter YOur 10 digitsMobile Number : "))
print("Success !")

# selecting State
State = Select(web.find_element_by_id("DdlState"))
State.select_by_visible_text(input("Enter YOur State name : "))
print("Success !")

# enter your Address
Address = web.find_element_by_xpath('//*[@id="txtAddress"]')
Address.send_keys(input("Enter YOur Full Address : "))
print("Success !")

# selecting District
District = Select(web.find_element_by_id("DdlDistrict"))
District.select_by_visible_text(input("Enter YOur District name : "))
print("Success !")

# enter your PinCode
PinCode = web.find_element_by_xpath('//*[@id="txtPinCode"]')
PinCode.send_keys(input("Enter YOur Pin Code : "))
print("Success !")

# selecting chkSameAdd
chkSameAdd = web.find_element_by_id("chkSameAdd").click()
print("DONE !")

# Entering Captcha
elem = web.find_element_by_xpath('//*[@id="mainCaptcha"]')
elem.send_keys(Keys.CONTROL, 'a') #highlight all in box
new_elem = elem.send_keys(Keys.CONTROL, 'c')
elem_2 = web.find_element_by_xpath('//*[@id="txtVerifyCaptcha"]')
elem_2.send_keys(Keys.CONTROL, 'v')
print("SUCCESS !")
