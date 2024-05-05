#lang scheme
(define (sqr x)
  (* x x))

(define (max a b)
  (cond ((>= a b) a)
        ((>= b a) b)))

(define (3max a b c)
  (max a (max b c)))

(define (min a b)
  (cond ((<= a b) a)
        ((<= b a) b)))

(define (middle a b c)
  (cond ((and (<= b (max a c)) (>= b (min a c))) b)
        ((and (<= c (max a b)) (>= c (min a b))) c)
        (else a)))

(define (sum3sqr a b c)
  (+ (sqr (3max a b c)) (sqr (middle a b c))))

;; Tests
(sum3sqr 1 2 3); 13
(sum3sqr 1 1 3); 10
(sum3sqr -3 2 0); 4
(sum3sqr 1 1 1); 2
(sum3sqr 1 2 2); 8
(sum3sqr 1 1 2); 5
(sum3sqr 1 4 3); 25