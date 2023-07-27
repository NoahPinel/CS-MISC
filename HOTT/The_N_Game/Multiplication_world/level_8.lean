-- A * B == B * A
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
