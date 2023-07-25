-- Prove (a + b) + c = a + (b + c)
begin
	-- idk if its bad to have with c
	-- I just did it so I can have abc
	-- present in the helper window
	
	-- Prove base case
	-- ⊢ a + b + 0 = a + (b + 0)
	induction c with c hc,
	
	-- Just pull out 0's
	rw add_zero,
	rw add_zero,
	
	-- Easily obtain ⊢ a + b = a + b
	refl,

	-- ⊢ a + b + succ c = a + (b + succ c)
	-- Cycle succ() we get
	rw add_succ,
	rw add_succ,
	rw add_succ,
	
	-- ⊢ succ (a + b + c) = succ (a + (b + c))
	rw hc,
	
	-- Finally, 
	-- ⊢ succ (a + (b + c)) = succ (a + (b + c))
	refl,
end
