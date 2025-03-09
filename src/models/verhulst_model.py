import math

def logistic_model (r,k,x0, final_time):
    x = [x0]
    for t in range(0, final_time):
        x.append(k / (1 + ((k - x0) / x0) * (pow(math.e, -1 * r * t))))
    return x

def simplified_model(r, x0, terms):
    x = [x0]
    for t in range(terms):
        x.append(r * x[-1] * (1 - x[-1]))
    return x

def exponential_model(r,x0,final_time):
    x = [x0]
    for t in range(0,final_time):
        x.append(x0 * pow(math.e,r*t))
    return x