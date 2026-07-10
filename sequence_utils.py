from collections import Counter
from Bio.Seq import Seq

RESTRICTION_ENZYMES = {
    "EcoRI": "GAATTC",
    "BamHI": "GGATCC",
    "HindIII": "AAGCTT",
    "NotI": "GCGGCCGC",
    "XhoI": "CTCGAG",
}


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

def find_restriction_sites(seq, enzyme):
    """
    Find restriction enzyme recognition sites.

    Returns:
        recognition_site, positions
    """

    if enzyme not in RESTRICTION_ENZYMES:
        return None, []

    recognition_site = RESTRICTION_ENZYMES[enzyme]
    positions = find_motif(seq, recognition_site)

    return recognition_site, positions

def find_longest_orf(seq):
    """
    Find the longest ORF in the forward strand.
    """

    seq = seq.upper()

    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}

    longest = ("", 0, 0)

    i = 0

    while i < len(seq) - 2:

        codon = seq[i:i+3]

        if codon == start_codon:

            j = i

            while j < len(seq) - 2:

                current = seq[j:j+3]

                if current in stop_codons:

                    orf = seq[i:j+3]

                    if len(orf) > len(longest[0]):
                        longest = (
                            orf,
                            i + 1,
                            j + 3,
                        )

                    break

                j += 3

        i += 1

    return longest

def find_all_orfs(seq):
    """
    Find all ORFs in the forward strand (Frame +1).

    Returns:
        List of dictionaries containing ORF information.
    """

    seq = seq.upper()

    start_codon = "ATG"
    stop_codons = {"TAA", "TAG", "TGA"}

    orfs = []

    i = 0

    while i < len(seq) - 2:

        if seq[i:i+3] == start_codon:

            j = i + 3

            while j < len(seq) - 2:

                codon = seq[j:j+3]

                if codon in stop_codons:

                    dna = seq[i:j+3]

                    protein = translate_protein(dna)

                    orfs.append({
                        "start": i + 1,
                        "end": j + 3,
                        "length": len(dna),
                        "protein": protein,
                    })

                    break

                j += 3

        i += 1

    return orfs