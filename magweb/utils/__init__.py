def iterable_to_dict(iterable):
    items = {}
    for item in iterable:
        try:
            items.update(item.to_dict())
        except:
            pass
    return items
