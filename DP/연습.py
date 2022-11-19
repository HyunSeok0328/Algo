stack1 = [2,7]
stack2 = [4,5]
stack3 = [1]
arr = []
ans = []
for i in range(len(stack1)) :
    arr.append(stack1[i])
for i in range(len(stack2)) :
    arr.append(stack2[i])
for i in range(len(stack3)) :
    arr.append(stack3[i])
arr.sort(reverse=True)
for i in range(len(arr)) :
    if arr[i] in stack1 :
        ans.append("1")
    elif arr[i] in stack2 :
        ans.append("2")
    elif arr[i] in stack3 :
        ans.append("3")
print("".join(ans))