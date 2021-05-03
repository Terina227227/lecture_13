def recursive_nth_fibo(n):
    if n<=1:
        return 1

    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)

def main():
    kolik_prvku = recursive_nth_fibo(int(input("zadej kolik chces vypsat cisel: ")))
    posloupnost = [recursive_nth_fibo(n) for n in range(kolik_prvku)]
    print(posloupnost)


if __name__ == '__main__':
    main()
