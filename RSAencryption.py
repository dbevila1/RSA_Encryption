print ("Enter two prime numbers. (Ex: 2, 3, 5, 7, 11, 13, etc...) ")
p = int(input("p: "))
q = int(input("q: "))

n = (p * q)
phi = (p-1) * (q-1)

print ("\nn = ", n)
print ("phi = ", phi)
e = int(input("\nChoose a number e, such that 1 < e < phi. e: "))

d = 2

while( d < phi):
    tester = e * d
    d = d + 1
    if tester%phi == 1:
        break

d = d-1
print ("\nd = ", d)
print ("\nSecret Values (p, q, phi, d): ", p, q, phi, d)

message = int(input("Enter a number to encrypt: "))
encMessage = pow(message, e, n)
print("Encrypted Message: ", encMessage)
decMessage = pow(encMessage, d, n)
print("Decrypted Message: ", decMessage)