def nombrespremiers ():
    n = 2
    i = 2
    while n <= 1000:
        while i < n:
            if n % i == 0:
                break
            i +=1
        else:
            print(f"{n} est premier ")
        n += 1
        i = 2
        i = i + 1


nombrespremiers()