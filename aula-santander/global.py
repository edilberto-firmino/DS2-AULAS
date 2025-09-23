def funcao1():
    varivel_local = 10
    return varivel_local

variavel_global = 20

def funcao2():
    return variavel_global

result_local = funcao1()
result_global = funcao2()

print(f"valor da varivel local {result_local}")
print(f"valor da varivel global {result_global}")

print(variavel_global)
