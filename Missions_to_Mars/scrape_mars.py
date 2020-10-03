import pandas as pd
from bs4 import BeautifulSoup as bs
from splinter import Browser

def scrap_all():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = mars_news(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": f_link_url(browser),
        "table": tables(),
        "hemisphere_img": hemisphere_image_urls()
    }

    browser.quit()
    return data
def mars_news(browser):

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
   
    news_title_div = soup.find('div', class_='list_text').find('div', class_='content_title')
    news_title = news_title_div.get_text()
    news_title

    news_p_div = soup.find('div', class_='article_teaser_body')
    news_p_div
    news_p = news_p_div.get_text()
    news_p
def f_link_url(browser):
#JPL Mars Space Images - Featured Image
#visit url
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages//?search=&category=Mars'
    browser.visit(url_jpl)

#find image button
    image = browser.find_by_id('full_image')
    image.click()

#find more info button
    browser.is_element_present_by_text('more info', wait_time=1)
    find_button = browser.links.find_by_partial_text('more info')
    find_button.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    image_url_a = soup.find('figure', class_='lede').find('img', class_='main_image').get('src')
    image_url_a

    base = 'https://www.jpl.nasa.gov'

    f_link_url = base + image_url_a
    browser.visit(f_link_url)
    f_link_url
def tables():
#Mars Facts
    table_url = 'https://space-facts.com/mars/'
    browser.visit(table_url)

    tables = pd.read_html(table_url)
    type(tables)
    list
    tables[0]
    df=tables[0]
    df.columns = ['Description', 'Mars']
    # df.head()
    df.set_index('Description', inplace=True)
    # df.head()
    return df.to_html('table.html')
def hemisphere_image_urls():
#Mars Hemispheres
    hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url)

    base = 'https://astrogeology.usgs.gov/'

#Cerberus Hemisphere Enhanced
    cer_hem = browser.links.find_by_partial_text('Cerberus Hemisphere Enhanced')
    cer_hem.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    cer_hem_url = soup.find('img', class_='wide-image').get('src')

    mars_cer = base + cer_hem_url
    mars_cer

#Schiaparelli Hemisphere Enhanced
    sch_hem = browser.links.find_by_partial_text('Schiaparelli Hemisphere Enhanced')
    sch_hem.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    sch_hem_url = soup.find('img', class_='wide-image').get('src')

    mars_sch = base + cer_hem_url
    mars_sch

#Syrtis Major Hemisphere Enhanced
    syr_hem = browser.links.find_by_partial_text('Syrtis Major Hemisphere Enhanced')
    syr_hem.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    syr_hem_url = soup.find('img', class_='wide-image').get('src')

    mars_syr = base + cer_hem_url
    mars_syr

#Valles Marineris Hemisphere Enhanced
    val_hem = browser.links.find_by_partial_text('Valles Marineris Hemisphere Enhanced')
    val_hem.click()

    html = browser.html
    soup = bs(html, 'html.parser')

    val_hem_url = soup.find('img', class_='wide-image').get('src')

    mars_val = base + val_hem_url
    mars_val

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": mars_cer},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": mars_sch},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": mars_syr},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": mars_val},
    ]

    hemisphere_image_urls
