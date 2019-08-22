#Mission to Mars: Webscraping 
![mars](img/mars.png) 

##Objective
Build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page created with a flask API. 

##Technologies 
Python 3, Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter, Pandas 

## Explore 
### Step 1: Web Scraping with Beautful Soup 

1.) Create and activate a new [Virtual Enviornment](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1)

2.) Download 
and install required technologies within new enviornment 
	
- Python 3 + Libraries: 
	* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
	* [Splinter](https://pypi.org/project/splinter/#files)
	* [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/install.html)   
	* [Pymongo](https://docs.opsmanager.mongodb.com/v1.2/monitoring/tutorial/install-pymongo/#easy-installation) 
	* [Selenium] (https://selenium-python.readthedocs.io/installation.html) 
	* [Chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) 
		*	 make sure chrome driver is placed in the correct system path `hd/usr/bin/'chromedriver'` (mac)

2.) Deploy a jupyter notebook within the downloaded repo

3.) Work through `Mission2Mars.ipynb` to employ webscraping code 

### Step 2: Web Deployment with Flask 

4.) Navigate to repo's `app` folder with a CLI. 

5.) To print scraped data to terminal: 
		
			python scrape_mars.py

6.) To view HTML page with scrape results:
	
			python app.py 