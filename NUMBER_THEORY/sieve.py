import tkinter as tk
import time
import math

def Green(label):
    label.config(bg='green')
    root.update()
    time.sleep(0.01)

def Red(label):
    label.config(bg='red')
    root.update()
    time.sleep(0.01)

def makeGrid(n):
    root = tk.Tk()
    numbers = []
    labels = []

    size = math.isqrt(n) + 1

    for i in range(size):
        label_row = []
        for j in range(size):
            number = i * size + j + 1
            if number <= n:
                label = tk.Label(root, text=str(number), padx=5, pady=5, width=4)
                label.grid(row=i, column=j)
                label_row.append(label)
        labels.append(label_row)

    return root, labels

def Sieve(n, labels):
    Search_Space = [True for _ in range(n+1)]
    primes = []
    p = 2
    
    # Default 1 to red
    Red(labels[0][0])
    
    # Start Search
    while pow(p, 2) <= n:
        if Search_Space[p] == True:
            for i in range(pow(p, 2), n + 1, p):
                Search_Space[i] = False
                row, col = divmod(i - 1, len(labels))
                Red(labels[row][col])
        p += 1
    
    # All index's that are T will be prime.
    for p in range(2, n + 1):
        if Search_Space[p]:
            row, col = divmod(p - 1, len(labels))
            Green(labels[row][col])
            primes.append(p)
    return primes
    
n = 300
root, labels = makeGrid(n)
root.update()
primes = Sieve(n, labels)
root.mainloop()
count = len(primes)
print('There are {} primes from 2,...,{}'.format(count, n))
print(primes)
