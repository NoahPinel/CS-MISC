-- We want to make a element of p from U
--
--	p \in P ---- h ----> Q
--			     |
--			     |
--			     j			
--			     |	
--			     |	
--		             T ---- l ---- U

begin
	--exact l(j(h(p))), -- Simple one liner
	have q := h(p),
	have t : T := j(q),
	have u : U := l(t),
	exact u,
end
