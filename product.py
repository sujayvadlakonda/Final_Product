class Product(object):
    def __init__(self, title, price, img_src, url, school, category):
        self.title = title
        self.price = price
        self.img_src = img_src
        self.url = url
        self.school = school
        self.category = category

    def json(self):
        return {'title': self.title,
                'price': self.price,
                'img_src': self.img_src,
                'url': self.url,
                'category': self.category,
                'school': self.school}

    def __repr__(self):
        return 'Title: ' + self.title + ' Price: ' + self.price + ' Img_Src: ' + self.img_src + ' URL: ' + self.url + ' School: ' + self.school + ' Category: ' + self.category
