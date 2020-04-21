question = '''
1. File Owners
https://www.testdome.com/d/python-interview-questions/9


Implement a group_by_owners function that:

Accepts a dictionary containing the file owner name for each file name.
Returns a dictionary containing a list of file names for each owner name, in any order.
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

'''








def group_by_owners(files):
    newDict={}
    for k, v in files.items():
        vv = []
        try:
            for t in newDict[v]:
                vv.append(t)            
        except  :
            pass
        
        vv.append(k)
        newDict.update({ v : vv})
    return newDict

 


if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))
