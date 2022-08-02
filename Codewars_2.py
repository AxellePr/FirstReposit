
numbers = [1, 2, 3, 4, 5]
def sum_two_smallest_numbers(numbers):
    res = sorted(numbers)
    return res[0] + res[1]
print(sum_two_smallest_numbers(numbers))

def get_middle(str):
    if len(string) % 2 != 0:
        middle_letter = int(len(string) / 2)
        return string[middle_letter:middle_letter + 1]
    else:
        two_middle = int(len(string) / 2)
        return string[two_middle -1 :two_middle  + 1]
string = 'stoyns'
print(get_middle(string))