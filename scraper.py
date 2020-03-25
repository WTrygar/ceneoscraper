#import bilbiotek
import requests
from bs4 import 

#adres URL przykładowej strony z opiniami
url = "https://www.ceneo.pl/70948157#tab=reviews"

#pobranie kodu html strny z podanego URL
page_rspons = requests.get(url)
page_tree = BeautifulSoup(page_respons.text, 'html.parser')

#wydobycie z kodu HTML strony fragmentów odpowiadających poszczególnym opiinom
opinions = page_tree.find_all("li", "review-box")

#wydobycie składowych d;a pojedynczej opinii
for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    author = opinion.find("div", "reviewer-name-line").string
    recommendation = opinion.find("div","product-review-summary").find("em").string
    stars = opinon.find("span", "reviewer-score-count")
    try:
        purchased = opionion.find("div","product-review-pz").string
    except IndexError:
        purchased = None
    dates = opinion.find("span", "review-time").find_all("time")
    review_date = dates.pop(0)["datetime"]
    try:
        purchase_date = dates.pop(0)["datetime"]
    except IndexError:
        purchase_date = None
    useful = opinion.find("button","vote-yes").find("span").string
    useless = opinion.find("button","vote-no").find("span").string
    content = opinion.find("p","product-review-body").get_text()
    try:
        pros = opinion.find("div","pros-cell").find("ul").get_text()
    except IndexError:
        pros = None
    try:
        cons = opinion.find("div","cons-cell").find("ul").get_text()
    except IndexError:
        cons = None
