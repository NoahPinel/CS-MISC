HOM(HOM(P,Q),HOM(HOM(Q,∅),HOM(P,∅)))

begin
	intros f h p,
	apply h,
	apply f,
	exact p,
end
