links = [
    "www.google.com",
    "www.youtube.com",
    "www.x.com",
    "www.walmart.org",
    "www.wallstreet.web"
]

for link in links:
    web_name = link.removeprefix('www.')
    web_name = web_name.removesuffix('.com')
    web_name = web_name.removesuffix('.org')
    web_name = web_name.removesuffix('.web')
    print(web_name)


