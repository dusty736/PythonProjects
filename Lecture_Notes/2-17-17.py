rolls = [1,5,4,6,2,1,1,3,2,5]

def rolls_to_hist(rolls):
    possible_rolls = range(0,7)
    counts = []

    for possibility in possible_rolls:
        roll_count = 0
        for roll in rolls:
            if roll == possibility:
                roll_count += 1
        counts.append(roll_count)
    print counts
    return counts
    
    #Easy code
    # result = [0, 0, 0, 0, 0, 0, 0]
    # for roll in rolls:
    #      result[roll] += 1
    # return result

assert rolls_to_hist(rolls) == [0, 3, 2, 1, 1, 2, 1]

def normalize(alist):
    total_counts = 0
    normalized_lst = []
    for count in alist:
      total_counts += count

    for count in alist:
      normalized_lst.append(float(count) / total_counts)
    print normalized_lst
    return normalized_lst
    
    #Easy code
    # list_sum = float(sum(alist))
    # norm_list = []
    # for elt in alist:
    #     normalized = elt / list_sum  
    #     norm_list.append(normalized)
    # return norm_list

assert normalize([3, 1, 0, 3, 2, 1]) == [.3, .1, 0, .3, .2, .1]
