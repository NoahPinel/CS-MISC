lemma zero_pow_succ (m : mynat) : (0 : mynat) ^ (succ m) = 0 :=

begin
	rw pow_succ, -- ⊢ 0 ^ m * 0 = 0
	rw mul_zero, -- ⊢ 0 = 0
	refl,
end
