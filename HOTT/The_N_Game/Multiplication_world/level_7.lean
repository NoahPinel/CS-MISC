-- With this proof we have shown \mathbb{N} to be a semiring

lemma add_mul (a b t : mynat) : (a + b) * t = a * t + b * t :=
begin
	induction t with k h,
	refl,

	rw mul_succ,
	rw mul_succ,
	rw mul_succ,
	rw h,
	simp,
end
