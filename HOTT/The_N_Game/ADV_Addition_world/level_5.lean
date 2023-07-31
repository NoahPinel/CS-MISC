begin
	intros h0,
	induction t with k h,
	rw add_zero at h0,
	exact h0,

	repeat{rw add_succ at h0},
	--have h2 := succ_inj(h0),
	--have h3 := h(h2),
	--exact h3,
	cc,
end
