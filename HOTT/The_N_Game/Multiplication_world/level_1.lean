-- proving  0 x m = 0
begin
	induction m with k h,
	refl, -- By def

	rw mul_succ, -- This gives ⊢ 0 * k + 0 = 0
	rw h, -- Invoke IH // simple replace, we are left to show 0+0=0
	refl, -- By def
end
