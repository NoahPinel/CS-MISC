-- split tactic, break a goal into two seperate ones
-- i.e. ⊢ P ∧ Q becomes ⊢ P and ⊢ Q

begin
	split,
	exact p,
	exact q,
end
