question = '''
https://www.testdome.com/d/python-interview-questions/9 
 
Sorted SearchALGORITHMIC THINKING BINARY SEARCH   Hard 
Implement function count_numbers that accepts a sorted list of unique integers and, efficiently with respect to time used, counts the number of list elements that are less than the parameter less_than.

For example, count_numbers([1, 3, 5, 7], 4) should return 2 because there are two list elements less than 4.

'''

 

def count_numbers(sorted_list, less_than):
     first = 0
     last = len(sorted_list)-1
     mid = (first + last)//2
     if less_than ==sorted_list[mid]:
         return mid
     elif  :
         pass


        
       


if __name__ == "__main__":
    sorted_list = [1,  3,9,15]
    print(count_numbers(sorted_list, 4))  # should print 2
