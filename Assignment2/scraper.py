#-------------------------------------------------------------------------
# AUTHOR: Diego Mejia
# FILENAME: scraper.py
# SPECIFICATION: This program is a solution to question 8 of the assignment,
#      That will crawl the circular links section of TestingURL.dev starting from
#      the seed URL defined below.
# FOR: CS 4250 - Assignment #2
# TIME SPENT: 3 hrs
#-------------------------------------------------------------------------

# Importing Python libraries
import requests
from bs4 import BeautifulSoup

# Defining the seed URL
seed = "https://testingurl.dev/scraping/links/circular"
baseURL = "https://testingurl.dev"

# Creating the frontier and seen collections
# --> add your Python code here
frontier = [seed]
seen = set([seed])

# Crawling until the frontier is empty
while frontier:

    # Removing the first URL from the frontier
    # --> add your Python code here
    url = frontier.pop(0)

    # Retrieving and parsing the Web page
    # --> add your Python code here
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html.parser")


    # Printing the text contained in the <h1> element
    # --> add your Python code here
    print(f'URL: {url} - H1: {soup.find("h1").text}')


    # Extracting and processing hyperlinks
    # --> add your Python code here
    # get all links from the page
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    # convert relative URLs to absolute URLs
    links = [link if link.startswith("http") else baseURL + link for link in links]

    for link in links:
        if link.startswith("https://testingurl.dev/scraping/links/circular") and link not in seen:
            frontier.append(link)
            seen.add(link)
        


# Printing all URLs in seen
# --> add your Python code here
print(f"\nVisited URLs:\n==============\n\n{"\n".join(seen)}\n")