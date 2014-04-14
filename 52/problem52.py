# Problem 52: Permuted multiples
#
# Problem Statement
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.


def sort_characters(my_string):
    '''
    Sorts characters in a string alphabetically.
    
    Examples:
    12  => 12
    21  => 12
    312 => 123
    '''
    my_string = str(my_string)
    return ''.join(sorted(my_string))


def is_permuted_multiples(x):
    # Multiply x by 1 through 6 and sorts digits alphabetically
    multiples = [sort_characters(c * x) for c in range(1, 7)]
    
    # Checks to see if all the multiples are equal
    # This checks if they share the same digits
    all_equal = (len(set(multiples)) == 1)
    
    return all_equal


def solve_problem_52():
    x = 1
    while True:
        found_solution = is_permuted_multiples(x)
        if found_solution:
            print x
            return
        else:
            x += 1


if __name__ == "__main__":
    solve_problem_52()
