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

| **Agent Name**             | **Description**                                                                                                                                                                                                             |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **RAG Agent**              | Determines whether external biomedical knowledge is needed based on the user's request. If so, it extracts a relevant query and retrieves scientific context from PubMed using a RAG (Retrieval-Augmented Generation) tool. |
| **Planner Agent**          | Parses the user's protein design request and generates a structured, multi-step plan using predefined tool schemas and a language model.                                                                                    |
| **Executor Agent**         | Executes each planned step by calling the appropriate tool with validated parameters, and records the results and progress.                                                                                                 |
| **Evaluator Agent**        | Reviews tool outputs and scores them based on technical metrics (e.g., pLDDT), domain knowledge (e.g., structure alignment), and match with user constraints (e.g., CATH class, symmetry).                                  |
| **Revision Planner Agent** | Analyzes low-scoring steps and revises them using heuristics, memory of past successes, or LLM-based reasoning to improve overall design performance.                                                                       |


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
- `protgenix.ipynb` – Generating protein sequences with custom constraints  


---

## 📦 Installation

```bash
git clone https://github.com/KonouzA/Protgenix.git
cd Protgenix
pip install -r requirements.txt
