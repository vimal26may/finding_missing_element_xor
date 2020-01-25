def missing_element_xor(main_set, missing_elm_set):
    xor_num=0
    for num in main_set:
        xor_num ^= num # Performing (A^B^C^D) where {A,B,C,D} is our set
    for num in missing_elm_set:
        xor_num ^= num # Performing (xor_num^(A^B^C)) where {A,B,C} is missing_elm_set
    return xor_num
