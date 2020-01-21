if __name__ == "__main__":
    plus()
    minus()
    multiply()
    slicer()

def plus(*params):
    for item in params:
        res += item
    return res


def minus(*params):
    for item in params:
        res -= item
    return res


def multiply(*params):
    for item in params:
        res *= item
    return res


def slicer(*params):
    for item in params:
        res /= item
        if item == 0:
            return ("Devision on zero ne kryto!")
        else:
            return res
    # if b == 0:
    #     return ("Devision on zero ne kryto!")
    # else:
    #     return a / b
