def find_missing(A,B):
    #checking if the list contains only integers

    AandB=A+B
    if all(isinstance(item,int) for item in AandB) and all(item>0 for item in AandB):
           array1=set(A)
           array2=set(B)

           if (array1== array2) or array1==[] or array2==[]:
               return 0
           elif (len(array1)-len(array2))==1:
               return list(array1-array2)[0]
           elif (len(array2)-len(array1))==1:
               return list(array2-array1)[0]
           else:
               return 'Missing number cannot be more than one'
