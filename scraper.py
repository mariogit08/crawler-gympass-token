import scrapy
import logging

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['https://www.gympass.com/']

    def parse(self, response):
        return scrapy.Request('https://www.gympass.com/pessoas/entrar',
                          callback=self.parse_loggin)
    
    def parse_loggin(self, response):      
        person_search_info = '09812092463'
        person_type = 'b2b'
        commit = 'Continuar'       
        utf8 = response.xpath('//input[@name="utf8"]/@value').get()
        self.log(utf8)        
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').get()
        self.log(authenticity_token)
        url = 'https://www.gympass.com//pessoas/entrar?utf8=%E2%9C%93&authenticity_token='+authenticity_token+'&person_search_info=09812092463&person_type=b2b&commit=Continuar?'
        self.log(url)
        return scrapy.Request(url,
                          callback=self.parse_senha)
    
    def parse_senha(self, response):
        url = 'https://www.gympass.com/pessoas/entrar'        
        utf8 = '%E2%9C%93'
        authenticity_token = response.xpath('//input[@name="authenticity_token"]/@value').get()                
        person[email]: 'emailConta'
        person[password]: 'senhaConta'
        person[remember_me]: '0'
        person[remember_me]: '1'                        
        self.log(authenticity_token)
        url = 'https://www.gympass.com/pessoas/entrar'
        self.log(url)
