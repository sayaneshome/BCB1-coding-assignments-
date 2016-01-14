
##Program for RNA 2-D folding using Nussinov algorithm using dynamic programming.
import numpy
import array
class Structure :
    def __init__(self): 
        self.paired =[]
        self.unpaired =[]
    def merge(self, s):
        for i in s.paired :
            self.paired.append(i)
        for i in s.unpaired :
            self.unpaired.append(i)
    def __str__(self):
        return "paired\n"+str(self.paired) +"\n unpaired \n"+str(self.unpaired)+"\n"
def l(ch) :

    if (ch=='A') :
        return 0
    elif (ch=='C'):
        return 1
    elif (ch=='U') :
        return 2
    elif (ch =='G') :
        return 3
    else :
        print "error"
    
def cost(i,j,M,w,seq,compare): #Defining the cost functions or can say recurrence formula
    j_unpaired = M[i,j-1]
    i_unpaired = M[i+1,j]
    paired = M[i+1,j-1] + w[l(seq[i]), l(seq[j])]
    
    return compare(j_unpaired,i_unpaired,paired)  #return comparison of the three relations

def fill(M, w, seq, compare): #function defining how to fill up the values 
    n = len(seq)
    for k in range(5,n):
        for i in range(0,n-k):
            j = k+i
            c = cost(i,j,M,w,seq,compare)
            M[i,j] = c

def trace(M, w, seq, compare, horizontal_arrow, vertical_arrow) :
    i = horizontal_arrow
    j = vertical_arrow
    struct = Structure()
    while (j != i-1):
        if M[i,j] == M[i,j-1] :
            struct.unpaired.append(j)
            j -= 1
            
        elif M[i,j] == M[i+1,j] :
            
            struct.unpaired.append(i)
            
            i += 1
        elif M[i,j] == M[i+1,j-1] + w[l(seq[i]), l(seq[j])] :
            
            struct.paired.append((i,j))
            i += 1
            j -= 1
        else:
            print "error"

    return struct

def real_string(struct) : 
    trace=dict()
    for element in struct.unpaired:
        trace[element] = '.'

    for element in struct.paired:
        trace[element[0]] = '('
        trace[element[1]] = ')'

    return list(trace.values())
    
f =open("example.fasta","r")
def readSeq(FASTA):
    for line in FASTA:
        if line.startswith('>'):
            continue
        line = line.strip()
        return line

    
seq=readSeq(f)

n = len(seq)

w = numpy.zeros([4,4],int)
w.fill(0)
w[l('A'), l('U')] = 1
w[l('U'), l('A')] = 1 
w[l('G'), l('C')] = 1
w[l('C'), l('G')] = 1
M = numpy.zeros([n,n],int) #initialisation of matrix
fill(M, w, seq, max) #Filling matrix M with scores
print M

s = trace(M, w, seq, max, 0, n-1)
print str(s)
print seq
result=real_string(s)
print "".join(result)
