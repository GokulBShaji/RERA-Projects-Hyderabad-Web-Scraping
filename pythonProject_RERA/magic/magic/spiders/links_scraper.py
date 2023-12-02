import scrapy
import pandas as pd

df = pd.read_excel('RERA_Builders_Database.xlsx')
a = df['links'].to_list()
l = len(a)
b = []
#for i in range(300,l):
for i in range(100):
    b.append(a[i])
    #b.append(a[i+100])
    #b.append(a[i+200])

class MagicSpider(scrapy.Spider):
    name = 'builder'
    start_urls = b

    def parse(self,response):
        name = response.xpath('//h1/text()').extract()
        q1 = response.xpath('//div[@class="proj-info__data__block"][1]/div[@class="proj-info__data__title"]/text()').extract()
        v1 = response.xpath('//div[@class="proj-info__data__block"][1]/div[@class="proj-info__data__value"]/text()').extract()
        q2 = response.xpath('//div[@class="proj-info__data__block"][2]/div[@class="proj-info__data__title"]/text()').extract()
        v2 = response.xpath('//div[@class="proj-info__data__block"][2]/div[@class="proj-info__data__value"]/text()').extract()
        q3 = response.xpath('//div[@class="proj-info__data__block"][3]/div[@class="proj-info__data__title"]/text()').extract()
        v3 = response.xpath('//div[@class="proj-info__data__block"][3]/div[@class="proj-info__data__value"]/text()').extract()
        q4 = response.xpath('//div[@class="proj-info__data__block"][4]/div[@class="proj-info__data__title"]/text()').extract()
        v4 = response.xpath('//div[@class="proj-info__data__block"][4]/div[@class="proj-info__data__value"]/text()').extract()
        q5 = response.xpath('//div[@class="proj-info__data__block"][5]/div[@class="proj-info__data__title"]/text()').extract()
        v5 = response.xpath('//div[@class="proj-info__data__block"][5]/div[@class="proj-info__data__value"]/text()').extract()
        q6 = response.xpath('//div[@class="proj-info__data__block"][6]/div[@class="proj-info__data__title"]/text()').extract()
        v6 = response.xpath('//div[@class="proj-info__data__block"][6]/div[@class="proj-info__data__value"]/text()').extract()
        q7 = response.xpath('//div[@class="proj-info__data__block"][7]/div[@class="proj-info__data__title"]/text()').extract()
        v7 = response.xpath('//div[@class="proj-info__data__block"][7]/div[@class="proj-info__data__value"]/text()').extract()
        q8 = response.xpath('//div[@class="proj-info__data__block"][8]/div[@class="proj-info__data__title"]/text()').extract()
        v8 = response.xpath('//div[@class="proj-info__data__block"][8]/div[@class="proj-info__data__value"]/text()').extract()
        q9 = response.xpath('//div[@class="proj-info__data__block"][9]/div[@class="proj-info__data__title"]/text()').extract()
        v9 = response.xpath('//div[@class="proj-info__data__block"][9]/div[@class="proj-info__data__value"]/text()').extract()
        q10 = response.xpath('//div[@class="proj-info__data__block"][10]/div[@class="proj-info__data__title"]/text()').extract()
        v10 = response.xpath('//div[@class="proj-info__data__block"][10]/div[@class="proj-info__data__value"]/text()').extract()
        q11 = response.xpath('//div[@class="proj-info__data__block"][11]/div[@class="proj-info__data__title"]/text()').extract()
        v11 = response.xpath('//div[@class="proj-info__data__block"][11]/div[@class="proj-info__data__value"]/text()').extract()
        q12 = response.xpath('//div[@class="proj-info__data__block"][12]/div[@class="proj-info__data__title"]/text()').extract()
        v12 = response.xpath('//div[@class="proj-info__data__block"][12]/div[@class="proj-info__data__value"]/text()').extract()
        q13 = response.xpath('//div[@class="proj-info__data__block"][13]/div[@class="proj-info__data__title"]/text()').extract()
        v13 = response.xpath('//div[@class="proj-info__data__block"][13]/div[@class="proj-info__data__value"]/text()').extract()
        q14 = response.xpath('//div[@class="proj-info__data__block"][14]/div[@class="proj-info__data__title"]/text()').extract()
        v14 = response.xpath('//div[@class="proj-info__data__block"][14]/div[@class="proj-info__data__value"]/text()').extract()

        yield {'Name': name,
               'P_1':q1,
               'PV_1':v1,
               'P_2':q2,
               'PV_2':v2,
               'P_3': q3,
               'PV_3': v3,
               'P_4': q4,
               'PV_4': v4,
               'P_5': q5,
               'PV_5': v5,
               'P_6': q6,
               'PV_6': v6,
               'P_7': q7,
               'PV_7': v7,
               'P_8': q8,
               'PV_8': v8,
               'P_9': q9,
               'PV_9': v9,
               'P_10': q10,
               'PV_10': v10,
               'P_11': q11,
               'PV_11': v11,
               'P_12': q12,
               'PV_12': v12,
               'P_13': q13,
               'PV_13': v13,
               'P_14': q14,
               'PV_14': v14
               }
