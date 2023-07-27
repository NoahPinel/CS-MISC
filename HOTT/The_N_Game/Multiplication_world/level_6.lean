lemma succ_mul (a b : mynat) : succ a * b = a * b + b :=
begin
	induction b with k h,
	refl, --Triv

	rw mul_succ,
	rw mul_succ,
	rw add_succ,
	rw add_succ,
	rw h,
	simp, -- :)
end
