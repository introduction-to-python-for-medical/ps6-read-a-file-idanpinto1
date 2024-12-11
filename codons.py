def create_codon_dict(file_path):
    file = open(file_path, 'r')
    rows = file.readlines()
    file.close()
    codons_dict = {}
    for each_row in rows:
      row = each_row.strip().split('\t')
      codon = row[0]
      amino_acid = row[2]
      codons_dict[codon] = amino_acid
    return codons_dict


