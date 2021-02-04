from instagramUser import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from openpyxl import Workbook


class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://instagram.com/accounts/login")
        sleep(3)

        usernameInput = self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(3)

        passlink = self.browser.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        passlink.click()
        sleep(3)

        passlinkk = self.browser.find_element_by_xpath('//button[contains(text(), "Şimdi Değil")]')
        passlinkk.click()
        sleep(3)

    def getFollowers(self):
        self.browser.get(f"https://instagram.com/{self.username}")

        followersLink = self.browser.find_element_by_css_selector("#react-root > section > main > div > header > section > ul > li:nth-child(2) > a > span")
        followersLink.click()
        sleep(2)

        jsKomut ="""
        sayfa = document.querySelector(".isgrP");
        sayfa.scrollTo(0,sayfa.scrollHeight);
        var sayfaSonu = sayfa.scrollHeight;
        return sayfaSonu;
        """

        sayfaSonu = self.browser.execute_script(jsKomut)
        while True:
            son = sayfaSonu
            sleep(1)
            sayfaSonu = self.browser.execute_script(jsKomut)

            if (son == sayfaSonu):
                break
        sleep(1)

    def writeExcel(self):
        wb = Workbook()
        ws = wb.active
        kisiler = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        say = 0
        takipciListesi = []
        for kisi in kisiler:
            takipciListesi.append(kisi.text)
            say += 1
        strSay = str(say)
        ws.append(["Toplam Takipçi Sayısı",strSay])
        ws.append(takipciListesi)
        wb.save("Instagram Takipçi Listesi.xlsx")
        wb.close()




instg = Instagram(username,password)
instg.signIn()
instg.getFollowers()
instg.writeExcel()

