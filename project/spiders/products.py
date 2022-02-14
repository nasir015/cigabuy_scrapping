# -*- coding: utf-8 -*-
import scrapy


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.cigabuy.com']
    start_urls = ['https://www.cigabuy.com/specials.html?disp_order=15']

    def parse(self, response):
        product= response.xpath("//ul[@class='productlisting-ul']/div")
        for list in product:
            title = list.xpath(".//a[@class='p_box_title']/text()").get()
            link=response.urljoin(list.xpath(".//a[@class='p_box_title']/@href").get())
            
           
            
            
            yield{
                'title':title,
                'link':link,
                
                
            }
        next_page= response.xpath("(//a[@class='nextPage'])[1]/@href").get()
        
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)