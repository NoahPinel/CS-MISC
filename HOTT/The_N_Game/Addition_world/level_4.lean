begin
	induction a with n hn,
	-- Base Case
	rw zero_add,
	refl, -- True by Def

	-- HT
	rw add_succ, -- ⊢ succ n + b = succ (b + n)
	rw succ_add, -- ⊢ succ (n + b) = succ (b + n)
	rw hn, -- ⊢ succ (hn) = succ (b + n) = succ (b + n)
	refl,
end
