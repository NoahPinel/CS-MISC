lemma pow_one (a : mynat) : a ^ (1 : mynat) = a :=

begin
	rw one_eq_succ_zero, -- ⊢ a ^ succ 0 = a
	rw pow_succ, -- ⊢ a ^ 0 * a = a
	rw pow_zero, -- ⊢ 1 * a = a
	rw one_mul, -- ⊢ a = a
	refl,
end
