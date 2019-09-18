# HARSHIT RAI
# 2017152

from math import log
import numpy as np

# Function for finding log-det distance 
def log_det(M):
    
    a=np.linalg.det(M)
    g0=(M[0][0]+M[1][0]+M[2][0]+M[3][0])*(M[0][1]+M[1][1]+M[2][1]+M[3][1])*(M[0][2]+M[1][2]+M[2][2]+M[3][2])*(M[0][3]+M[1][3]+M[2][3]+M[3][3])
    g1=sum(M[0])*sum(M[1])*sum(M[2])*sum(M[3])
    b=g0*g1
    d=-(1/4)*(log(a)-(1/2)*log(b))
    
    return(d)

# Function for finding Jukes-Cantor distance 
def jcd(p):
    
    d=-(3/4)*log(1-(4/3)*p)
    return(d)

# Function for finding Kimura 2-parameter distance 
def k2pd(ts,tv):      
    
    p1=ts/len(S0)
    p2=tv/len(S0)
    
    d=(-0.5)*log(1-2*p1-p2)-(1/4)*log(1-2*p2)
    
    return(d)   

S0="CGGCCTGAAGCGACGTCGTATCATATCAATCGCATGTCATCGCCGTCTACGCCCCGGAGACTAAACCCTGCCGCATGATAATGTGGTCTACTGAGTTCTTCATGGGGCAGGGGATCATGAATCGTGCAAGACCCAAGCCCCTACCAAAGAGACCACGAGGTCATTAGTCTTCCTAGGCGACTAGTTCTGTCGCGCTCTCACCATTTCTTCTCATGGGGAACTCAGAACTGGATGAATGTCCCTTAGACCCTGTTTTCCTCGCGTGAAAAAGTACCTTTTAGAGCATTCAAATATGTCGACCGAAGAACCTGTAGTTAAATCCGTCGCATTAACTCTTAGAGGGCCGGAGCTAAGACCAAGTCTATCACGCGCGCTCAAACATGAGGGAGATTGGTCCATTTGTGGGAGATTAGCCAAGCATCATGGAACTACCTCTTTCCATACAATTTCGGCCTTGCCATATTCCATTTAATGAAAGCTACGCCTCGAGCCGTTAAGCCCGTCAATAGAACTGGTTACCTAAGGCCAGTACCAACGGAATGGCTGGAGGTCGCGCCACGAATATGGTGCCTTTTTCCTGTAGCTCGTGTCGGCCGAAGA"
S1="AGGCGTCAAGTGTCGGCGGGGCATATTAATGGCGTGTTGCTAAGCTGGACAGTCAAAGTGCCCAACTCAGCTGCGCCGCAGCGTATTCCGACGGCTTCTCCATGAGGGAAAAGATCGCAAAACGGGTAAGTTTTAAATTTGTAATAATAAGACGATTTGCCAACTGGTCCCGAAAGGGGAATGAGTTTGCCACAGACCCCCTGTCTGTTCGTCCCAAAAATCAGGGTCCAGATGAGTTGTACCTGAGGGTCCATTTCTTCTTTTAGCTGATTGATTCCCGGATGACCCCTACGTGTCGCTCAGAAAGACAGTACGTCGACGCGTCACCTTAACATAGGGGTTGCCCAGGCCCGGCCCTAACCGAATTGGCATCCACAAACATAGGAAAGATTGATCCAATAAAAAGAAATCAGCCGCGTACCATTATGTTAGCTATATCTGGGCATTGGCGTCCGTGCCGTCCTTTGACTAATAACGGTTACTCCCCAAGCAGTTATACCGGTGGGCAAAACTGGTCGATGGACTCGGCGGTGAATAGTCCGATCGGCGCACACGCCATGAGCAGGATGCATTCTTCCTGTAACCTGTGACAACTGCGGG"

# Counting the frequency of each base in S0
a0=S0.count('A')
g0=S0.count('G')
c0=S0.count('C')
t0=S0.count('T')

# Counting the frequency of each base in S1
a1=S1.count('A')
g1=S1.count('G')
c1=S1.count('C')
t1=S1.count('T')

aa,ag,ac,at=0,0,0,0
ga,gg,gc,gt=0,0,0,0
ca,cg,cc,ct=0,0,0,0
ta,tg,tc,tt=0,0,0,0
ts,tv,p=0,0,0

# Calculating the values of the frequency matrix
for i in range(len(S0)):
    
    if(S0[i]=='A'):
        if(S1[i]=='A'):
            aa+=1
        elif(S1[i]=='G'):
            ag+=1
            ts+=1
        elif(S1[i]=='C'):
            ac+=1
            tv+=1
        elif(S1[i]=='T'):
            at+=1
            tv+=1

    elif(S0[i]=='G'):
        if(S1[i]=='A'):
            ga+=1
            ts+=1
        elif(S1[i]=='G'):
            gg+=1
        elif(S1[i]=='C'):
            gc+=1
            tv+=1
        elif(S1[i]=='T'):
            gt+=1
            tv+=1

    elif(S0[i]=='C'):
        if(S1[i]=='A'):
            ca+=1
            tv+=1
        elif(S1[i]=='G'):
            cg+=1
            tv+=1
        elif(S1[i]=='C'):
            cc+=1
        elif(S1[i]=='T'):
            ct+=1
            ts+=1

    elif(S0[i]=='T'):
        if(S1[i]=='A'):
            ta+=1
            tv+=1
        elif(S1[i]=='G'):
            tg+=1
            tv+=1
        elif(S1[i]=='C'):
            tc+=1
            ts+=1
        elif(S1[i]=='T'):
            tt+=1

# Total changes = transitions + transversions
p=(ts+tv)/len(S0)

# Frequency Matrix
M=[[aa,ga,ca,ta],
     [ag,gg,cg,tg],
     [ac,gc,cc,tc],
     [at,gt,ct,tt]]

# Markov Matrix
M_prob=[[aa/a0,ga/g0,ca/c0,ta/t0],
              [ag/a0,gg/g0,cg/c0,tg/t0],
              [ac/a0,gc/g0,cc/c0,tc/t0],
              [at/a0,gt/g0,ct/c0,tt/t0]]

# Initial vector
p0=[[a0/len(S0)],[g0/len(S0)],[c0/len(S0)],[t0/len(S0)]]

print("Answer: 1_A")
print("Base A appearing in same site:",aa)
print("Base G appearing in same site:",gg)
print("Base C appearing in same site:",cc)
print("Base T appearing in same site:",tt)
print()
print("Matrix:")
print(M)
print()
print("Answer: 1_B")
print("Fraction of Base A in S0:",a0/len(S0))
print("Fraction of Base G in S0:",g0/len(S0))
print("Fraction of Base C in S0:",c0/len(S0))
print("Fraction of Base T in S0:",t0/len(S0))
print()
print("Answer: 1_C")
print("Fraction of Base A in S1:",a1/len(S0))
print("Fraction of Base G in S1:",g1/len(S0))
print("Fraction of Base C in S1:",c1/len(S0))
print("Fraction of Base T in S1:",t1/len(S0))
print()
print("Answer: 1_D")
print("Conditional Probability:")
print(M_prob)
print()

print("Answer 2:")
print("Jukes-Cantor Distance:",round(jcd(p),10))
print("Kimura 2-parameter Distance:",round(k2pd(ts,tv),10))
print("Paralinear Distance:",round(log_det(M),10))
print()
print("Kimura 2-parameter is likely to be a better estimate of the number of substitutions per site that actually occurred because 'BETA' comes out to be 0.3 ,'GAMMA' and 'DELTA' comes out to be 0.1 which are same. So this case perfectly fits in Kimura 2-parameter")
print()

M_prob=np.array(M_prob)
p0=np.array(p0)
print("Answer: 3_A")
print("Equilibrium Vector:")
# P(t) = (M^t)*P(0)
okay=np.linalg.matrix_power(M_prob,32)
print(np.matmul(okay,p0))
print()
evl,evc=np.linalg.eig(M_prob)
print("Answer: 3_B")
print("Eigen vectors:")
print(evc)
print()
print("Eigen Values:")
print(evl)
print()
print("The eigenvector corresponding to eigenvalue '1' is same as the equilibrium vector.It's just that the eigenvector is multiplied by a factor of '0.54752229' to get the Equilibrium Vector")
print()
print("Answer: 3_C")
print("A Markov matrix with all positive entries will always have 1 as its dominant eigenvalue with corresponding eigenvector having all non-negative entries also the sum of each column is equal to '1'")

