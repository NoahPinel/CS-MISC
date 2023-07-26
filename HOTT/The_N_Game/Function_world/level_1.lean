-- P Q : Type,
-- p : P,
-- h : P → Q
-- ⊢ Q

-- We call the new tactic 'exact' to solve this
begin
	exact h(p),
end
