# 🧬 FASTA Sequence Analyzer

A modular **Python** and **Biopython** command-line application for analyzing DNA sequences stored in **FASTA** format.

The project performs sequence validation, nucleotide composition analysis, GC content calculation, DNA transcription, protein translation, motif searching, restriction enzyme recognition site analysis, and generates detailed analysis reports.

---

# 📚 Table of Contents

- Overview
- Features
- Sequence Analysis
- Supported Restriction Enzymes
- Project Structure
- Installation
- Usage
- Example Output
- Technologies
- Development Roadmap
- Future Improvements
- Contributing
- License
- Author

---

# 🔬 Overview

FASTA Sequence Analyzer is a modular bioinformatics toolkit designed to analyze DNA sequences stored in FASTA files.

This project demonstrates practical applications of:

- Bioinformatics
- Molecular Biology
- Computational Biology
- Scientific Python Programming
- Command-Line Application Development

The project is intended both as a learning resource and as a professional portfolio project demonstrating software development for biological data analysis.

---

# ✨ Features

## ✅ Current Features (Version 2.2)

- Read FASTA files
- Parse single and multi-FASTA files
- Validate nucleotide sequences
- Detect invalid DNA characters
- Calculate GC content
- Generate sequence statistics
- Count nucleotide composition (A, T, G, C, N)
- Generate reverse complements
- DNA → RNA transcription
- DNA → Protein translation
- DNA motif search
- Restriction enzyme recognition site analysis
- Export reports to text files
- Modular Python architecture

---

# 🧬 Sequence Analysis

| Analysis | Description |
|----------|-------------|
| GC Content | Calculates percentage of G and C nucleotides |
| Nucleotide Counts | Counts A, T, G, C and N bases |
| Reverse Complement | Generates reverse complementary DNA strand |
| DNA → RNA | Converts DNA into RNA |
| DNA → Protein | Translates DNA into amino acid sequence |
| DNA Motif Search | Finds user-defined DNA motifs |
| Restriction Enzyme Analysis | Detects recognition sites of common restriction enzymes |

---

# 🧪 Supported Restriction Enzymes

| Enzyme | Recognition Sequence |
|---------|----------------------|
| EcoRI | GAATTC |
| BamHI | GGATCC |
| HindIII | AAGCTT |
| NotI | GCGGCCGC |
| XhoI | CTCGAG |

Example:

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --enzyme EcoRI
```

---

# 📁 Project Structure

```text
FASTA-Sequence-Analyzer/
│
├── fasta_analyzer.py          # Main application
├── sequence_utils.py          # Sequence utility functions
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── sample_data/
│     └── human_gene.fasta
│
├── output/
│
├── screenshots/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/HareemAhmad-Molbio/FASTA-Sequence-Analyzer.git
```

Move into the project

```bash
cd FASTA-Sequence-Analyzer
```

Create a virtual environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

### Analyze a FASTA file

```bash
python fasta_analyzer.py sample_data/human_gene.fasta
```

---

### Export report

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --output output/report.txt
```

---

### Search for a DNA motif

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --find ATG
```

---

### Search for a restriction enzyme

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --enzyme EcoRI
```
# 📸 Screenshots

## FASTA Sequence Analysis

![FASTA Analyzer](screenshots/analyzer_output.png)

---

## DNA Motif Search

![Motif Search](screenshots/motif_search.png)

---

## Restriction Enzyme Analysis

![Restriction Enzyme](screenshots/restriction_enzyme.png)
---

# 📄 Example Output

```text
FASTA Sequence Analyzer Report
========================================

File: sample_data/human_gene.fasta

Records: 1
Total Bases: 126033
Average Length: 126033
Minimum Length: 126033
Maximum Length: 126033
GC Content: 44.10%

Sequence Preview
----------------------------------------

DNA
CTTTCTGTCCCCGCCCTTCCTCTGACTGTGT...

RNA
CUUUCUGUCCCCGCCCUUCCUCUGACUGUGU...

Reverse Complement
CACGCTTTACTGTTGCCACGGAA...

Protein
LSVPPFL*LCLDFLF*EAIAQRFPWQQ*SV

Nucleotide Counts

A : 35147
T : 35309
G : 28369
C : 27208
N : 0

Motif Search

Motif: ATG
Occurrences: 57

Restriction Enzyme Analysis

Enzyme: EcoRI
Recognition Site: GAATTC
Occurrences: 0
```

---

# 🧪 Example Dataset

The repository contains a sample FASTA file for testing.

Additional public datasets can be obtained from:

- NCBI
- Ensembl
- UCSC Genome Browser

---

# 🛠 Technologies Used

- Python
- Biopython
- argparse
- pathlib
- collections
- Git
- GitHub

---

# 📈 Development Roadmap

| Version | Status | Features |
|----------|--------|----------|
| ✅ v1.0 | Complete | FASTA parsing, validation, GC content, nucleotide counts |
| ✅ v2.0 | Complete | Reverse complement, DNA→RNA transcription, DNA→Protein translation |
| ✅ v2.1 | Complete | DNA motif search |
| ✅ v2.2 | Complete | Restriction enzyme recognition site analysis |
| 🚧 v3.0 | In Development | Open Reading Frame (ORF) Finder |
| ⏳ v4.0 | Planned | GC Content & Nucleotide Composition Plots |
| ⏳ v5.0 | Planned | HTML & PDF Report Generation |
| ⏳ v6.0 | Planned | Batch FASTA Analysis |
| ⏳ v7.0 | Planned | Interactive CLI |
| ⏳ v8.0 | Planned | Desktop GUI |

---

# 🎯 Future Improvements

Planned additions include:

- Open Reading Frame (ORF) Finder
- Six-frame Translation
- Batch FASTA Analysis
- GC Content Visualization
- Nucleotide Composition Charts
- Codon Usage Analysis
- Sequence Alignment
- HTML Reports
- PDF Reports
- Interactive CLI
- Desktop GUI
- Unit Testing
- Continuous Integration (GitHub Actions)
- PyPI Package Distribution

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you would like to contribute:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

See the **LICENSE** file for more details.

---

# 👨‍🔬 Author

**Hareem Ahmad**

**M.Sc. Molecular Biology & Biochemistry**

**Interests**

- Bioinformatics
- Molecular Biology
- Computational Biology
- Scientific Programming

GitHub:

https://github.com/HareemAhmad-Molbio

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Your support helps improve the project and encourages future development.