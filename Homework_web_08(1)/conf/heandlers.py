import conf.connect as connect

import redis
from redis_lru import RedisLRU

from conf.models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag):
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result

def find_by_tags(tag):
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__in=tag)
    result = [q.quote for q in quotes]
    return result

@cache
def find_by_author(author):
    print(f"Find by {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result

if __name__ == '__main__':
    find_by_tag()
    find_by_tags()
    find_by_author()
