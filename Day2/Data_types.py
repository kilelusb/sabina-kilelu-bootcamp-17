def data_type(A):
    if type(A)==str:
        return len(A)
    elif type(A)==bool:
        return A
    elif type(A)==int:
        if (A < 100):
            return 'less than 100'
        elif (A==100):
            return 'equal to 100'
        else:
            return 'more than 100'
    elif A is None:
        return 'no value'
    elif type(A) is list:
        if len(A)>= 3:
            if A[2]!=None:
                return A[2]
        else:
             return 'None'
        
    else:
         pass
