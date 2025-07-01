# Protogenix: A Multi-Agent AI System for De Novo Protein Design

This project presents **Protogenix**, a modular multi-agent system developed for automating de novo protein design. It integrates generative AI, protein folding prediction, and structural analysis via LangGraph and multiple scientific tools.

---

## 🧠 Project Overview

**Goal:**  
Design, validate, and analyze protein structures using an orchestrated pipeline of intelligent agents and tools.

**Key Technologies:**
- 🧬 **Chroma** for generative backbone and sequence design
- 🔬 **OmegaFold** for protein structure prediction
- 🌊 **ANM (Anisotropic Network Model)** for dynamics & flexibility analysis
- 🔗 **LangGraph** to orchestrate autonomous agents and tools
- 📚 **UniProt & PubMed** for biological validation & RAG-based retrieval

---

## 🧪 Agents and Responsibilities

| Agent Name               | Description |
|--------------------------|-------------|
| `Planner` | Resolves biological and medical abbreviation ambiguity |
| `SymptomAnalyzer`           | Interprets biological functions or pathologies from input queries |
| `DrugAdvisor`               | Suggests known modulators, ligands, or inhibitors (via UniProt/PubMed RAG) |
| `DiagnosticSummarizer`     | Consolidates output into a biological hypothesis |

---

## 🛠️ Tools

| Tool Name         | Purpose |
|-------------------|---------|
| `ChromaTool`      | Generate protein backbones/sequences with constraints |
| `OmegaFoldTool`   | Predict high-resolution protein structures |
| `ANMTool`         | Compute structural flexibility and RMSD |
| `UniProtSearchTool` | Perform biological validation or find known proteins with similar motifs |

---

## 📁 Example Workflows

1. **Protein Design Request:**
   > "Design a thermostable alpha-helix protein under 80 residues with high flexibility in the C-terminal region."
   - Chroma designs sequence
   - OmegaFold predicts structure
   - ANM analyzes dynamics
   - Agents validate via PubMed/UniProt


---

## 📊 Notebooks
- `prot.ipynb` – Generating protein sequences with custom constraints  


---

## 📦 Installation

```bash
git clone https://github.com/KonouzA/Protgenix.git
cd Protgenix
pip install -r requirements.txt
