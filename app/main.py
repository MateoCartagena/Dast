def suma(a, b):
    return a + b

if __name__ == "__main__":
    import sys
    exec("a = " + sys.argv[1])  # Uso inseguro de exec
    exec("b = " + sys.argv[2])  # Uso inseguro de exec
    print(f"Resultado: {suma(a, b)}")