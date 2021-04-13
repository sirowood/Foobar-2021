def max_layer(n):
    array = list(range(1, n))
    layer = 0
    total = 0
    for i in array:
        total += i
        if total > n:
            break
        layer += 1
    print('maxmium layer: ' + str(layer))
