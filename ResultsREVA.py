#A code to retrieve marks of my friends
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #optional
from bs4 import BeautifulSoup as soup, BeautifulSoup
from urllib.request import urlopen as uReq
url="http://results.logisys.org/reva/index.php"
srnst = "R18CS"
results=[]
frnds=[492,500,501,502,506,537]
#no=400
#print(srnst)
driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
print("Searching for Sibayan,Abhishek,Adnan,Akash,Avi,Vineet:\n")
print(".")
for no in frnds:
    print(".")
    driver.get(url)
    srn = driver.find_element_by_id("reg_no")
    srn.send_keys(srnst+str(no))
    sem = driver.find_element_by_id("exam")
    sem.send_keys(Keys.ARROW_DOWN)
    sem.send_keys(Keys.ARROW_DOWN)
    sem.send_keys(Keys.ARROW_DOWN)
    sem.send_keys(Keys.ARROW_DOWN)
    sem.send_keys(Keys.ARROW_DOWN)
    sem.send_keys(Keys.ENTER)
    #driver.quit()
    newurl = "http://results.logisys.org/reva/result.php?r="+srnst+str(no)+"&e=D"
    #driver.get(newurl)
    time.sleep(1)
    print(".")
    a = uReq(newurl)      
    page_html = a.read()
    a.close()
    page_soup = soup(page_html,"lxml")
    x=page_soup.findAll("table")
    #print(len(x))
    time.sleep(1)
    print(".")
    results.append(driver.find_element_by_xpath("//table[@class='result_table_footer']/tbody/tr/td").text)
print("Result of Sibyan,Abhishek,Adnan,Akash,Avi,Vineet:\n")
for i in results:
    print(i+"\n")
driver.quit()


'''#-----------------------------------SCRAPING---------------------------------------

newurl = "http://results.logisys.org/reva/result.php?r="+srnst+str(no)+"&e=D"
a=uReq(newurl)
page_html = a.read()
a.close()
print(newurl)
page_soup = BeautifulSoup(page_html,"html.parser")
container = page_soup.find("div" , {"id" : "result_success_div"})
print(container.text)

#------------------------------------------------------------------------------------'''

