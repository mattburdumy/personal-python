import bs4, requests

r = requests.get('http://www.zillow.com/homes/make_me_move/house_type/size_sort/39.682734,-106.059759,39.643949,-106.115077_rect/14_zm/0d219582bbX1-CReu25v37plhfi_uph68_crid/1_rs/')

soup = bs4.BeautifulSoup(r.text, 'html.parser')