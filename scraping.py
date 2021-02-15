'''
Sehajpreet Kaur
Aditi KP
Sejal Bansal

Data has been mined from Tripadvisor
'''

# import libraries
import urllib.request
from bs4 import BeautifulSoup
import csv

reviews = []  # list to store mined reviews
ratings = []  # list to store rating associated with each review
overall_rating = ''

def scrape(soup, reviews, ratings):
    for r in soup.find_all('div', {'class': 'cPQsENeY'}):
        rev = r.find('span')
        if rev:
            rev = str(rev)  # convert to string
            rev = rev[6: -7]  # slice to remove extra tags
            if rev[0:5] != 'class':  # ensure it does not include replies to reviews
                reviews.append(rev)
    print(len(reviews))

    for r in soup.find_all('div', {'class': 'location-review-review-list-parts-RatingLine__bubbles--GcJvM'}):
        rating = r.find('span')
        rating = str(rating)
        rating = rating[37: -10]  # slice to only take the rating
        ratings.append(rating)
    print(len(ratings))


for i in range(0, 121, 5):  # reviews are most recent first; taking 120 reviews
    if i==0:
        urlpage = 'https://www.tripadvisor.in/Hotel_Review-g294265-d7736497-Reviews-JW_Marriott_Hotel_Singapore_South_Beach-Singapore.html'
    else:  # pagination
        urlpage = 'https://www.tripadvisor.in/Hotel_Review-g294265-d7736497-Reviews-or' + str(i) + '-JW_Marriott_Hotel_Singapore_South_Beach-Singapore.html'
    print(urlpage)
    page = urllib.request.urlopen(urlpage)  # query the website and return the html to the variable 'page'
    soup = BeautifulSoup(page, 'html.parser')  # parse the html using beautiful soup and store in variable 'soup'
    s = soup.find('span', {'class': 'hotels-hotel-review-about-with-photos-Reviews__overallRating--vElGA'})
    overall_rating = str(s)
    overall_rating = overall_rating[82: -7]
    scrape(soup, reviews, ratings)


with open('JW Marriott South Beach.csv','w', newline='', encoding="utf-8") as f_output:  # write reviews and corresponding ratings to csv file
    csv_output = csv.writer(f_output)
    csv_output.writerow(['Review ', 'Rating'])
    for i in range(len(reviews)):
        csv_output.writerow([reviews[i], ratings[i]])
    csv_output.writerow([])
    csv_output.writerow(['Overall Rating', overall_rating])
