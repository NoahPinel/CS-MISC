-- Show transitivity of \Rightarrow
begin
	intros hpq hqr p,
	apply hqr,
	apply hpq,
	exact p,
end
