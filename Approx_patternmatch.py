
#Program for approximate pattern matching upto k mismatches using dynamic programming.

import numpy
import array   

def readSeq(FASTA): #read the sequence
    for line in FASTA:
        if line.startswith('>'):
            continue
        line = line.strip()
        return line


def posList(pattern, text): #determine the positions in the matrix
    retList = list()
    textList = [x for x in text.strip()]
    for i, char1 in enumerate(pattern):
        textPos = [j for j, char2 in enumerate(textList) if char1==char2]
        for j in textPos:
            retList.append((i+1,j+1))
    return retList

def cost_match(i,j,M):
        return min(M[i,j-1]+1, M[i-1,j-1], M[i-1,j]+1)

def cost_mismatch(i,j,M):
        return min(M[i,j-1]+1, M[i-1,j]+1, M[i-1,j-1]+1)
 


def fill(M,text,compare, pattern):
    n = len(text)
    m = len(pattern)
    positions = posList(pattern,text)
    print positions
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if (i,j) in positions:
                M[i,j] = cost_match(i,j,M)
            else:
                M[i,j] = cost_mismatch(i,j,M)

    return M

                    
def trace(M,pattern,text,k):
    list=[]
    n = len(text)
    m = len(pattern)
    i=m
    j=n
    positions = posList(pattern,text)
    
    tempi=m
    tempj=n
    while(j!=-1):
        if i==m:
           tempj=j
        if i==0:
            if j+1 not in list:
                list.append(j+1)
            i=m
            j=tempj-1
            tempj=j
        if M[i][j]<=k:
            if (i,j) not in positions:
                if M[i-1][j-1]+1<=min(M[i-1][j]+1,M[i][j-1]+1) and M[i-1][j-1]<=k:
                    
                    i=i-1#Moving diagonally
                    j=j-1
    
                elif M[i][j-1]+1<=min(M[i-1][j-1]+1,M[i-1][j]+1) and M[i][j-1]<=k:  
                    
                    j=j-1#Moving horizontally
                elif M[i-1][j]+1<=min(M[i-1][j-1]+1,M[i][j-1]+1) and M[i-1][j]<=k:
                    
                    i=i-1#Moving vertically
            elif (i,j) in positions:
                if M[i-1][j-1]<=min(M[i-1][j]+1,M[i][j-1]+1) and M[i-1][j-1]<=k:
                   
                    j=j-1#Moving diagonally
                    i=i-1
                elif M[i][j]==M[i-1][j-1]:
                    
                    j=j-1#Moving diagonally
                    i=i-1
                elif M[i][j-1]+1<=min(M[i-1][j-1],M[i-1][j]+1) and M[i][j-1]<=k:
                    
                    j=j-1#Moving horizontally
                elif M[i-1][j]<=min(M[i-1][j-1],M[i][j-1]+1) and M[i-1][j]<=k:
                    
                    i=i-1#Moving vertically
        else:
            j=j-1
 
    return list


##Uncomment following lines to read from file.
##T =open("text.fasta","r")
##
##P =open("pattern.fasta","r")
##text=readSeq(T)
##print "String:",text,"\n"
##pattern=readSeq(P)
##print "Pattern",pattern,"\n"

text='ACAGCAG'
print "String:",text,"\n"
pattern='GC'
print "Pattern",pattern,"\n"

n = len(pattern)
m = len(text)

M=numpy.zeros([n+1,m+1],int)


for i in range(0,n+1):
    M[i,0]=i
    for j in range(0,m+1):
        M[0,j]=0


text1=list(text)
pattern1=list(pattern)


M = fill(M,text,min, pattern) #Filling matrix M with scores
print "\n", M


#perform traceback
s= trace(M,pattern,text,1)
print s




