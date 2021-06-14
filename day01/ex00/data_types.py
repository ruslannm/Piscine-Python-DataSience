#!/usr/bin/python3

def data_types():
    var_int = 42
    var_str = 'quarante-deux'
    var_float = 42.0
    var_bool = True
    var_list = [42]
    var_dict = {42: 42}
    var_tuple = (42,)
    var_set = set()
    vars = (var_int, var_str, var_float, var_bool, var_list, var_dict,\
        var_tuple, var_set)
    print("[", ", ".join(type(var).__name__ for var in vars), "]", sep="")


if __name__ == "__main__":
    data_types()