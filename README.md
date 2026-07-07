# 🧬 FASTA Sequence Analyzer

A Python-based bioinformatics tool for analyzing DNA sequences stored in FASTA format. This project provides sequence validation, nucleotide composition statistics, GC content analysis, and detailed summary reports using Biopython.

> **Status:** 🚧 Actively Developing  
> Current Version: **v1.0**

---

## 📖 Overview

FASTA Sequence Analyzer is designed to simplify the analysis of DNA sequences in FASTA files. It performs essential sequence quality checks and generates a comprehensive report containing sequence statistics and nucleotide composition.

This project demonstrates practical applications of Python in bioinformatics and serves as a foundation for more advanced sequence analysis tools.

---

## ✨ Features

### Current Features (v1.0)

- ✅ Read FASTA files
- ✅ Validate nucleotide sequences
- ✅ Detect invalid characters
- ✅ Calculate GC content
- ✅ Count nucleotides (A, T, G, C, N)
- ✅ Generate sequence statistics
- ✅ Support single and multi-FASTA files
- ✅ Export analysis report to a text file

---

## 🚀 Planned Features

Future releases will include:

- 🔄 Reverse Complement Generation
- 🧬 DNA → RNA Transcription
- 🧪 DNA → Protein Translation
- 🔍 Motif Search
- 🧬 Open Reading Frame (ORF) Detection
- ✂️ Restriction Enzyme Site Finder
- 📊 GC Content Visualization
- 📈 Base Composition Charts
- 🌐 HTML Reports
- 📄 PDF Reports
- 🖥 Interactive Command-Line Interface
- 📦 Python Package Distribution
- 🧪 Unit Testing

---

## 📂 Project Structure

```text
FASTA-Sequence-Analyzer/
│
├── fasta_analyzer.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── sample_data/
│   └── human_gene.fasta
│
├── output/
│
└── screenshots/
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/HareemAhmad-Molbio/FASTA-Sequence-Analyzer.git
```

Move into the project directory:

```bash
cd FASTA-Sequence-Analyzer
```

Create a virtual environment:

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

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📦 Requirements

- Python 3.10+
- Biopython

Install manually if needed:

```bash
pip install biopython
```

---

## ▶️ Usage

Analyze a FASTA file:

```bash
python fasta_analyzer.py sample_data/human_gene.fasta
```

Save the report to a file:

```bash
python fasta_analyzer.py sample_data/human_gene.fasta --output output/report.txt
```

---

## 📋 Example Output

```text
FASTA Sequence Analyzer Report
==============================

File: sample_data/human_gene.fasta
Records: 1
Total bases: 126033
Average length: 126033.00
Min length: 126033
Max length: 126033
GC content: 44.10%

Nucleotide counts:
A: 35147
T: 35309
G: 28369
C: 27208
N: 0
```

---

## 🧪 Example Dataset

The repository includes a sample FASTA sequence for testing.

You may also use publicly available FASTA files from:

- NCBI
- Ensembl
- UCSC Genome Browser

---

## 🛠 Technologies Used

- Python
- Biopython
- argparse
- pathlib
- collections
- Git

---

## 🎯 Learning Objectives

This project demonstrates:

- Bioinformatics sequence analysis
- FASTA parsing
- DNA sequence validation
- Python command-line application development
- Scientific programming
- Clean code organization
- GitHub project management

---

## 📈 Project Roadmap

| Version | Status | Features |
|----------|--------|----------|
| v1.0 | ✅ Complete | FASTA parsing, validation, GC content, nucleotide counts |
| v2.0 | 🚧 In Progress | Reverse complement, transcription, translation |
| v3.0 | ⏳ Planned | Motif search, ORF finder |
| v4.0 | ⏳ Planned | Sequence visualizations |
| v5.0 | ⏳ Planned | HTML & PDF reports |
| v6.0 | ⏳ Planned | Interactive CLI |
| v7.0 | ⏳ Planned | Desktop GUI |

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve this project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

See the **LICENSE** file for details.

---

## 👨‍🔬 Author

**Hareem Ahmad**

M.Sc. Molecular Biology & Biochemistry

Bioinformatics | Molecular Biology | Computational Biology

GitHub: https://github.com/HareemAhmad-Molbio

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.