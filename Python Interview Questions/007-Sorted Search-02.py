question = '''
https://www.testdome.com/d/python-interview-questions/9 
 
Sorted SearchALGORITHMIC THINKING BINARY SEARCH   Hard 
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.

'''


def count_numbers(sorted_list, less_than):
    lys = sorted_list
    val = less_than
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
            return index 
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return (index +1)

if __name__ == "__main__":
    sorted_list = [1,  2,3,4,5,15]
    print(count_numbers(sorted_list, 4))  # should print 2
