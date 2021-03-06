import scrapy

"""docstring for PyScraper"scrapy.Spideref __init__(self, arg):
    super(PyScraper,scrapy.Spider.__init__()
    self.arg = arg"""

"""Inheriting Spider class from Scrapy and creating PyScraper sub
class inheriting features from Spider class."""
class PyScraper(scrapy.Spider):
  name = 'brickset_pyscrapy'
  start_urls = ['https://brickset.com/sets/year-2016']

  """selecting .set as css selector for response object. Grabs all the sets
  on the page and loops over them to extract the data. Uses brickset object
  to loop over each set using its own css method to locate set name and
  display"""
  def parse(self, response):
    SET_SELECTOR = '.set'
    for brickset in response.css(SET_SELECTOR):
      NAME_SELECTOR = 'h1 ::text'
      PIECES_SELECTOR = './/dl[dt/text() = "Pieces"]/dd/a/text()'
      MINIFIGS_SELECTOR = './/dl[dt/text() = "Minifigs"]/dd[2]/a/text()'
      RRP_SELECTOR = './/dl[dt/text() = "RRP"]/dd[3]/text()'
      PPP_SELECTOR = './/dl[dt/text() = "PPP"]/dd[4]/text()'
      PKG_SELECTOR = './/dl[dt/text() = "PPP"]/dd[5]/text()'
      AVAIL_SELECTOR = './/dl[dt/text() = "PPP"]/dd[6]/text()'
      FSOLD_SELECTOR = './/dl[dt/text() = "PPP"]/dd[7]/text()'
      INST_SELECTOR = './/dl[dt/text() = "Instructions"]/dd[8]/a/text()'
      ADDIMG_SELECTOR = './/dl[dt/text() = "Additional images"]/dd[9]/a/text()'
      IMAGE_SELECTOR = 'img ::attr(src)'
      yield {
        'name': brickset.css(NAME_SELECTOR).extract_first(),
        'pieces': brickset.xpath(PIECES_SELECTOR).extract_first(),
        'minifigs': brickset.xpath(MINIFIGS_SELECTOR).extract_first(),
        'rrp': brickset.xpath(RRP_SELECTOR).extract_first(),
        'ppp': brickset.xpath(PPP_SELECTOR).extract_first(),
        'pkg': brickset.xpath(PKG_SELECTOR).extract_first(),
        'avail': brickset.xpath(AVAIL_SELECTOR).extract_first(),
        'fsold': brickset.xpath(FSOLD_SELECTOR).extract_first(),
        'inst': brickset.xpath(INST_SELECTOR).extract_first(),
        'addimg': brickset.xpath(ADDIMG_SELECTOR).extract_first(),
        'image': brickset.css(IMAGE_SELECTOR).extract_first(),
      }

    """taking into account that spider would crawl and extract data from
    subsequent pages(if it exists) by adding a next_page response object which
    would extract the required HTML portion and parse it using the parse method
    defined above, extract data and search for the next page again"""
    NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
    next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
    if next_page:
      yield scrapy.Request(
        response.urljoin(next_page),
        callback=self.parse
      )




