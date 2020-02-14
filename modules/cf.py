# cool functions


def collision(one, two, size):
    if one[0] + size <= two[0]:
        return False
    elif two[0] + size <= one[0]:
        return False
    elif one[1] + size <= two[1]:
        return False
    elif two[1] + size <= one[1]:
        return False
    return True
