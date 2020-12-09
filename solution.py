# Imports
from collections import Counter

# Global Functions
def get_day_input(day:int, cast:type=None, strip:bool=True) -> list:
    '''
    Returns list of input values from reading day specific text file
    '''
    out = []
    path = f"./inputs/day_{day}.txt"
    try:
        with open(path, 'r') as file:
            data = file.readlines()
            for raw in data:
                clean = raw
                if strip:
                    clean = clean.strip()
                if cast:
                    clean = cast(clean)
                out.append(clean)
    except:
        pass
    return out



'''
--- Day 1 Part 1: Report Repair ---
'''

def d1p1(expense_report:list) -> int:
    '''
    Given an expense report (a list of integers), find the TWO entries that sum to 2020 and multiply both numbers together.

    Example:

    [1721, 979, 366, 299, 675, 1456]

    This expense report shows that 1721 (idx 0) and 299 (idx 3) sum up to 2020. The solution for this is 1721 * 299 -> 514579
    '''
    match = {}
    for expense in expense_report:
        found = match.get(expense, None)
        if found:
            return (found * expense)
        need = 2020 - expense
        match[need] = expense


# Test
day_1_test = [1721, 979, 366, 299, 675, 1456]
# print(d1p1(day_1_test))
# Validate
day_1_input = get_day_input(1, int)
# print(d1p1(day_1_input))


'''
--- Day 1 Part 2: Report Repair ---
'''

def d1p2(expense_report:list) -> int:
    '''
    Given an expense report (a list of integers), find the THREE entries that sum to 2020 and multiply all THREE numbers together.

    Example:

    [1721, 979, 366, 299, 675, 1456]

    This expense report shows that 979 (idx 1), 366 (idx 2), 675 (idx 4) sum up to 2020. The solution for this is 979 * 366 * 675 -> 241861950
    '''
    

# Test
# print(d1p2(day_1_test))
# Validate
# print(d1p2(day_1_input))
