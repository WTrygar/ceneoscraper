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
opinion = opinions.pop()

opinion_id = opinion["data-entry-id"]
author = opinion.find("div", "reviewer-name-line").string
recommendation = opinion.find("div","product-review-summary").find("em").string
stars = opinon.find("span", "reviewer-score-count")
purchased = opinion.find("div","product-review-pz")
# - identyfikator: li.review-box["data-entry-id"]
# - autor: div.reviewer-name-line
# - rekomendacja: div.product-review-summary > em
# - gwiazdki: span.review-score-count
# - potwierdzona zakupem: div.product-review-pz
# - data wystawienia: span.review-time > time["datetime"] - pierwszy element listy
# - data zakupu: span.review-time > time["datetime"] - drugi element listy
useful = opinion.find("button","vote-yes").find("span").string
useless = opinion.find("button","vote-no").find("span").string
content = opinion.find("p","product-review-body").get_text()
# - przydatna: span[id=^vote-yes]
#              button.vote-yes["data-total-vote"]
#              button.vote-yes > span
# - nieprzydatna: span[id=^vote-no]
#              button.vote-no["data-total-vote"]
#              button.vote-no > span
# - treść: p.product-review-body
# - wady: div.cons-cell > ul
# - zalety: div.pros-cell > ul
