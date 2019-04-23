from requests_html import HTMLSession

from product import Product
from database import Database

prepsportswear_schools = {
    # 'centennial': 'centennial-high-school-titans?schoolid=1007205&category=',
    'frisco': 'frisco-high-school-fightin-raccoons?schoolid=183760&category=',
    # 'heritage': 'heritage-high-school-coyotes?schoolid=2299078&category=',
    # 'independence': 'independence-high-school-knights?schoolid=3093477&category=',
    # 'lebanon Trail': 'lebanon-trail-high-school-trail-blazers?schoolid=3249929&category=',
    # 'liberty': 'iberty-high-school-redhawks?schoolid=1282162&category=',
    # 'lone Star': 'lone-star-high-school-rangers?schoolid=2671036&category=',
    # 'memorial': 'frisco-memorial-high-school-warriors?schoolid=3344278&category=',
    # 'wakeland': 'wakeland-high-school-wolverines?schoolid=1006720&category=',
    # 'reedy': 'Rick-Reedy-High-School-Lions/productlist?schoolid=3208016&category='
}
prepsportswear_categories = {
    # The Category Title: The Category ID
    'T-Shirts': '30',
    'Sweatshirts': '305',
    'Hats': '684',
    'Men': '29',
    'Women': '11',
    'Youth': '89',
    'Top Sellers': '183'
}

jostens_schools = {
    'Reedy': 'reedy-high-school'
}

jostens_categories = {
    # The Category Title: The Category ID
    'T-Shirts': 't-shirts',
    'Sweatshirts': 'sweatshirts',
    'Hats': 'hats',
    'Men': 'mens',
    'Women': 'womens',
    'Youth': 'kids',
    'Top Sellers': 'products'
}

data = {
    'T-Shirts': [],
    'Sweatshirts': [],
    'Hats': [],
    'Men': [],
    'Women': [],
    'Youth': [],
    'Top Sellers': []
}


session = HTMLSession()
session.browser


def test():
    return Database.find('frisco', {}).count()


# move session under school area.
def web_scrape():
    # Right now this iterates only through prepsportswear.com
    # In the future, this should be adapted to function for multiple sites

    for school_name, school_id in prepsportswear_schools.items():
        school_url = 'https://www.prepsportswear.com/school/us/Texas/Frisco/' + school_id
        num_skip = 0
        for category_title, category_id in prepsportswear_categories.items():
            category_url = school_url + category_id
            category_session = HTMLSession()
            category_response = category_session.get(category_url)
            links = category_response.html.absolute_links

            for product_url in links:
                if 'https://www.prepsportswear.com/product' in product_url:
                    if num_skip == 0:
                        product_session = HTMLSession()
                        product_response = product_session.get(product_url)
                        product_response.html.render()
                        product_title = product_response.html.find('h2', first=True).text
                        product_price = product_response.html.find('span.priceContent', first=True).text
                        product_img_src = product_response.html.find('img.productImage-Front', first=True).attrs['src']
                        product = Product(title=product_title,
                                          price=product_price,
                                          img_src=product_img_src,
                                          url=product_url,
                                          school=school_name,
                                          category=category_title)
                        print(product_url)
                        Database.insert('products', product.json())
                    else:
                        num_skip = num_skip - 1
                        print('Skipped! ' + str(num_skip) + ' left')

    # for school_name, school_id in jostens_schools.items():
    #     school_url = 'https://schoolstore.jostens.com/school/texas/frisco/' + school_id + '/'
    #     for category_title, category_id in jostens_categories.items():
    #         category_url = school_url + category_id
    #         category_session = HTMLSession()
    #         category_response = category_session.get(category_url)
    #         links = category_response.html.absolute_links
    #
    #         for link in links:
    #             # if this link leads to a product
    #             if '/product' in link:
    #                 product_session = HTMLSession()
    #                 product_response = product_session.get(link)
    #                 product_response.html.render()
    #
    #                 product_title = product_response.html.find('a[href=' + link[39:] + ']', first=True).text
    #                 product_price = product_response.html.find('div.btdzn-add-to-cart-price', first=True).text
    #                 product_img_src = product_response.find('img.btdzn-link-img', first=True).attrs['src']
    #                 print(product_title)
    #                 data[category_title].append({'title': product_title,
    #                                              'price': product_price,
    #                                              'img_src': product_img_src,
    #                                              'url': link})
