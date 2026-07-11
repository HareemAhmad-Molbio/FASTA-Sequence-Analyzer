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


def find_orfs_in_frame(seq, frame=0, min_length=0):
    """
    Find all ORFs in one reading frame.

    Parameters
    ----------
    seq : str
        DNA sequence
    frame : int
        Reading frame (0,1,2)
    min_length : int
        Minimum ORF length in bp

    Returns
    -------
    list
        List of ORFs
    """

    seq = seq.upper()

    stop_codons = {"TAA", "TAG", "TGA"}

    orfs = []

    inside_orf = False
    start = None
    current_codons = []

    for i in range(frame, len(seq) - 2, 3):

        codon = seq[i:i+3]

        if not inside_orf:

            if codon == "ATG":
                inside_orf = True
                start = i
                current_codons = [codon]

            continue

        current_codons.append(codon)

        if codon not in stop_codons:
            continue

        dna = "".join(current_codons)

        if len(dna) >= min_length:

            protein = translate_protein(dna)

            orfs.append({
                "frame": frame + 1,
                "start": start + 1,
                "end": i + 3,
                "length": len(dna),
                "protein": protein,
                "dna": dna,
            })
            
            inside_orf = False
            start = None
            current_codons = []

            return orfs