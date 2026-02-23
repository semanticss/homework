def solve_discrete_log():
    base = 17
    c = 5
    mod = 31

    for x in range(mod):
        result = pow(base, x, mod)
        
        if result == c:
            print(x)
            return x

    return None

if __name__ == "__main__":
    solve_discrete_log()


