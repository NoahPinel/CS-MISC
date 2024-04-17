# TEMPLATE FOR VERIFY R[X]/<S(X)> IS INDEED A VALID FF.
p = 3 
K.<x> = GF(p)[]
f = x^2+1 # make sure this is actually irreducible or the code will brick
F = GF(p^f.degree(), 'x', modulus=f)

print(F.order())

