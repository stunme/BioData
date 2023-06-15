##  Mendel's First Law

def mendelLaw(k, m, n):
    all = k + m + n
    probility = 0 
    # aa aa
    probility += n/all*(n-1)/(all-1)
    # aa Aa
    probility += n/all*m/(all-1)/2
    # Aa aa
    probility += m/all*n/(all-1)/2
    # Aa Aa
    probility += m/all*(m-1)/(all-1)/4
    return probility

k, m, n = 21,20,19

print(1-mendelLaw(k,m,n))

