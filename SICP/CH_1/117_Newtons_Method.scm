#lang scheme
#|
This is neat because we didnt need to
rely on constructs for looping to achieve
our iteration, it was simply done with procedure
calls.
|#

(define (square x)
  (* x x))

(define (avg x y)
  (/ (+ x y) 2)) 

; Threshold for good enough
(define (good? guess x)
  (< (abs (- (square guess) x)) 0.001))

; If our guess was shite, avg the guess with the quotient
(define (improve guess x)
  (avg guess (/ x guess)))

(define (sqrt-iter guess x)
  (if (good? guess x)
      guess
      (sqrt-iter (improve guess x)
                 x)))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(sqrt 9)
(sqrt 49)
(sqr (sqrt 10))
(sqr (sqrt 9999))
(sqrt 0.25)
