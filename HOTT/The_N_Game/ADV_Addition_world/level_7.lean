theorem add_right_cancel_iff (t a b : mynat) :  a + t = b + t ↔ a = b :=

begin
	split,
	exact add_right_cancel _ _ _,
	-- cc, Stop here

	intro hyp,
	rw hyp,
	refl,
end
