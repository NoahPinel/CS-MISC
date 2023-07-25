-- Use rw (re-write) tactic
lemma example2 (x y : mynat) (h : y = x + 7) : 2 * y = 2 * (x + 7) :=

begin
	-- Rewrite h so we can reduce to rf
	rw h,
	rf,
end
