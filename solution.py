# Imports
from collections import Counter
from functools import reduce
import re


# Global Functions
def get_day_input(day:int, cast:type=None, strip:bool=True, split_by:str=None) -> list:
    '''
    Returns list of input values from reading day specific text file
    '''
    out = []
    path = f"./inputs/day_{day}.txt"
    try:
        with open(path, 'r') as file:
            if not split_by:
                data = file.readlines()
            else:
                data = file.read().split(split_by)
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



day_1_input = get_day_input(1, int)
'''
--- Day 1 Part 1: Report Repair ---
'''

def d1p1(expense_report:list, sum_to:int=2020) -> int:
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
        need = sum_to - expense
        match[need] = expense


# Test
day_1_test = [1721, 979, 366, 299, 675, 1456]
# print(d1p1(day_1_test))
# Validate
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
    for i in range(len(expense_report)):
        cur = expense_report[i]
        sum_to = 2020 - cur
        res = d1p1(expense_report[i+1:], sum_to)
        if res:
            return res * cur


# Test
# print(d1p2(day_1_test))
# Validate
# print(d1p2(day_1_input))



day_2_input = get_day_input(2)
'''
--- Day 2 Part 1: Password Philosophy ---
'''

def d2p1(password_report) -> int:
    '''
    Takes in a list of passwords and their policies, cleans strings then evaluates if password is valid
    '''
    cnt = 0
    for req in password_report:
        req_split = req.split()

        # hard code
        x, y = (int(x) for x in req_split[0].split('-'))
        req_range = range(x, y + 1)
        char = req_split[1][0]
        ipt = req_split[2]

        char_cnt = ipt.count(char)
        cnt += 1 if char_cnt in req_range else 0

    return cnt


day_2_test = [
'1-3 a: abcde',
'1-3 b: cdefg',
'2-9 c: ccccccccc'
]

# Test
# print(d2p1(day_2_test))
# Validate
# print(d2p1(day_2_input))


'''
--- Day 2 Part 2: Password Philosophy ---
'''
def d2p2(password_report) -> int:
    '''
    Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    '''
    cnt = 0
    for req in password_report:
        req_split = req.split()

        # hard code
        pos = (int(x) for x in req_split[0].split('-'))
        char = req_split[1][0]
        ipt = req_split[2]

        r = [char == ipt[i - 1] for i in pos]
        cnt += 1 if sum(r) == 1 else 0

    return cnt

# Test
# print(d2p2(day_2_test))
# Validate
# print(d2p2(day_2_input))



day_3_input = get_day_input(3)
'''
--- Day 3 Part 1: Toboggan Trajectory ---
'''

def d3p1(toboggan_map:list, r:int=3, d:int=1, l:int=0, u:int=0) -> int:
    '''
    You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

    The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

    From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.
    '''
    if type(toboggan_map) == str:
        toboggan_map = toboggan_map.split()

    move = lambda x, y: (x + (r - l), y + (d - u))
    tree_cnt = 0
    x, y = 0, 0

    max_x, max_y = len(toboggan_map[0]), len(toboggan_map)

    while (y < max_y):
        row = toboggan_map[y] * (y + 1)
        cur = row[x]


        tree_cnt += 1 if cur == '#' else 0

        x, y = move(x, y)

    return tree_cnt



day_3_test = '''..##.........##.........##.........##.........##.........##.......
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#'''


# Test
# print(d3p1(day_3_test))
# Validate
# print(d3p1(day_3_input))


'''
--- Day 3 Part 2: Toboggan Trajectory ---
'''

def d3p2(toboggan_map:list, slopes:list=[{'r':1,'d':1}, {'r':3,'d':1}, {'r':5,'d':1}, {'r':7,'d':1}, {'r':1,'d':2}]) -> int:
    '''
    Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

    Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    '''
    if type(toboggan_map) == str:
        toboggan_map = toboggan_map.split()

    trees = reduce(lambda x, y: x * y, [d3p1(toboggan_map, **slope) for slope in slopes])

    return trees

# Test
# print(d3p2(day_3_test))
# Validate
# print(d3p2(day_3_input))


day_4_input = get_day_input(4, split_by='\n\n')
passport_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
'''
--- Day 4 Part 1: Passport Processing ---
'''

def d4p1(passport_data:list, required:set={'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}, process_single:bool=False) -> int:
    '''
    The automatic passport scanners are slow because they're having trouble detecting which passports have all required fields. The expected fields are as follows:

    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    '''
    res = None
    if process_single:
        data = dict(map(lambda x: x.split(':'), passport_data.split()))
        if all(data.get(key, False) for key in required):
            res = data
    else:
        res = 0
        passport_dict = [dict(map(lambda x: x.split(':'), data.split())) for data in passport_data]
        for passport in passport_dict:
            if all(passport.get(key, False) for key in required):
                res += 1
    return res



day_4_test = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''.split('\n\n')

# Test
# print(d4p1(day_4_test))
# Validate
# print(d4p1(day_4_input))



requirement = {
    'byr' : lambda b: int(b) in range(1920, 2002 + 1),
    'iyr' : lambda i: int(i) in range(2010, 2020 + 1),
    'eyr' : lambda e: int(e) in range(2020, 2030 + 1),
    'hgt' : lambda n: int(''.join(filter(str.isdigit, n))) in range(150, 193 + 1) if 'cm' in n else int(''.join(filter(str.isdigit, n))) in range(59, 76 + 1),
    'hcl' : lambda h: bool(re.compile("^#[a-f0-9]+").fullmatch(h)),
    'ecl' : lambda c: c.strip() in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid' : lambda p: len("".join(filter(str.isdigit, p))) == 9
}
'''
--- Day 4 Part 2: Passport Processing ---
'''

def d4p2(passport_data:list, requirements:dict=requirement) -> int:
    '''
    The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!

    You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
    '''
    cnt = 0
    for data in passport_data:
        res = d4p1(data, process_single=True)
        if res:
            check_sum = all(req(res[cat]) for cat, req in requirements.items())
            cnt += 1 if check_sum else 0

    return cnt


# Test
# print(d4p1(day_4_test[0], process_single=True))
# print(d4p2(day_4_test))
# Validate
# print(d4p2(day_4_input))


day_5_input = get_day_input(5)
'''
--- Day 5 Part 1: Binary Boarding ---
'''

def translate_cmd(pass_code:str, row_ranges:range=list(range(128)), col_ranges:range=list(range(8))) -> int:
    row_cmds = {
    'F' : lambda row: row[0:len(row)//2],
    'B' : lambda row: row[len(row)//2:len(row)]
    }
    col_cmds = {
    'L' : lambda col: col[0:len(col)//2],
    'R' : lambda col: col[len(col)//2:len(col)]
    }
    res = None
    row = None
    col = None

    for cmd in pass_code:
        row_cmd = row_cmds.get(cmd)
        col_cmd = col_cmds.get(cmd)

        if row_cmd:
            row_ranges = row_cmd(row_ranges)
        elif col_cmd:
            col_ranges = col_cmd(col_ranges)

    row = row_ranges[0]
    col = col_ranges[0]
    res = (row * 8) + col
    return res


def d5p1(passes:list, return_ids:bool=False) -> int:
    """
    The first 7 characters will either be F or B; these specify exactly one of the 128 rows on the plane (numbered 0 through 127). Each letter tells you which half of a region the given seat is in. Start with the whole list of rows; the first letter indicates whether the seat is in the front (0 through 63) or the back (64 through 127). The next letter indicates which half of that region the seat is in, and so on until you're left with exactly one row.
    """

    res = -1
    res_id = []

    for mvmt in passes:
        seat_id = translate_cmd(mvmt)
        res_id.append(seat_id)
        res = seat_id if seat_id > res else res

    return res_id if return_ids else res



day_5_test = ['FBFBBFFRLR']
# Test
# print(d5p1(day_5_test))
# Validate
# print(d5p1(day_5_input, False))

'''
--- Day 5 Part 2: Binary Boarding ---
'''

def d5p2(passes:list) -> int:
    '''
    Ding! The "fasten seat belt" signs have turned on. Time to find your seat.

    It's a completely full flight, so your seat should be the only missing boarding pass in your list. However, there's a catch: some of the seats at the very front and back of the plane don't exist on this aircraft, so they'll be missing from your list as well.

    Your seat wasn't at the very front or back, though; the seats with IDs +1 and -1 from yours will be in your list.

    What is the ID of your seat?
    '''
    sorted_id = list(set(d5p1(passes, True)))
    cur = sorted_id[0]
    for id in sorted_id:
        if cur != id:
            return cur
        cur += 1

# Validate
# print(d5p2(day_5_input))

# day_6_input = get_day_input(6)
'''
--- Day 6 Part 1: Custom Customs ---
'''









#
