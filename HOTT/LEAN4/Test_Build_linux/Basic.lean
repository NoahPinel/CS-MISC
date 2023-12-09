import Mathlib

theorem foo : 1 + 1 = 2 := by
  rfl

/- Example does not the term to our env
   Hence, no name is needed for them -/
example : 1 + 1 = 2 := by
  rfl

example : 2 + 2 = 4 := by
  exact rfl

example (p q : ℕ) (h1 : p = q) : p = q := by
  exact h1

example : ℕ → ℕ := by
  intro n
  exact n + 42

example (P Q R : Prop) (h : P -> Q -> R) : R := by
  apply h -- It's like invoking a lemma
  sorry

example (n : ℕ) (h : n = 124) : n = 124 := by
  assumption

example (n : ℕ) (h : n = 0) : n + 1 = 1 := by
  rw [h]

example (n : ℕ) : n + 0 = n := by
  simp

example (x y : ℕ) (h : y = x + 7) : 2 * y = 2 * (x + 7) := by
  rw [h]

example (n : ℕ) : (1 : ℝ) ≤ 1.3^n := by
  have hyp : (1 : ℝ) ≤ 1.3 := by
    norm_num
  exact one_le_pow_of_one_le hyp n
