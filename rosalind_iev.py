# Calculating expected no. of offspring which has dominant phenotype
# Answer to rosalind.info/problems/iev

# Expected Value = Probability * Number of Offspring / Couple * Number of Couple
def expected_dom():
    input_ = input("Input: ").split()
    for i in range(len(input_)):
        input_[i] = int(input_[i])
    num_offspring = 2
    e = 0.
    table = {'AA-AA': 1,
             'AA-Aa': 1,
             'AA-aa': 1,
             'Aa-Aa': 0.75,
             'Aa-aa': 0.5,
             'aa-aa': 0}
    prob_list = list(table.values())

    for i in range(len(input_)):
        e += prob_list[i] * input_[i] * num_offspring

    return e

print(expected_dom())