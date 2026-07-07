# 🧬 FASTA Sequence Analyzer

A professional bioinformatics command-line application built with **Python** and **Biopython** for analyzing DNA sequences stored in **FASTA** format.

The project performs sequence validation, nucleotide composition analysis, GC content calculation, DNA transcription, protein translation, reverse complement generation, and produces detailed sequence reports.

---

# 📚 Table of Contents

- Overview
- Features
- Project Structure
- Installation
- Usage
- Example Output
- Technologies
- Roadmap
- Future Improvements
- Contributing
- License
- Author

---

# 🔬 Overview

FASTA Sequence Analyzer is a modular bioinformatics toolkit designed to analyze DNA sequences stored in FASTA files.

The project demonstrates practical applications of:

- Bioinformatics
- Molecular Biology
- Computational Biology
- Scientific Python Programming

This repository is intended both as a learning project and as a portfolio project demonstrating software development for biological data analysis.

---

# ✨ Features

## ✅ Current Features (Version 2.0)

- Read FASTA files
- Parse single and multi-FASTA sequences
- Validate nucleotide sequences
- Detect invalid DNA characters
- Calculate GC Content
- Calculate sequence statistics
- Count nucleotide composition (A, T, G, C, N)
- Generate Reverse Complement
- DNA → RNA Transcription
- DNA → Protein Translation
- Export reports to text files
- Modular project architecture

---

# 🧬 Sequence Analysis

Current biological analyses include:

| Analysis | Description |
|----------|-------------|
| GC Content | Calculates percentage of G and C nucleotides |
| Nucleotide Counts | Counts A, T, G, C and N |
| Reverse Complement | Generates reverse complementary DNA strand |
| DNA → RNA | Transcribes DNA into RNA |
| DNA → Protein | Translates coding DNA into amino acid sequence |

---

# 📁 Project Structure

```text
FASTA-Sequence-Analyzer/
│
├── fasta_analyzer.py          # Main application
├── sequence_utils.py          # Sequence analysis functions
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
│
└── plots/
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

Analyze a FASTA sequence

```bash
python fasta_analyzer.py sample_data/human_gene.fasta
```

Generate a report

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --output output/report.txt
```

---

# 📄 Example Output

```text
FASTA Sequence Analyzer Report
==============================

File: sample_data/human_gene.fasta

Records: 1

Total Bases: 126033

Average Length: 126033

GC Content: 44.10%

Sequence Preview
==============================

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
```
---

# 🧪 Example Dataset

This repository contains an example FASTA file for testing.

Public datasets can also be downloaded from:

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
| ✅ Version 1.0 | Complete | FASTA parsing, validation, GC content, nucleotide statistics |
| ✅ Version 2.0 | Complete | Reverse complement, DNA→RNA transcription, DNA→Protein translation |
| 🚧 Version 2.1 | In Progress | Motif Search |
| ⏳ Version 3.0 | Planned | Open Reading Frame (ORF) Finder |
| ⏳ Version 4.0 | Planned | Restriction Enzyme Analysis |
| ⏳ Version 5.0 | Planned | Sequence Visualizations |
| ⏳ Version 6.0 | Planned | HTML & PDF Reports |
| ⏳ Version 7.0 | Planned | Interactive Command-Line Interface |
| ⏳ Version 8.0 | Planned | Desktop GUI |

---

# 🎯 Future Improvements

Planned additions include:

- DNA Motif Search
- Open Reading Frame Detection
- Restriction Enzyme Site Finder
- GC Content Graphs
- Nucleotide Composition Charts
- Sequence Alignment
- HTML Reports
- PDF Reports
- Desktop GUI
- Unit Testing
- PyPI Package Distribution

---

# 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

If you'd like to contribute:

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

# 👨‍🔬 Author

**Hareem Ahmad**

M.Sc. Molecular Biology & Biochemistry

Bioinformatics • Molecular Biology • Computational Biology

GitHub:
https://github.com/HareemAhmad-Molbio

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps support the project and encourages future development.