import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bilgi import kullaniciadi,sifre,hedef,sayi

class instagram:
    def __init__(self,kullaniciadi,sifre):
        self.tarayici = webdriver.Firefox()
        self.kullaniciadi = kullaniciadi
        self.sifre = sifre       


    def giris (self):
        self.tarayici.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        kullaniciadigiris = self.tarayici.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[1]/div/label/input")
        sifregiris = self.tarayici.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div/div[2]/div/label/input")

        kullaniciadigiris.send_keys(self.kullaniciadi)
        sifregiris.send_keys(self.sifre)
        sifregiris.send_keys(Keys.ENTER)
        time.sleep(5)

        simdidegil1 =self.tarayici.find_element_by_class_name("cmbtv")
        simdidegil1.click()
        time.sleep(2)

        simdidegil2 = self.tarayici.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        simdidegil2.click()
        time.sleep(2)
    

    def arama(self,hedef):
        self.tarayici.get("https://www.instagram.com/" + hedef)
        time.sleep(2) 

    
    def begeni(self,sayi):
        foto=self.tarayici.find_element_by_class_name("v1Nh3")
        foto.click()

        i=1
        while i<=sayi:
            time.sleep(1)
            ilk=self.tarayici.find_element_by_class_name("fr66n")
            ilk.click()
            time.sleep(1)
            sonra=self.tarayici.find_element_by_class_name("coreSpriteRightPaginationArrow")
            sonra.click()
            
            i+=1
        
        
        self.tarayici.get("https://www.instagram.com/")


        




insta = instagram(kullaniciadi,sifre)
insta.giris()
insta.arama(hedef)
insta.begeni(sayi)

#  python instagramlikebot.py