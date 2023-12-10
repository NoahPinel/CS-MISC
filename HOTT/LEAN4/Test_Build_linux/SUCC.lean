 theorem REFLEX : 42  = 42 := by
  rfl

theorem triv (a b c : Nat):
  a * b + c = a * b + c := by
  rfl

-- m + 0 = m
theorem Succ_Ax_1 (m : Nat) :
  m + 0 = m := by
  rfl

-- m + succ(n) = succ(m + n)
theorem Succ_Ax_2 (m n : Nat) :
  m + Nat.succ n = Nat.succ (m + n) := by
  rfl

theorem one_eq_succ_zero :
  1 = Nat.succ 0 := by
  rfl

theorem two_eq_succ_zero :
  2 = Nat.succ 1 := by
  rfl

-- 2 = succ(succ(0)) → 2 = succ(1)
theorem two_eq :
  2 = Nat.succ (Nat.succ 0) := by
  rw [two_eq_succ_zero]

