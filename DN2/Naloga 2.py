our_list = [1,2,3,4,5,6,7]

our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}

our_tuple = (357, 12, 12, 8, 5, 2, 2)

our_dict["d"] = our_list[4]

del our_list[4]

nov_tuple = ()

for v in our_dict.values():
    nov_tuple = nov_tuple + (v,)

for i in range(0, len(nov_tuple)):
    if our_tuple[i] == nov_tuple[i]:
        print(str(i + 1) + ". vrednost " + "(" + str(nov_tuple[i]) + ")" + " iz nov_tuple NI enaka " + str(i + 1) + ". vrednosti " + "(" + str(our_tuple[i]) + ")" +" iz our_tuple.")
    elif our_tuple[i] != nov_tuple[i]:
        print(str(i + 1) + ". vrednost " + "(" + str(nov_tuple[i]) + ")" + " iz nov_tuple NI enaka " + str(i + 1) + ". vrednosti " + "(" + str(our_tuple[i]) + ")" +" iz our_tuple.")
    
