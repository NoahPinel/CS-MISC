begin
	intros f h p,
	apply f, -- we split our goal into ⊢ Q and ⊢ P
	exact p, -- proves f (P → Q → R)

	apply h, -- P → Q
	exact p,
end
