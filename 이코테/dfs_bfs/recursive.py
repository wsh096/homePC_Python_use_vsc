def recursive(n):
    if n>5000:
        return
    print(n,"재귀함수 호출")
    recursive(n+1)

recursive(4999) #현재 pc에서는 1000번 정도 호출하면 
# maximum recursion depth exceeded while calling a Python object 에러 발생