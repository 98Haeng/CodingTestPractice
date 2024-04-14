from collections import Counter
def main(): 
    x,k = map(int, input().split())
    socks = list(map(int, input().split()))

    L = Counter(socks[:x])
    R = Counter(socks[x:])
    
    ans = x * x
    for i in range(1, k+1):
        ans -= L[i] * R[i]
    
    print(ans)

if __name__ == "__main__":
    main()