-- A * B == B * A
-- showing comm. we now know that \mathbb{N} is a commutative semiring.

lemma mul_comm (a b : mynat) : a * b = b * a :=

begin
	induction a with k h,
	rw zero_mul,
	refl, -- BC

	rw succ_mul,
	rw h,
	rw mul_succ,
	refl,
end
