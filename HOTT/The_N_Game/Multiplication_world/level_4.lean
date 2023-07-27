-- lemma mul_add (t a b : mynat) : t * (a + b) = t * a + t * b :=
begin
	induction b with k h,
	refl, -- BC by Def

	rw add_succ, -- ⊢ t * succ (a + k) = t * a + t * succ k
	rw mul_succ, -- ⊢ t * (a + k) + t = t * a + t * succ k
	-- invoke IH
	rw h,
	rw add_assoc,
	refl,
end
