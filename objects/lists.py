def chain(lst):
    t = ''
    for i in range(len(lst)):
        t = t + ' ' + lst[i]
    return t[1:]
