# Answer to rosalind.info/problems/iprb
# Probability - Mendelian Inheritance and Heredity


def dom_pheno(k, m, n):  # Function to calculate probability of dominant phenotype from k homo dom, m hetero, n homo rec
    k, m, n = float(k), float(m), float(n)
    total = k + m + n
    total1 = total - 1
    p = k / total + (m / total) * (k / total1 + (m-1) / total1 * 0.75 + n / total1 * 0.5) + (n / total) * (k / total1 + m / total1 * 0.5)
    return p


print(dom_pheno(30, 15, 30))


