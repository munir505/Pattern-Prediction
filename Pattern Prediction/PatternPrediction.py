pattern_list = [0,4,8,12,16,20]

def linear_pattern (list_pattern):
    difference = find_difference(list_pattern[0], list_pattern[1])
    return pattern_list[len(pattern_list) - 1] + difference

def find_difference (value_one, value_two):
    difference = value_two - value_one
    return difference

def pattern_type (list_pattern):
    difference_list = []
    pattern_type = ""
    for x in range (len(list_pattern) - 1):
        difference = find_difference(list_pattern[x], list_pattern[x+1])
        difference_list.append(difference)
        if(difference_list[x - 1] != difference):
            pattern_type = "Other"
        else:
            pattern_type = "Linear"
    if(pattern_type == "Linear"):
        return linear_pattern(list_pattern)
        

def main():
    print(pattern_type(pattern_list))

main()
