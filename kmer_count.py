string_inp ='ACGTTGCATGTCGCATGATGCATGAGAGCT'
k = 4

def kmer_func(string,k):
    sub_string = [string[i:i+k] for i in range(len(string)) if i <= len(string)-k]
    return high_freq(sub_string)

def high_freq(list):
    unique_list = set(list)
    max_element = max(set(list), key=list.count)
    return [x for x in unique_list if list.count(str(x)) == list.count(max_element)]


answer = kmer_func(string_inp, k)
print "The k-mer with maximum occurences is : ",answer,"\n"
