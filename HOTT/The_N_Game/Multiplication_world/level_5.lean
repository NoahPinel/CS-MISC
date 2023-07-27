-- With this we have shown \mathbb{N} to be a monoid

lemma mul_assoc (a b c : mynat) : (a * b) * c = a * (b * c) :=
begin
	induction c with k h,
	refl, -- BC

	rw mul_succ,
	rw h,
	rw mul_succ,
	rw mul_add,
	refl,
end
