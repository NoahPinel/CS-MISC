begin 
	exact zero_add m, -- Cheeky sol --> m * 1 == m + 0 =)

	-- Long way
	rw one_eq_succ_zero,
	rw mul_succ,
	rw mul_zero,
	rw zero_add,
	refl,
end
