def k_most_frequent(lst, k):
    
    elements = {}

    for x in lst:
        if x not in elements:
            elements[x] = 1
        
        else:
            elements.update({x: elements[x] + 1})

    print(elements)

    items = []
    keys = []
    for x, y in elements.items():
        items.append((x, y))
        keys.append(x)

    if k >= len(keys): return keys

    items.sort(key=lambda x: x[1], reverse = True)

    print(items)

    final_elements = []
    for x in range(len(items)):
        print((items[x])[0])
        print(k)
        print("___")
        final_elements.append((items[x])[0])
        if x != len(items) - 1:
            if (items[x])[1] != (items[x+1])[1]: k -= 1
        
        if k == 0: break

    return final_elements


print(k_most_frequent([1, 1, 1, 2, 2, 3], 2))
