import re
import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from sys import argv


def create_soup_object(url_link):
    page =  requests.get(url_link)

    return BeautifulSoup(page.content, 'html.parser')


def print_html(soup, file_name):
    '''
    This function will write the raw html format of the given soup file into
    a html file.
    '''
    with open(file_name, 'w', encoding='utf-8') as writer:
        writer.write(soup.prettify())


def scroll_link(url_link):
    '''
    Scroll the given web page and returns the page source code as soup object
    '''
    browser = webdriver.Chrome(executable_path='chromedriver.exe')

    browser.get(url_link)

    for i in range(50):
        time.sleep(2)
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    source_data = browser.page_source

    soup = BeautifulSoup(source_data, 'html.parser')

    # print_html(soup, 'selenium_test.html')

    return soup


def create_url_list(href_list):
    url_list = []

    for href in href_list:
        url_list.append(href.get('href'))

    # Remove duplicates URLS
    url_list = list(set(url_list))

    return url_list


def get_menu_urls(url_link, check_html=False, file_name=None):
    '''
    This function will retrieve all the URLS on the menu bar of the web page.

    Return
    ------
    url_menu_list: list
        URLS of the menu bar
    '''
    soup = create_soup_object(url_link)

    if check_html:
        print_html(soup, file_name)

    # Get all the <a> links with topics inside the url
    url_menu = soup.find_all('a', attrs={'href':
               re.compile("^http://news.sabay.com.kh/topics/")})

    # Store the URLS
    url_menu_list = []

    for menu in url_menu:
        url_menu_list.append(menu.get('href'))

    # Remove duplicate URLS
    url_menu_list = (set(url_menu_list))

    return url_menu_list


def get_article_urls(url_link, check_html=False, file_name=None):
    '''
    Scroll through each given link and capture all the article links

    Return
    ------

    '''
    # Step 1: Print some information
    topic = re.findall('topics/(.+)$', url_link)[0]
    print('Scraping:', topic)

    # Step 2: Scroll through the given link
    soup = scroll_link(url_link)

    if check_html:
        print_html(soup, file_name)

    # Step 3: Get all the <a> links with word article inside the URL
    url_article = soup.find_all('a', attrs={'href':
                  re.compile("^http://news.sabay.com.kh/article" +
                  "/.+#utm_campaign")})

    # Step 4: Get all unique article URLS
    url_list = create_url_list(url_article)

    # Step 5: Print the number of acquired links
    print('Count:', len(url_list))
    print()

    return url_list


def write_article_content(url_link, check_html=False, file_name=None):
    '''
    Write the title and paragraph content from the given url link
    '''
    soup = create_soup_object(url_link)

    title = soup.find('div', class_='title detail')

    article = soup.find('div', class_='detail content-detail').find_all('p')

    # Check article content
    with open(file_name, 'a', encoding='utf-8') as writer:
        writer.write('Article source: ' + str(url_link))
        writer.write('\n\n')
        writer.write(title.get_text())
        writer.write('\n')
        for line in article:
            writer.write(line.get_text())
            writer.write('\n')
        writer.write('\n-----')
        writer.write('\n\n\n')


if __name__ == '__main__':
    MAIN_URL = 'http://news.sabay.com.kh/'

    # Get the menu bar URLS
    menu_urls = get_menu_urls(MAIN_URL)

    #
    article_urls = []

    # Loop through each menu bar URLS
    for menu_url in menu_urls:
        article_urls.extend(get_article_urls(menu_url))

    # Ensure no duplicates
    article_urls = list(set(article_urls))
    print('Total URLS:', len(article_urls))

    # Write the content of each articles
    for article_url in article_urls:
        write_article_content(article_url, file_name='sabay_scrape.txt')
