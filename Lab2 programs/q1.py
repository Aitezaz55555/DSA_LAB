'''def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return "at position",i+1
    return "element not found"
a=[]
while True:
    elem=input("Enter a element(or enter stop to finish):-")
    if elem.lower()=="stop":
        break
    a.append(int(elem))
b=int(input("Enter the element that is to be found:-"))
print(linear_search(a,b))'''
def binary_search(arr,target):
    low=0
    high=(len(arr))-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return "at position",mid
        elif target>arr[mid]:
            low,high=mid+1,high
        else:
            low,high=low,mid-1
a=[]
while True:
    elem=input("Enter a element(or enter stop to finish):-")
    if elem.lower()=="stop":
        break
    a.append(int(elem))
b=int(input("Enter the element that is to be found:-"))
a.sort()
print(binary_search(a,b))
    
        
    
