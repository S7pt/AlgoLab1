def swap(perforators_list, first_element, second_element):
    buffer = perforators_list[first_element]
    perforators_list[first_element] = perforators_list[second_element]
    perforators_list[second_element] = buffer
