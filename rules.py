import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class MySpider(CrawlSpider):
    name = 'trabajando.pe'
    allowed_domains = ['rabajando.pe']
    start_urls = ['https://www.trabajando.pe/empleos/oferta/939217/Coordinador-de-la-especialidad-de-Contact-Center.html']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('/oferta', ),deny = ( ' subsection \ .php ' ,  ))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('empleos/oferta/\.html', )), callback='parse_item', follow=True,),
    )
    print (Rule)
    def parse_item(self, response):
        print ("felicidades")
        self.logger.info('.//div[@class="col-md-12 oferta_row"]', response.url)
        item = scrapy.Item()
        item['Empleo'] = response.xpath('.//div[@itemprop="title"]/h1/text()').extract()
        item['Empresa'] = response.xpath('.//h4[@itemprop="hiringOrganization"]/a/text()').extract()
        item['Sector'] = response.xpath('.//h3[@itemprop="industry"]/text()').extract()
        #yield scrapy.Request(response.urljoin(next_page_url))
        yield item.load_item()