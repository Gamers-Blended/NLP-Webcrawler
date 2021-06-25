import scrapy
import time
import selenium
from selenium import webdriver


# define spider
class NewssSpider(scrapy.Spider):
    name = 'newss'
    allowed_domains = ['forbes.com/business']
    start_urls = ['https://www.forbes.com/business/']

    # initialise webdriver object - modify path to chromedriver
    def __init__(self):
        self.driver = webdriver.Chrome(<path to chromedriver\chromedriver.exe")


    def parse(self, response):
        self.driver.get(response.url)
        # continuously look for "More Articles" button
        while True:
            # find the "More Articles" button
            next = self.driver.find_element_by_class_name("load-more")
            try:
                time.sleep(5)
                # click button
                next.click()
            except:
                break

        # get urls from More from Business
        for link in response.css('a.stream-item__title::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_text, dont_filter=True)
        
        # get urls from featured articles at the top page
        for link in response.css('a.headlink::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_text, dont_filter=True)

        # get urls from featured articles at the middle
        for link in response.css('a.chansec-special-feature__title-wrapper::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_text, dont_filter=True)

        self.driver.close()


    # extract text from url
    def parse_text(self, response):
        words = response.css('div.article-body.fs-article.fs-responsive-text.current-article')
        headers = response.css('div.header-content-container')
        for word in words:
            for header in headers:
                # final output
                yield {
                    'header': header.css('h1.fs-headline.speakable-headline.font-base.font-size::text').get(),
                    'word': word.css('p *::text').getall()
                }
