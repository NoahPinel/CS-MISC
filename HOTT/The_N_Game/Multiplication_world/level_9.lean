lemma mul_left_comm (a b c : mynat) : a * (b * c) = b * (a * c) :=
begin
	induction c with k h,
	refl, -- BC

	rw mul_succ, -- ⊢ a * (b * k + b) = b * (a * succ k)
	rw mul_succ, -- ⊢ a * (b * k + b) = b * (a * k + a)
	rw mul_add, -- ⊢ a * (b * k) + a * b = b * (a * k + a)
	rw mul_add, -- ⊢ a * (b * k) + a * b = b * (a * k) + b * a
	rw h, -- Invoke IH // ⊢ b * (a * k) + a * b = b * (a * k) + b * a
	rw mul_comm b a, -- get a * b on both sides 
	refl,
end
