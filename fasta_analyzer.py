#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from sequence_utils import (
    gc_content,
    nucleotide_counts,
    reverse_complement,
    transcribe_dna,
    translate_protein,
    find_motif,
    find_restriction_sites,
)

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


def summarize(records, source_name):
    lengths = [len(r.seq) for r in records]
    total_bases = sum(lengths)
    avg_len = total_bases / len(lengths) if lengths else 0
    all_seq = "".join(str(r.seq) for r in records)

    report = []

    report.append("FASTA Sequence Analyzer Report")
    report.append("=" * 40)
    report.append("")
    report.append(f"File: {source_name}")
    report.append(f"Records: {len(records)}")
    report.append(f"Total bases: {total_bases}")
    report.append(f"Average length: {avg_len:.2f}")
    report.append(f"Min length: {min(lengths) if lengths else 0}")
    report.append(f"Max length: {max(lengths) if lengths else 0}")
    report.append(f"GC content: {gc_content(all_seq):.2f}%")

    preview = all_seq[:90]

    report.append("")
    report.append("Sequence Preview")
    report.append("-" * 40)
    report.append(f"DNA                : {preview}")
    report.append(f"RNA                : {transcribe_dna(preview)}")
    report.append(f"Reverse Complement : {reverse_complement(preview)}")
    report.append(f"Protein            : {translate_protein(preview)}")

    report.append("")
    report.append("Nucleotide counts:")

    counts = nucleotide_counts(records)

    for base in ["A", "T", "G", "C", "N"]:
        report.append(f"{base}: {counts[base]}")

    if len(records) > 1:
        report.append("")
        report.append("Record details:")

        for record in records:
            report.append(
                f"- {record.id}: {len(record.seq)} bp, "
                f"GC {gc_content(str(record.seq)):.2f}%"
            )

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Analyze FASTA files.")

    parser.add_argument(
        "input",
        help="Path to FASTA file",
    )

    parser.add_argument(
        "--output",
        help="Write report to file",
        default=None,
    )

    parser.add_argument(
        "--find",
        help="Search for a DNA motif",
        default=None,
    )
    
    parser.add_argument(
        "--enzyme",
        help="Search for a restriction enzyme recognition site",
        default=None,
    )

    args = parser.parse_args()

    fasta_path = Path(args.input)

    if not fasta_path.exists():
        print(f"File not found: {fasta_path}")
        sys.exit(1)

    records = read_fasta(str(fasta_path))
    errors = validate_fasta(records)

    report = summarize(records, str(fasta_path))

    if args.find:
        all_seq = "".join(str(record.seq) for record in records)

        positions = find_motif(all_seq, args.find)

        report += "\n\n"
        report += "Motif Search\n"
        report += "=" * 40 + "\n"
        report += f"Motif: {args.find}\n"
        report += f"Occurrences: {len(positions)}\n"

        if positions:
            report += "Positions:\n"
            report += ", ".join(map(str, positions))
        else:
            report += "Motif not found."

    if errors:
        report += "\n\nValidation warnings:\n"

        for err in errors:
            report += f"- {err}\n"

    print(report)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report + "\n", encoding="utf-8")

    if args.find:
       ...
    else:
        report += "Motif not found."


    if args.enzyme:
        all_seq = "".join(str(record.seq) for record in records)

        recognition_site, positions = find_restriction_sites(
        all_seq,
        args.enzyme,
    )

        report += "\n\n"
        report += "Restriction Enzyme Analysis\n"
        report += "=" * 40 + "\n"

        if recognition_site is None:
            report += f"Unknown enzyme: {args.enzyme}\n"
        else:
            report += f"Enzyme: {args.enzyme}\n"
            report += f"Recognition Site: {recognition_site}\n"
            report += f"Occurrences: {len(positions)}\n"

        if positions:
            report += "Positions:\n"
            report += ", ".join(map(str, positions))
        else:
            report += "Recognition site not found."


    if errors:
        report += "\n\nValidation warnings:\n"

    for err in errors:
        report += f"- {err}\n"


    print(report)

    if args.output:
        ...

if __name__ == "__main__":
    main()