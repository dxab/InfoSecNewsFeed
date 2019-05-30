#this scraper will pull data from Krebs On Security 
#front page titles

import time, requests, bs4, sys

def main():
	krebspage = requests.get("https://krebsonsecurity.com/")

	#try suite which will close the page if krebs rejects our 
	#scraping advances, program will close out if it does
	try:
		krebspage.raise_for_status()
	except Exception as exc:
		print("Fatal Error: %s" % (exc))
		print("Program exiting...")
		sys.exit()
	krebsoup = bs4.BeautifulSoup(krebspage.text, features="html5lib")
	titlesoup = krebsoup.select(".post-title a")
	outputFile = open('newskreb.txt', "w")
	for x in range(0, len(titlesoup)):
		outputFile.write(titlesoup[x].getText() + "****")
	outputFile.close()
	print("Latest news headlines acquired.")
 





