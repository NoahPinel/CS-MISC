begin
	repeat{rw not_iff_imp_false},
	intros f h p,
	apply h,
	apply f,
	exact p,
end
