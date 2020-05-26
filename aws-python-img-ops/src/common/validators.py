def isnumeric(p):
    if isinstance(p, int):
        return True
    if isinstance(p, str):
        return p.isnumeric()
    return False
