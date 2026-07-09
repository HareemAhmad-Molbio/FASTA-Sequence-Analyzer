from collections import Counter
from Bio.Seq import Seq



def gc_content(seq):
    seq = seq.upper()
    if not seq:
        return 0.0

    gc = seq.count("G") + seq.count("C")
    atgc = sum(seq.count(b) for b in "ACGT")

    if atgc == 0:
        return 0.0

    return (gc / atgc) * 100


def nucleotide_counts(records):
    counts = Counter()

    for record in records:
        counts.update(str(record.seq).upper())

    return {base: counts.get(base, 0) for base in ["A", "T", "G", "C", "N"]}


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    return str(Seq(seq).reverse_complement())


def transcribe_dna(seq):
    """Convert DNA to RNA."""
    return str(Seq(seq).transcribe())


def translate_protein(seq):
    """Translate DNA sequence into protein."""
    dna = Seq(seq)

    # Ensure the sequence length is divisible by 3
    usable = len(dna) - (len(dna) % 3)
    dna = dna[:usable]

    return str(dna.translate())

def find_motif(seq, motif):
    """
    Find all occurrences of a DNA motif.
    Returns a list of starting positions (1-based indexing).
    """
    seq = seq.upper()
    motif = motif.upper()

    positions = []

    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i + len(motif)] == motif:
            positions.append(i + 1)

    return positions