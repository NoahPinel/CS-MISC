begin
	-- Group by Assoc, then simply invoke Com.
	rw add_assoc a c b, -- ⊢ a + b + c = a + (c + b)

	rw add_assoc a b c, -- ⊢ a + (b + c) = a + (c + b)

	rw ← add_comm b c, -- ⊢ a + (b + c) = a + (b + c)
	refl,
end
