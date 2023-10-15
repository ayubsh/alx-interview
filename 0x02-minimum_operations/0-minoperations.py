#!/usr/bin/python3
''' minimun ops
'''


def minOperations(n):
    '''minimum operations
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    clp = 0
    done = 1
    while done < n:
        if clp == 0:
            clp = done
            done += clp
            count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            clp = done
            done += clp
            count += 2
        elif clp > 0:
            done += clp
            count += 1

    return count
