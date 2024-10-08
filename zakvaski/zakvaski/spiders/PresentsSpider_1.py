import scrapy

class PresentsSpider(scrapy.Spider):
    name = 'PresentsSpider'
    start_urls = ['https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/']
    def parse(self, response):
        links = [data.get() for data in response.css('.row .nameproduct a::attr(href)')]
        for link in links:
            yield response.follow(link, callback=self.parse_card)

    def parse_card(self, response):
        name = response.css('h1::text').get()
        price = response.css('span.autocalc-product-price::text').get()
        availability = response.css('div.product-description b::text').get()
        yield {
            'name': name,
            'price': price,
            'availability': availability
        }

# response.css('h1::text').get() __название
# response.css('span.autocalc-product-price::text').get()  __цена
# response.css('div.product-description b::text').get())  __наличие
# [data.get() for data in response.css('.row .nameproduct a::attr(href)')]  __карточки

# scrapy crawl 'PresentsSpider' -o 'zakvaski.csv'
