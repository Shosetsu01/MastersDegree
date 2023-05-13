def sven_method(x0, h, f):
    left_f_x0, f_x0, rigth_f_x0 = f(x0 - h), f(x0), f(x0 + h)
    if left_f_x0 >= f_x0 <= rigth_f_x0:
        return (x0 - h, x0 + h)
    if left_f_x0 <= f_x0 >= rigth_f_x0:
        return None 
    if left_f_x0 >= f_x0 >= rigth_f_x0:
        x1 = x0 + h 
    if left_f_x0 <= f_x0 <= rigth_f_x0:
        x1 = x0 - h
        h = -h
    h *= 2
    while f(x1) < f(x0):
        tmp = x0 
        x0 = x1
        x1 = x0 + h
        h *= 2

    if h > 0:
        return(tmp, x1)
    return (x1, tmp)
    