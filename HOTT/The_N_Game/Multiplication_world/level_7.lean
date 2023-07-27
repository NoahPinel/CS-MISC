begin
	induction t with k h,
	refl,

	rw mul_succ,
	rw mul_succ,
	rw mul_succ,
	rw h,
	simp,
end
