"""
Challenge:
Each line of the input file describes the policy. Count how many passwords are valid.
"""

import itertools
from functools import reduce

input = "./input"


def parse_row_p1(row):
    """
    parse a row of the file. The rule is the range given describes the number of times
    the specified letter must appear in the password

    Parameters:
    row : str
      space-separated string containing number range, letter, and password

    Output:
    valid : bool
      True if password is valid, else False
    """
    nrange, letter, pwd = row.split(' ')
    nrange = [int(i) for i in nrange.split('-')]
    letter = letter[:-1]
    nletter = pwd.count(letter)
    valid = (nletter >= nrange[0]) and (nletter <= nrange[1])
    return valid


def parse_row_p2(row):
    """
    parse a row of the file. The rule is that the range given describes the *positions*
    that the specified letter must appear in, in the password. Also, make sure to index
    from 1, not 0.

    Parameters:
    row : str
      space-separated string containing number range, letter, and password

    Output:
    valid : bool
      True if password is valid, else False
    """
    nrange, letter, pwd = row.split(' ')
    pos = [int(i)-1 for i in nrange.split('-')]
    letter = letter[:-1]
    has_letter = [pwd[p] == letter for p in pos]
    # make sure only 1 position has the letter
    valid = (all(has_letter) == False) and (any(has_letter) == True)
    #print(nrange, pos, letter, pwd, has_letter, all(has_letter), any(has_letter))
    return valid

if __name__ == '__main__':
    pwd_counter = {'good': 0, 'bad': 0 }
    with open(input) as file:
        line = file.readline()
        while line != '':
            valid = parse_row_p2(line)
            if valid == True:
                pwd_counter['good'] += 1
            else:
                pwd_counter['bad'] += 1
            line = file.readline()
    print(pwd_counter)
