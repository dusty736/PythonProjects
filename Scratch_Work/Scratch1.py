input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 9]
output_set = set([])
for i in input_list:
    output_set.add(i)

set_one = {'a', 'b', 'c', 'd', 'e', 'f'}
set_two = {'a', 'c', 'd', 'g'}
# print set_one & set_two

weather = {
    'Monday': {'low': 45, 'high': 62, 'precipitation': 0.3},
    'Tuesday': {'low': 48, 'high': 69, 'precipitation': 0.2},
    'Wednesday': {'low': 42, 'high': 58, 'precipitation': 0.5},
}

# print weather['Monday']['high']
# print weather['Tuesday'][0]
# print weather['Wednesday']

def total_spent():