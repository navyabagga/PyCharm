import operator
import sys


def employee_lister(f):
    def inner(employee):
        # write code
        print(employee)

    return inner


@employee_lister
def name_format(employee):
    return ("Mr." if employee[3] == "M" else "Ms.") + employee[0] + " " + employee[1]


if __name__ == "main":
    employee = map(lambda x: sys.argv[2].split()[4 * x:(x + 1) * 4], range(int(sys.argv[1])))
    print('\n'.join(name_format(employee)))