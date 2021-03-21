"""
Set the grey level limits a, b and the grey level range R. Load the reference image A

For each image in the database s = 1 to m
    Load database image B_s
    Zero co-occurrence matrix C of size R x R
    for row i = 1 to M
        for column j = 1 to N
            K = I_A (i,j) + 1,      
            L = I_B (i,j) + 1
            increment C (K,L)
    Compute co-occurrence probability P  =  C / (M*N)    
    Convert P to 1-D and compute H_s (A , B_s)

Compute similarity measure ρ(s) for each image Bsin the database 
"""

a = 0 
b = 31 
R = 32

M = 50
N = 50

eps = 0.0000000000000001
