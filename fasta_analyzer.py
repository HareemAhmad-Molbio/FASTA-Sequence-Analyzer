#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path
from collections import Counter

try:
    from Bio import SeqIO
except ImportError:
    print("Biopython is required. Install with: pip install -r requirements.txt")
    sys.exit(1)


VALID_BASES = set("ACGTN")


def read_fasta(path):
    return list(SeqIO.parse(path, "fasta"))


def validate_fasta(records):
    errors = []
    if not records:
        errors.append("No FASTA records found.")
        return errors

    for i, record in enumerate(records, start=1):
        seq = str(record.seq).upper()
        invalid = sorted(set(seq) - VALID_BASES)
        if invalid:
            errors.append(
                f"Record {i} ({record.id}) contains invalid characters: {', '.join(invalid)}"
            )
    return errors


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


def summarize(records, source_name):
    lengths = [len(r.seq) for r in records]
    total_bases = sum(lengths)
    avg_len = total_bases / len(lengths) if lengths else 0
    all_seq = "".join(str(r.seq) for r in records)

    report = []
    report.append("FASTA Sequence Analyzer Report")
    report.append("=" * 30)
    report.append("")
    report.append(f"File: {source_name}")
    report.append(f"Records: {len(records)}")
    report.append(f"Total bases: {total_bases}")
    report.append(f"Average length: {avg_len:.2f}")
    report.append(f"Min length: {min(lengths) if lengths else 0}")
    report.append(f"Max length: {max(lengths) if lengths else 0}")
    report.append(f"GC content: {gc_content(all_seq):.2f}%")
    report.append("")
    report.append("Nucleotide counts:")
    counts = nucleotide_counts(records)
    for base in ["A", "T", "G", "C", "N"]:
        report.append(f"{base}: {counts[base]}")
    report.append("")

    if len(records) > 1:
        report.append("Record details:")
        for record in records:
            report.append(f"- {record.id}: {len(record.seq)} bp, GC {gc_content(str(record.seq)):.2f}%")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Analyze FASTA files.")
    parser.add_argument("input", help="Path to FASTA file")
    parser.add_argument("--output", help="Write report to file", default=None)
    args = parser.parse_args()

    fasta_path = Path(args.input)
    if not fasta_path.exists():
        print(f"File not found: {fasta_path}")
        sys.exit(1)

    records = read_fasta(str(fasta_path))
    errors = validate_fasta(records)

    report = summarize(records, str(fasta_path))

    if errors:
        report += "\nValidation warnings:\n"
        for err in errors:
            report += f"- {err}\n"

    print(report)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()