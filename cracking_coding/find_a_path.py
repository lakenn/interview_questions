def is_free(x, y):
    if x == 0 and y == 1:
        return False

    return True

def get_path(x, y, path):

    print(x,y)
    if x == 0 and y == 0:
        path.append((x, y))
        return True

    success = False

    if x >= 1 and is_free(x-1, y):
        success = get_path(x-1, y, path)

    if not success and y >= 1 and is_free(x, y-1):
        success = get_path(x, y-1, path)

    if success:
        path.append((x,y))

    return success


path = []
success = get_path(2,2, path)

print(path)