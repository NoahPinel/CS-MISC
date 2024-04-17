# Check irr. of polynomial in the ring of polynomials in x 
# with integer coefficients

R = PolynomialRing(GF(2), 'x')
x = R.gen()
f = x^4 + x^2 + x + 1

is_irreducible = f.is_irreducible()

if f.is_irreducible():
    print("The polynomial is irreducible.")

else:
    print("The polynomial is reducible.")
    factors = f.factor()
    print("Factors:")
    for factor, multiplicity in factors:
        print(factor, "^", multiplicity)
