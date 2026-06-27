import os
import json
import uuid
from typing import Dict, List
from dotenv import load_dotenv

# Load env variables
load_dotenv()

def process_event_with_agents(event_type: str, amount: float, user_memory: Dict) -> List[Dict]:
    """
    Uses LangChain and OpenAI to generate recommendations if an API key is present.
    Falls back to a deterministic rules-engine if not configured or if an error occurs.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key and api_key != "your_openai_api_key_here":
        try:
            from langchain_openai import ChatOpenAI
            from langchain_core.prompts import PromptTemplate
            from langchain_core.output_parsers import JsonOutputParser
            from pydantic import BaseModel, Field
            
            class Nudge(BaseModel):
                title: str = Field(description="Short title of the recommendation")
                description: str = Field(description="Why this is recommended, based on user numbers")
                action_text: str = Field(description="Text for the action button (e.g., 'Invest ₹5,000')")
                amount: float = Field(description="The numeric amount associated with the action")
                category: str = Field(description="One of: 'Investment', 'Bills', 'Savings', 'Credit', 'Support', 'Travel'")
            
            class NudgeList(BaseModel):
                recommendations: List[Nudge]
                
            parser = JsonOutputParser(pydantic_object=NudgeList)
            
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2, api_key=api_key)
            
            prompt = PromptTemplate(
                template="""You are the SBI Smart Financial Coach, an expert AI agent orchestrator.
An event has occurred: {event_type}. The transaction amount or value associated is: ₹{amount}.
The user's current memory state is:
- Balance: ₹{balance}
- Monthly Income: ₹{income}
- Avg Monthly Expense: ₹{expense}
- Active Goals: {goals}
- Upcoming Bills: {bills}

Your task is to analyze this event against the user's memory and generate up to 3 contextually relevant, data-driven financial recommendations (nudges).

Handling Specific Events:
1. "FD Maturing Soon": Suggest renewing the FD or moving funds to Mutual Funds/SIPs.
2. "Upcoming EMI Shortfall": Warn if balance is too low before an EMI, suggest transferring funds.
3. "Large Unusual Inflow": Detect bonuses/asset sales and suggest investments rather than leaving cash idle.
4. "High Credit Card Utilization": Warn about credit score impacts and suggest a mid-cycle partial payment.
5. "Sustained High Idle Balances": Suggest auto-sweep (Flexi-Deposit) or SIPs to fight inflation.
6. "Missing Salary": Detect job loss/hardship and offer EMI moratorium or loan restructuring options.
7. "First-Time International Travel": Detect international portal spends and suggest Forex cards or enabling international transactions.
8. "Salary Credited": Suggest investments or emergency fund top-ups with surplus cash.

Prioritize urgent financial risks (like avoiding bounce charges or high credit utilization) over discretionary investments.

{format_instructions}""",
                input_variables=["event_type", "amount", "balance", "income", "expense", "goals", "bills"],
                partial_variables={"format_instructions": parser.get_format_instructions()},
            )
            
            chain = prompt | llm | parser
            
            response = chain.invoke({
                "event_type": event_type,
                "amount": amount,
                "balance": user_memory.get("balance"),
                "income": user_memory.get("monthly_income"),
                "expense": user_memory.get("avg_monthly_expense"),
                "goals": user_memory.get("goals"),
                "bills": user_memory.get("upcoming_bills")
            })
            
            # Format to our expected dictionary structure with uuids
            recommendations = []
            for rec in response.get("recommendations", []):
                rec_dict = dict(rec)
                rec_dict["id"] = str(uuid.uuid4())
                recommendations.append(rec_dict)
                
            if recommendations:
                return recommendations
        except Exception as e:
            print(f"LLM Agent Error, falling back to rule engine: {e}")
            
    # Fallback / Mock logic for the expanded events
    return _mock_process_event(event_type, amount, user_memory)


def _mock_process_event(event_type: str, amount: float, user_memory: Dict) -> List[Dict]:
    recommendations = []
    avg_expense = user_memory.get("avg_monthly_expense", 38000)
    
    if event_type == "Salary Credited":
        surplus = amount - avg_expense
        if surplus > 0:
            safe_invest_amount = min(10000, surplus * 0.5)
            recommendations.append({
                "id": str(uuid.uuid4()),
                "title": "Invest Surplus",
                "description": f"Your average expenses are ₹{avg_expense:,.0f}. You have a safe surplus of ₹{surplus:,.0f} this month.",
                "action_text": f"Invest ₹{safe_invest_amount:,.0f} in SIP",
                "amount": safe_invest_amount,
                "category": "Investment"
            })
            
    elif event_type == "FD Maturing Soon":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "FD Maturing in 7 Days",
            "description": f"Your Term Deposit of ₹{amount:,.0f} is maturing. Current rates for a 1-year renewal are 7.1%.",
            "action_text": "Renew at 7.1%",
            "amount": amount,
            "category": "Investment"
        })
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Diversify into SIP",
            "description": "Consider moving 20% of your matured FD into a Balanced Mutual Fund for higher long-term growth.",
            "action_text": "Start SIP",
            "amount": amount * 0.2,
            "category": "Investment"
        })
        
    elif event_type == "Upcoming EMI Shortfall":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Low Balance Warning",
            "description": f"You have an upcoming EMI of ₹{amount:,.0f} in 3 days, but your current balance is lower.",
            "action_text": "Transfer Funds",
            "amount": amount,
            "category": "Bills"
        })
        
    elif event_type == "Large Unusual Inflow":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Significant Inflow Detected",
            "description": f"You received ₹{amount:,.0f}. Leaving this in a savings account loses value to inflation.",
            "action_text": "Open Short-Term FD",
            "amount": amount * 0.8,
            "category": "Investment"
        })
        
    elif event_type == "High Credit Card Utilization":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Credit Score Alert",
            "description": f"Your credit card utilization is very high (₹{amount:,.0f}). This can negatively impact your CIBIL score.",
            "action_text": "Pay Partially Now",
            "amount": amount * 0.5,
            "category": "Credit"
        })
        
    elif event_type == "Sustained High Idle Balances":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Idle Cash Opportunity",
            "description": f"You have ₹{amount:,.0f} earning minimal interest. Enable Auto-Sweep to earn FD rates on surplus funds.",
            "action_text": "Enable Auto-Sweep",
            "amount": amount,
            "category": "Savings"
        })
        
    elif event_type == "Missing Salary":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Financial Hardship Assistance",
            "description": "We noticed a drop in your regular income. We are here to help during tough times.",
            "action_text": "Explore EMI Moratorium",
            "amount": 0,
            "category": "Support"
        })
        
    elif event_type == "First-Time International Travel":
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Enable International Spends",
            "description": "It looks like you're traveling! Your cards are currently disabled for international transactions for security.",
            "action_text": "Enable Now",
            "amount": 0,
            "category": "Travel"
        })
        recommendations.append({
            "id": str(uuid.uuid4()),
            "title": "Get a Multi-Currency Card",
            "description": "Save on forex markup fees (up to 3.5%) by loading an SBI Multi-Currency Forex Card.",
            "action_text": "Order Forex Card",
            "amount": 0,
            "category": "Travel"
        })
        
    # Generic Bill and Goal Checks for all events
    bills_raw = user_memory.get("upcoming_bills", "[]")
    if isinstance(bills_raw, str):
        bills = json.loads(bills_raw)
    else:
        bills = bills_raw
        
    for bill in bills:
        if bill.get("due_in_days", 10) <= 5 and event_type not in ["Upcoming EMI Shortfall", "Missing Salary"]:
            recommendations.append({
                "id": str(uuid.uuid4()),
                "title": f"{bill['name']} Due Soon",
                "description": f"Your {bill['name']} of ₹{bill['amount']:,.0f} is due in {bill['due_in_days']} days.",
                "action_text": f"Pay ₹{bill['amount']:,.0f} Now",
                "amount": bill['amount'],
                "category": "Bills"
            })

    priority = {"Bills": 1, "Credit": 1, "Support": 1, "Travel": 2, "Savings": 3, "Investment": 4}
    recommendations.sort(key=lambda x: priority.get(x["category"], 5))
    return recommendations[:3]
