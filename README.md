# AI Recruitment Automation Platform 🤖💼

A production-ready automation system designed to streamline the hiring process using **LLMs**, **LangChain**, and **n8n**. This platform automates resume ingestion, performs deep content analysis, and executes intelligent decision-making workflows.

## 📊 System Architecture & Logic

### 1. Platform Overview
An end-to-end visualization of the candidate journey—from resume submission via Gmail or Google Drive to the final automated decision.
![Platform Overview](assets/platform_overview.png)

### 2. n8n Workflow Logic
The orchestration layer where PDF-to-text conversion and API routing are managed visually.
![n8n Logic](assets/n8n_workflow.png)

### 3. LangChain Internal Architecture
A detailed look at the "AI Brain," showcasing how structured output parsers and LLM chains evaluate candidate data.
![LangChain Architecture](assets/langchain_logic.png)

### 4. Automated Action Workflow
The decision loop that triggers Slack notifications and personalized feedback based on the AI-calculated score.
![Action Workflow](assets/action_workflow.png)

---

## 🚀 Key Features
*   **Agentic Evaluation**: Uses LangChain and GPT-4o to analyze CVs against JDs with human-like reasoning.
*   **Structured Scoring**: Generates a normalized score (0-100) and extracts specific "Missing Skills".
*   **Seamless Orchestration**: Fully managed by n8n for high reliability and scalability.
*   **Intelligent Alerts**: Automated Slack notifications for high-potential candidates (Score ≥ 80).
*   **Automated Feedback**: Generates constructive rejection emails for candidates who do not meet the threshold.

## 🛠️ Tech Stack
*   **Orchestration**: n8n
*   **AI Framework**: LangChain
*   **Model**: OpenAI GPT-4o
*   **Backend**: FastAPI (Python)
*   **PDF Parsing**: PyPDF

## 📂 Project Structure
```text
ai-recruitment-automation/
├── assets/                 # Architecture diagrams
├── src/
│   ├── main.py             # FastAPI entry point
│   ├── evaluator.py        # LangChain logic
│   └── parser.py           # PDF utility
├── workflows/
│   └── n8n_flow.json       # Exported n8n workflow
├── .env                    # API Keys (Local only)
├── .gitignore              # Files to ignore
├── requirements.txt        # Dependencies
└── README.md               # Documentation
🚥 Evaluation Example
CriteriaResultScore85/100Status✅ PASS -> Interview Invite SentFit SummaryCandidate has strong Python/n8n expertise; fits 90% of JD requirements.Missing SkillsExperience with Kubernetes and Vector Databases.
🚦 Getting Started1. InstallationClone the repository and install the required Python libraries:Bashgit clone [https://github.com/AizazMuhammad/ai-recruitment-automation.git](https://github.com/AizazMuhammad/ai-recruitment-automation.git)
cd ai-recruitment-automation
pip install -r requirements.txt
2. Setup EnvironmentCreate a .env file in the root directory and add your OpenAI API key:PlaintextOPENAI_API_KEY=your_actual_key_here
3. Run the Backend APIStart the FastAPI server:Bashpython src/main.py
👤 Author:
Aizaz Muhammad
AI Engineer & Data Scientist
