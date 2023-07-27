-- contravariance of Hom(⋅,F) functor.

begin
	intros f h p,
	-- f : P → Q
	-- h : Q → F
	apply h, -- get ⊢ Q
	apply f, -- get ⊢ P
	exact p,
end
