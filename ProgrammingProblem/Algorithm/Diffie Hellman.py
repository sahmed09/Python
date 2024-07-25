def power(a, b, P):
    if b == 1:
        return a
    else:
        return (pow(a, b)) % P


P = int(input("Enter the prime number : "))
print("The value of P :", P)

G = int(input("Enter the primitive root for previous prime number : "))
print("The value of G :", G)

a = int(input("Enter the chosen private key A : "))
print("The private key for A :", a)

b = int(input("Enter the chosen private key B :"))
print("The private key for B :", b)

x = power(G, a, P)
print("Public key for A: ", x)

y = power(G, b, P)
print("Public key for B: ", y)

ka = power(y, a, P)
kb = power(x, b, P)
print("Secret key for A is :", ka)
print("Secret Key for B is :", kb)
