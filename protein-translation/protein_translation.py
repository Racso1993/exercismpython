from typing import List
PMAP = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP",
}
def proteins(strand: str) -> List[str]:
    """ Given a strand of RNA: "AUGUUUUCUUAAAUG" generate Protein names based on
    three character codons:
            RNA: "AUGUUUUCUUAAAUG" =>
            Codons: "AUG", "UUU", "UCU", "UAA", "AUG" =>
            Protein: "Methionine", "Phenylalanine", "Serine"
    """
    # seperate them into 3 char codon chunks
    codon_chunks = [strand[i:i + 3] for i in range(0, len(strand), 3)]
    protein_names = []  # Holds final protein name results
    # parse each item and compare to PMAPS until we hit a stop codon
    for codon in codon_chunks:
        if PMAP.get(codon) is not "STOP":
            protein_names.append(PMAP.get(codon))
            continue
        else:
            break
    return protein_names
