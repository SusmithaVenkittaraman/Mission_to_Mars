#!/usr/bin/env python
# coding: utf-8

# # Mission to Mars

# ## Importing all the dependencies

# In[36]:


#Dependencies

from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# ## Splinter Setup

# In[37]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Getting the latest news and description from https://mars.nasa.gov/news/

# In[38]:


#url
url='https://mars.nasa.gov/news/'

browser.visit(url)

html=browser.html

#convert the brouser html to a soup object and then quit the browser

new_soup=BeautifulSoup(html,'html.parser')

slide_element=new_soup.select_one("ul.item_list li.slide")


news_title=slide_element.find("div",class_="content_title").get_text()
news_paragraph=slide_element.find("div",class_="article_teaser_body").get_text()
print(news_title+" " +news_paragraph)



# ### Getting the featured image from https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html

# In[39]:


# visit URL
url="https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"

browser.visit(url)


html=browser.html

#convert the brouser html to a soup object and then quit the browser

new_soup_1=BeautifulSoup(html,'html.parser')

image=new_soup_1.find("a",class_="showimg fancybox-thumbs")

print("https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"+image['href'])


# ### Getting the mars facts from https://space-facts.com/mars/

# In[40]:


#mars facts

df=pd.read_html("https://space-facts.com/mars/")[0]
df.columns=["Description","Mars"]
df.set_index("Description", inplace=True)
df


# In[41]:


#converting to html
df.to_html()



# ### getting the images from https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

# In[42]:


# visit URL
url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

browser.visit(url)

hemisphere_image_urls = []

# First get a list of all the hemisphere
links = browser.find_by_css("a.product-item h3")

for index in range(len(links)):
    hemisphere = {}
    
    browser.find_by_css("a.product-item h3")[index].click()
    
    # Next is find the sample image anchor tag and extract the href 
    sample_element = browser.links.find_by_text("Sample").first
    title = browser.find_by_css("h2.title").text
    link = sample_element["href"]
    
    hemisphere["title"] = title
    hemisphere["link"] = link
    
    hemisphere_image_urls.append(hemisphere)
    browser.back()

print(hemisphere_image_urls)
    


# In[ ]:





# In[ ]:




