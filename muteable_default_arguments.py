def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items


print(add_item(10))
print(add_item(29))
