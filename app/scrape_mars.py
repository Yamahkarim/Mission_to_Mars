
#Import Dependencies
from splinter import Browser
from bs4 import BeautifulSoup 
import requests
import pandas as pd
import datetime as dt
from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our MongoDB database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Create variable for splinter browser
browser = Browser("chrome", executable_path="chromedriver", headless=True)


#Initiate Function to Scrape all information
def web_scrape():
    #Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)
    news_title, news_paragraph = mars_news(browser)

    #Run scraping function and store in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "mars_image": mars_image(browser),
        "hemispheres": hemi_scrape(browser),
        "weather": mars_weather(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now()
    }
    # Stop webdriver and return data
    browser.quit()
    return data

# Scrape Recent News from Nasa Mars Website
def mars_news (browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    try:
       #website elements were recently changed and comments reflect original website html elements
       #recent = news_soup.find('div', class_='list_text').text
        # news_title = recent.find_all('div', class_='content_title').text
        # news_pgraph = recent.find_all('div', class_='article_teaser_body').text
        news_title = soup.find('div', class_='content_title').text
        news_pgraph = soup.find('div', class_='article_teaser_body').text
        print(news_title,news_pgraph)
        return news_title, news_pgraph
    except AttributeError:
        return None, None

    return None, None


# JPL Mars Space Images


def mars_image(browser):
# Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
#create soup object
    img_soup = BeautifulSoup(html, 'html.parser')

# Scrape URL for featured Mars image
    img_find = img_soup.find('footer')
    img = img_find.find('a', class_='button fancybox')['data-fancybox-href']
    img_url = "https://jpl.nasa.gov" + img
    featured_image_url = img_url

    try:
        img_url_rel = img.get("src")

    except AttributeError:
        return None


        img_url = f"https://www.jpl.nasa.gov {img_url_rel}"

    return featured_image_url


# Mars Weather
# Retrieve most recent tweet about the weather on Mars
def mars_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    weather_soup = BeautifulSoup(html, 'html.parser')

    tweet_box = weather_soup.find('div', class_='js-tweet-text-container')
    tweet = tweet_box.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather = tweet
    return mars_weather


# Mars Facts
def mars_facts():
    url = 'https://space-facts.com/mars/'
    #response = requests.get(url)
    browser.visit(url)
    try:
        Mars_df = pd.read_html('https://space-facts.com/mars/')[1]
    except BaseException:
        return None

    Mars_df.columns=['description', 'value']
    Mars_df.set_index('description', inplace=True)
    Mars_df


    #read the data to HTML
    return Mars_df.to_html()
    browser.quit()


# Mars Hemisphere Images
def hemi_scrape(html_text):
#Visit Website for Mars Hemisphere Images 
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_urls = []

    for h in range(4):
        browser.find_by_tag('h3')[h].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h2', class_='title').text
        img_url_partial = soup.find('img', class_='wide-image')['src']
        img_url = 'https://astrogeology.usgs.gov' + img_url_partial
        dict = {'title':title, 'img_url':img_url}
        hemisphere_image_urls.append(dict)
        browser.back()

    return hemisphere_image_urls

if __name__ == "__main__":
    # If running as script, print scraped data
    print(web_scrape())




