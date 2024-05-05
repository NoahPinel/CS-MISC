#lang scheme

(+ (* 3
      (+ (* 2 4) 
         (+ 3 5)))
   (+ (- 10 7)
      6))

;Simple abstraction
(define size 2)

size

(* 100 size)

(define pi 3.14159)

(define rad 10)

; pi * r^2 (Area of a circle)
(* pi (* rad rad))

; Circumference
(define circ (* 2 pi rad))

circ

; Compound procedure
(define (sqr x) (* x x))

(sqr 10)
(sqr 21)
(sqr (+ 2 2))

; 16^2 = 2^8 = 2^2^2^2
(sqr (sqr (sqr 2)))

; Sum of squares: x^2 + y^2
(define (sum-of-sqr x y)
  (+ (sqr x) (sqr y)))

(sum-of-sqr 5 12)

(define (f a)
  (sum-of-sqr (+ a 1) (* a 2)))

(f 5)

; Conditional Expressions and Predicates
(define (abs x)
  (cond ((> x 0) x)
        ((= x 0) 0)
        ((< x 0) (- x))))

(abs -10)

; This is cleaner
(define (abs1 x)
  (if (< x 0)
      (- x)
      x))
(abs1 -12)

