pattern_list = [0,4,8,12,16,20]

#If we can find the difference between the numbers
#Not just two of them, but all pairs, then we can split
#To have different functions for different types

#Ideally split to different types of patterns function
#Such as linear patterns and fibonacci numbers
#First we need to determine what type of pattern it is

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

#So this is just the start
#My plan is to accomidate as many different patterns as possible
#This is currently only doing linear patterns
#Also if you read these comments you may delete them