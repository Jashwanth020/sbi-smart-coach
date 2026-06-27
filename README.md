# SBI Smart Financial Coach 🚀

**An Autonomous Multi-Agent AI Financial Assistant for Customer Acquisition & Digital Banking Adoption**

SBI Smart Financial Coach turns the mobile banking app from a passive transaction tool into a **proactive financial co-pilot**. Instead of waiting for a customer to ask a question, this system watches financial events (e.g., a salary credit, a maturing FD, an upcoming bill) and uses a coordinated team of AI agents to surface explainable, context-aware nudges.

## Features

This MVP includes an interactive React frontend and a FastAPI LangChain backend that orchestrates the following 8 real-time proactive events:

1. 💰 **Salary Credited:** Suggests investments or emergency fund top-ups with surplus cash.
2. 📈 **FD Maturing Soon:** Suggests renewing the FD or moving funds to Mutual Funds/SIPs.
3. 🚨 **Upcoming EMI Shortfall:** Warns if balance is too low before an EMI, suggests transferring funds.
4. 💸 **Large Unusual Inflow:** Detects bonuses/asset sales and suggests investments rather than leaving cash idle.
5. 💳 **High Credit Card Utilization:** Warns about credit score impacts and suggests a mid-cycle partial payment.
6. 🏦 **Sustained High Idle Balances:** Suggests auto-sweep (Flexi-Deposit) or SIPs to fight inflation.
7. 🆘 **Missing Salary:** Detects job loss/hardship and offers EMI moratorium or loan restructuring options.
8. ✈️ **First-Time International Travel:** Detects international portal spends and suggests Forex cards or enabling international transactions.

## Tech Stack

- **Frontend:** React, Vite, Vanilla CSS (Premium Dark Navy Theme)
- **Backend:** FastAPI, Python, SQLite (Persistent Memory)
- **AI / Orchestration:** LangChain, OpenAI (GPT-4o-mini)

## Setup Instructions

### 1. Backend (FastAPI + LangChain)

```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
```

**Configure API Key:**
Rename `.env.example` to `.env` and add your OpenAI API key.
*(Note: If you do not provide an API key, the backend will safely fall back to a deterministic rule-engine so the demo remains fully functional).*

**Run Backend:**
```bash
uvicorn main:app --port 8000
```

### 2. Frontend (React + Vite)

Open a new terminal window:
```bash
cd frontend
npm install
npm run dev
```

The application will be live at `http://localhost:5173`. 

## Demo Usage

1. Open the web interface.
2. Observe your mock Financial Health score on the left panel.
3. Use the **Simulation Dropdown** to select one of the 8 banking events.
4. Click **Trigger** to send the event to the AI Orchestrator.
5. The LangChain agent will read your current financial state and surface up to 3 tailored nudges.
6. Approve or dismiss nudges, and watch the actions securely commit to the immutable Audit Trail.
