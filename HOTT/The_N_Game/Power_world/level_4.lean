lemma one_pow (m : mynat) : (1 : mynat) ^ m = 1 :=

begin
	induction m with k h,
	refl, -- BC

	rw pow_succ, -- ⊢ 1 ^ k * 1 = 1
	rw h, -- ⊢ 1 * 1 = 1
	refl,
end
