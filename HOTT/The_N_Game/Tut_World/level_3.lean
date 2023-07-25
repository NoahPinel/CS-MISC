-- Rewrite so we get succ(b) == succ(b) then refl
-- Note it is viable to also call the rw variant rw \l

begin
	rw h,
	refl,
end
