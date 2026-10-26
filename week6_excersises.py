# def concat_dico(dico1:dict, dico2:dict):
#     return_dict = {}
#     for key in dico1:
#         return_dict[key] = dico1[key]
#     for key in dico2:
#         if key in return_dict:
#             values_list = []
#             values_list.append(return_dict[key])
#             values_list.append(dico2[key])
#             return_dict[key] = values_list
#         else:
#             return_dict[key] = dico2[key]
#     return return_dict

# dict1 = {"one":1, "two":2, "five":5}
# dict2 = {"two":"10", "five":"101"}
# concat_dico(dict1, dict2)

# def map_list(keys: list, values: list) -> dict | None:
#     if len(keys) != len(values) or len(set(keys)) != len(values):
#         return None

#     return dict(zip(keys, values))

# map_list(["un", "two"], [1,2])

def reverse_dictionary(dico: dict):
    keys: list = dico.keys()
    values: list = dico.values()
    return_dict = {}
    if len(values) != len(keys) or len(set(values)) != len(keys):
        return None
    
    return dict(zip(values, keys))

reverse_dictionary({"one": 1, "two": 2})
