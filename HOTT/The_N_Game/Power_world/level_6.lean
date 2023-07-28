lemma mul_pow (a b n : mynat) : (a * b) ^ n = a ^ n * b ^ n :=

begin
	induction n with k h,
	refl, -- Triv True

	rw pow_succ, -- ⊢ (a * b) ^ k * (a * b) = a ^ succ k * b ^ succ k
	rw pow_succ, -- ⊢ (a * b) ^ k * (a * b) = a ^ k * a * b ^ succ k
	rw pow_succ, -- ⊢ (a * b) ^ k * (a * b) = a ^ k * a * (b ^ k * b)
	rw h, -- ⊢ a ^ k * b ^ k * (a * b) = a ^ k * a * (b ^ k * b)
	simp,
end
