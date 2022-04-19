def tag_search(q, tags):

    matches = []

    for term in q:
        for tag in tags:
            if term in tag['item']:
                matches.append(tag)

    return matches




tags = [
    {'item': 'oranges'},
    {'item': 'apples'},
    {'item': 'appliances'}
]
'''
result = tag_search('apples', tags)
assert result['item'] == 'apples'

result = tag_search('oranges', tags)
assert result['item'] == 'oranges'

result = tag_search('doesnt exist', [])
assert result == None

results = tag_search("app", tags)
assert len(results) == 2

results = tag_search("es", tags)
assert len(results) == 3

results = tag_search("poop", tags)
assert len(results) == 0
'''

results = tag_search(["app", "es", "poop"], tags)
assert len(results) == 5