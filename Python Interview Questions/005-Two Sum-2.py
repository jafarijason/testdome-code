question = '''
https://www.testdome.com/d/python-interview-questions/9 
 
5. Two SumALGORITHMIC THINKING DICTIONARY   Easy 
Write a function that, when passed a list and a target sum, returns, efficiently with respect to time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to the target sum. If there are no two numbers, the function should return None.

For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the following pairs of indices:

0 and 3 (or 3 and 0) as 3 + 7 = 10
1 and 5 (or 5 and 1) as 1 + 9 = 10
2 and 4 (or 4 and 2) as 5 + 5 = 10

'''


def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
    u=-1
    h =-1
    dictt ={}
    for i in range(0, len(numbers)):
        dictt.update({str(numbers[i]): i})
        # print(dictt)
        if u >= 0:
            kl = (u,h)
            return kl         
        try:    
            jk = (target_sum-numbers[i])
            ss = dictt[str(jk)]
            # print(ss)
            if i != ss :
                u = i
                h= ss
        except  :
            pass

    return None


if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))
