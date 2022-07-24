def examine_buildings_with_sunset(seq):

    candidates = []

    for idx, height in enumerate(seq):

        while candidates and height > candidates[-1][1]:
            candidates.pop()
        candidates.append([idx, height])

    return [bldg[0] for bldg in reversed(candidates)]

seq = [6, 3, 7, 5, 7, 65, 4, 3, 88]

print(examine_buildings_with_sunset(seq))