def tag_search(q, tags):

    for tag in tags:
        if tag['item'] == q:
            return tag

    return None



tags = [
    {'item': 'oranges'},
    {'item': 'apples'},
]
result = tag_search('apples', tags)
assert result['item'] == 'apples'

result = tag_search('oranges', tags)
assert result['item'] == 'oranges'

result = tag_search('doesnt exist', [])
assert result == None