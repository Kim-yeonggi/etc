# 길이 단위 변환
# cm <-> in
def centimeter2inch(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = float(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # cm -> inch
            converted = length / 2.54
        elif reverse == True:       # inch -> cm
            converted = length * 2.54
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# m <-> yd
def meter2yard(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # m -> yd
            converted = length * 1.09361
        elif reverse == True:       # yd -> m
            converted = length / 1.09361
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# m <-> ft
def meter2feet(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # m -> ft
            converted = length * 3.2808
        elif reverse == True:       # ft -> m
            converted = length / 3.2808
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# ft <-> yd
def feet2yard(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # m -> yd
            converted = length / 3
        elif reverse == True:       # yd -> m
            converted = length * 3
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# in <-> ft
def inch2feet(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # in -> ft
            converted = length / 12
        elif reverse == True:       # ft -> in
            converted = length * 12
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# km <-> mi
def kilometer2mile(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # km -> mi
            converted = length *0.62137
        elif reverse == True:       # mi -> km
            converted = length /0.62137
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


# yd <-> mi
def yard2mile(length=1, reverse=False, decimal_point=2, *not_used_args):
    try:
        length = int(length)
        reverse = bool(reverse)
        decimal_point = int(decimal_point)
        if reverse == False:        # km -> mi
            converted = length * 1760
        elif reverse == True:       # mi -> km
            converted = length / 1760
    except Exception as e:
        return type(e), e
    else:
        return round(converted, decimal_point)


