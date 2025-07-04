from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from collections import deque

def scrape_website_bfs(url, link_selector):
    """
    Scrapes a website using a BFS traversal, yielding BeautifulSoup objects for each page.
    :param url: The starting URL.
    :param link_selector: A function that takes a BeautifulSoup object and returns (left_url, right_url).
    """
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    try:
        queue = deque([url])
        visited = set()
        while queue:
            current_url = queue.popleft()
            if current_url in visited:
                continue
            visited.add(current_url)
            driver.get(current_url)
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            yield soup
            left_url, right_url = link_selector(soup)
            # Enqueue left and right children if not visited
            if left_url and left_url not in visited:
                queue.append(left_url)
            if right_url and right_url not in visited:
                queue.append(right_url)
    except Exception as e:
        print(f"Error fetching {current_url}: {e}")
    finally:
        driver.quit()