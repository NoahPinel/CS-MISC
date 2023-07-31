lemma add_right_eq_zero {a b : mynat} : a + b = 0 → a = 0 :=

begin
	intro h,
	cases a,
	refl,

	exfalso,
	rw succ_add at h,
	apply succ_ne_zero,
	exact h,
end
