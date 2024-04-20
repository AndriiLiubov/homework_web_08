import json

from mongoengine.errors import NotUniqueError

from conf.models import Author, Quote

import conf.connect as connect


def set_authors(file):
    with open(f'files/{file}', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author = Author(fullname=el.get('fullname'), born_date=el.get('born_date'),
                                born_location=el.get('born_location'), description=el.get('description'))
                author.save()
            except NotUniqueError:
                print(f"Such author already exists {el.get('fullname')}")

def set_qoutes(file):
    with open(f'files/{file}', encoding='utf-8') as fd:
        data = json.load(fd)
        for el in data:
            try:
                author, *_ = Author.objects(fullname=el.get('author'))
                quote = Quote(quote=el.get('quote'), tags=el.get('tags'), author=author)
                quote.save()
            except NotUniqueError:
                print(f"Such quote already exists {el.get('quote')}")

if __name__ == '__main__':
    set_authors('authors.json')
    set_qoutes('qoutes.json')