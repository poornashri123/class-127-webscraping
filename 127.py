from selenium import webdriver
from bs4 import BeutifulSoup
import time 
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Proper name","Distance","Mass","Radius"]

    scrape()


