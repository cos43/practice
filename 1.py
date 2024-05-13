def shortest_way_to_form_string(source, target):
    source_set = set(source)
    if any(char not in source_set for char in target):
        return -1

    count = 0
    i = 0
    while i < len(target):
        j = 0
        start_i = i
        while j < len(source) and i < len(target):
            if source[j] == target[i]:
                i += 1
            j += 1
        if i == start_i:
            return -1
        count += 1
    return count


test_source = ["abc", "abc", "xyz"]
test_target = ["abcbc", "acdbc", "xzyxz"]
for i in range(len(test_source)):
    print(shortest_way_to_form_string(test_source[i], test_target[i]))
