import scrapy

# scrapy startproject PresentsSpider  <name(PresentsSpider)> __инициализация
# обьявляем класс и делаем наследование от класса Spider
class PresentsSpider(scrapy.Spider):
    name = 'PresentsSpider'
    # сайт с заквасками
    start_urls = ['https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/']
    # создаем метод класса для сбора дааных и передаем в него обьект класса и dom обьект response
    def parse(self, response):
        # создаем список ссылок с заквасками
        links = [data.get() for data in response.css('.row .nameproduct a::attr(href)')]
        for link in links:
            # с помощью метода Yield параллельно переходим по каждой ссылке
            # в функции parse_card записываем в память полученные обьекты
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

# scrapy crawl 'PresentsSpider' -o 'zakvaski.csv'  __записываем файл csv в терминале

# scrapy shell  __проверяем селектор в терминале
# response.css('h1::text').get() __название
# response.css('span.autocalc-product-price::text').get()  __цена
# response.css('div.product-description b::text').get())  __наличие
# [data.get() for data in response.css('.row .nameproduct a::attr(href)')]  __карточки
