import scrapy

class MagicSpider(scrapy.Spider):
    name = 'magic'
    start_urls = [
        'https://www.magicbricks.com/rera-registered-projects-Hyderabad/','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-2','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-3','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-4',
        'https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-5','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-6','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-7','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-8',
        'https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-9','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-10','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-11','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-12',
        'https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-13','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-14','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-15','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-16',
        'https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-17','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-18','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-19','https://www.magicbricks.com/rera-registered-projects-Hyderabad/page-20'
    ]

    def parse(self,response):
        for i in range(40):
            links = response.xpath("(//div[@class='proNameColm1']/a)").xpath("@href")[i].extract()

            yield {'links': links}