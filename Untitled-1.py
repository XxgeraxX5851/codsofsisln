def calculate(s):
    s = s.replace("plus", "+").replace("minus", "-")
    return str(eval(s))
    pass