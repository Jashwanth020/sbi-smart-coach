# SBI Smart Financial Coach
### *An Autonomous Multi-Agent AI Financial Assistant for Customer Acquisition & Digital Banking Adoption*

**Theme:** Agentic AI | **Track:** Customer Acquisition & Digital Adoption

---

## 1. Executive Summary

**SBI Smart Financial Coach** turns the SBI mobile banking app from a passive transaction tool into a **proactive financial co-pilot**.

Most banking apps wait for the customer to ask a question. This system instead watches financial *events* — a salary credit, a rising credit utilization, an upcoming bill — and a coordinated team of specialized AI agents decides what (if anything) should be recommended, explains the reasoning in plain language, and executes only after explicit one-tap customer approval.

**In one line:** *We don't wait for customers to ask for help — we notice the moment they need it, and act on their behalf within guardrails they control.*

**Target outcomes for SBI:**
| Goal | Mechanism |
|---|---|
| Customer acquisition | Personalized first-30-days journey nudges new users into SIPs, RDs, insurance at the right moment |
| Digital adoption | Converts passive balance-checkers into active users of SIP, bill-pay, and investment features |
| Cross-sell | Recommendations are contextual and consent-based, not generic banner ads |
| Retention | Continuous, useful engagement — not just login-triggered interaction |
| Financial literacy | Every recommendation is accompanied by a plain-language "why" |

---

## 2. Problem Statement Alignment

**Official Problem Statement:** *Use of Agentic AI for Customer Acquisition, Digital Adoption & Digital Engagement*

This proposal is mapped directly to all three official focus pillars — not retrofitted to match them after the fact:

| Pillar | Official ask | Where this proposal delivers it |
|---|---|---|
| **1. Customer Acquisition** | Intelligently identify, qualify, and convert customers through hyper-personalised engagement and conversational onboarding | First-30-days onboarding journey (Section 18) nudging new-to-bank customers into SIPs, RDs, and insurance at the right moment, with conversational, plain-language explanations (Section 13) rather than generic offer screens |
| **2. Digital Adoption** | Contextual and adaptive AI experiences that encourage adoption of payments, investments, insurance, and mobile banking | Bill Reminder, Investment Recommendation, and Spending Analysis agents (Section 6) surfacing the *right* digital feature at the moment of relevance; Smart Contextual Nudges (Section 13) replace generic "Open an FD" banners with numbers-grounded suggestions |
| **3. Digital Engagement** | AI-driven engagement models that proactively interact with customers based on behaviours, financial patterns, and life events | This is where the proposal goes deepest — Persistent Customer Memory (Section 8), Collaborative Multi-Agent Reasoning (Section 9), Adaptive Learning (Section 10), and Life-Event Detection (Section 12) together build an engagement model that compounds over the relationship, not a single-session feature |

**On the sixth jury evaluation criterion — Regulatory Readiness:** Section 14 (Responsible-AI & Compliance Guardrails) is written specifically against RBI's consent, explainability, and audit-trail expectations and the DPDP Act's consent-and-purpose-limitation requirements — granular per-category consent, human-in-the-loop for every money-moving action, immutable audit logging, and a hard-constraint suitability layer the LLM cannot override. This is deliberately positioned as a first-class section, not an afterthought, since it's one of the six dimensions the SBI jury panel scores against.

**Where this proposal is strongest relative to a likely competitive field:** most submissions in this hackathon will treat "Agentic AI" as a single smarter chatbot serving Pillar 2 (Digital Adoption) alone. This proposal's differentiation is building genuine Pillar 3 (Digital Engagement) — memory, multi-agent collaboration, and behavior-based life-event inference — which is structurally harder to fake with a single LLM prompt and is the part of the brief most likely to separate finalists from the rest of the field.

---

## 3. The Problem, Quantified

Banking apps today are used almost exclusively for utility tasks — balance checks, transfers, UPI. Industry data consistently shows that a large majority of retail banking app sessions never touch an investment, insurance, or savings-goal feature, even though these are the products that drive both customer lifetime value and lock-in.

This isn't a UX problem — it's an **initiative problem**. The app is reactive by design: it answers what you ask, but never tells you what you didn't know to ask. The result is a structural gap between the services a bank *offers* and the services a customer *uses*, and that gap is where competitors (fintech apps, robo-advisors, neobanks) win the customer's attention.

**The opportunity:** be the first major Indian PSU bank to close that gap with an agentic system that acts, not just answers — while staying firmly inside RBI's consent and audit expectations for AI in BFSI.

---

## 4. Why "Agentic," Not "Chatbot" — and Why That Distinction Matters to Judges

A chatbot is a single model responding to a single query in a single turn. What we're proposing is different on three axes:

1. **Autonomy of perception** — the system detects financial *events* without being asked (salary credit, bill due, utilization spike).
2. **Decomposed reasoning** — specialized agents (spending, goals, credit, investment, bills) each reason over their domain and pass structured outputs to an orchestrator, rather than one model trying to do everything in one prompt.
3. **Bounded autonomous action** — the system can *act* (schedule a payment, initiate a SIP) through SBI's APIs, gated by human-in-the-loop approval — this is what separates "agentic" from "generative."

```
                       Salary Credited (Event)
                              │
                              ▼
                    Event Detection Agent
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                      ▼
  Spending Agent      Goal Planning Agent       Credit Agent
        │                     │                      │
        └─────────────────────┼──────────────────────┘
                              ▼
                  Recommendation Generator
                   (ranks, dedupes, explains)
                              │
                              ▼
                 Human-in-the-Loop Approval
                   (one-tap accept / edit / reject)
                              │
                              ▼
                    Execute via SBI Sandbox APIs
                              │
                              ▼
                  Audit Log + Outcome Feedback
                   (feeds back into agent learning)
```

---

## 5. Illustrative Scenario

**Status quo**

> ₹62,000 credited.

Nothing else happens.

**With Smart Financial Coach**

> Your salary of ₹62,000 has been credited.
>
> Based on your last six months:
> - Average monthly expenses: ₹38,000
> - Expected utility bills this month: ₹7,200
> - You can safely set aside ₹10,000 while keeping your emergency buffer intact.
>
> I'd suggest:
> ✅ Invest ₹10,000 in an SBI Mutual Fund SIP
> ✅ Move ₹5,000 into your Emergency Fund goal
> ✅ Schedule your electricity bill (due in 4 days)
>
> **[Approve All] [Customize] [Not Now]**

The customer taps once. Every action remains reversible and fully logged.

---

## 6. Core Agents

| Agent | Purpose | Example Output |
|---|---|---|
| **Spending Analysis** | Categorizes transactions, flags anomalies, detects subscriptions, forecasts monthly spend | "You spent 28% more on food this month than your 6-month average." |
| **Goal Planning** | Translates a stated goal (bike, education, home, retirement) into a savings/investment plan | "Saving ₹4,500/month gets you to your laptop goal in 9 months." |
| **Investment Recommendation** | Matches risk profile, age, income, and goals to FD/RD/Mutual Fund/SIP/G-Sec options, explained in plain language before any action | "Given your moderate risk profile, a balanced hybrid SIP fits better than a pure equity fund." |
| **Credit Health** | Tracks EMI payments, card utilization, repayment history | "Your card utilization just hit 82%. Paying down ₹15,000 would bring it under 30% and likely help your score." |
| **Bill Reminder** | Detects recurring payments (electricity, mobile, insurance, EMI) and offers to schedule them | "Your DTH recharge is due in 2 days — shall I pay it from your linked account?" |

An **Orchestrator** sits above these agents: it routes events, resolves conflicting recommendations (e.g., "invest more" vs. "pay down credit card first" both firing at once), ranks by urgency and financial benefit, and ensures the customer is never shown more than 2–3 actions at once to avoid recommendation fatigue.

---

## 7. Event-Driven Intelligence

| Event | Agent Response |
|---|---|
| Salary credited | Recommend savings allocation + investment |
| Unusually large expense | Flag and adjust monthly budget forecast |
| Bill approaching due date | Remind, offer to auto-schedule |
| Credit utilization rises | Suggest repayment strategy |
| Savings rate drops | Recommend specific expense categories to trim |
| FD/RD matures | Recommend reinvestment options, compare rates |
| Goal milestone reached/missed | Recalculate timeline, suggest adjustment |

---

## 8. Persistent Customer Memory — From Recommendations to Real Coaching

A one-off recommendation is a tip. A recommendation informed by everything the system has learned about you over months is *coaching*. With explicit, revocable consent, the system maintains a long-term financial memory per customer, separate from any single session:

- Active financial goals and progress toward them
- Income trend and seasonality
- Spending habits and category drift
- Investment preferences and stated risk tolerance
- Recommendations the customer has previously rejected (so the system stops repeating ignored advice)
- Recurring commitments and seasonal spending patterns (e.g., higher December spend)

**Example — the same goal, two different moments:**

> **January:** "I want to save ₹5 lakh for higher education."
>
> **April:** "You're 42% toward your education goal. Increasing your SIP by ₹500/month would get you there two months earlier."

This is what separates a financial *coach* from a financial *chatbot* — the system's advice compounds in value over the relationship, which is also what makes it a retention lever rather than a one-time engagement gimmick.

---

## 9. Collaborative Multi-Agent Reasoning (Not Just Parallel Agents)

In the base architecture, agents reason independently and an orchestrator ranks their outputs. The stronger version has agents **share observations and resolve conflicts before** a recommendation is generated — because agents pulling in different directions at once is a realistic and important failure mode to design for.

**Example conflict, resolved before the customer ever sees it:**

| Agent | Observation |
|---|---|
| Spending | ₹20,000 surplus this month |
| Investment | Recommends ₹15,000 into SIP |
| Credit Health | Card utilization at 92% — high-priority concern |
| Goal Planning | Emergency fund is below target |

**Conflict Resolution Agent output (single consolidated recommendation):**
- ₹10,000 → Credit card repayment (highest financial-harm-avoidance priority)
- ₹5,000 → Emergency fund top-up
- ₹5,000 → SIP

The customer sees one coherent, prioritized suggestion — not four competing notifications. This is a meaningfully harder (and more honest) version of "multi-agent" than agents simply running in parallel.

---

## 10. Adaptive Learning Engine

Every approval, rejection, edit, or delay is feedback, not just a logged event — it should change future behavior, within the same suitability guardrails described in Section 13.

| Customer behavior | System adapts by |
|---|---|
| Repeatedly rejects high-risk mutual funds | Shifts future suggestions toward FDs, debt funds, government bonds |
| Always pays bills 3 days early | Moves reminder timing earlier automatically |
| Consistently overspends every December | Pre-emptively adjusts savings recommendations ahead of the season |

This learning loop is what keeps recommendations from going stale — and what gives SBI a defensible reason the assistant gets *more* useful the longer a customer stays, directly supporting the retention goal in Section 1.

---

## 11. Financial Health Score Dashboard

A single, glanceable score gives customers (and the bank) a snapshot of overall financial wellness, recalculated after every major event:

```
Financial Health Score:  82 / 100

Income Stability       ✔
Savings                ✔
Emergency Fund         ✔
Investments            ⚠
Insurance              ⚠
Credit Utilization     ⚠
```

This doubles as a cross-sell surface: a low "Insurance" or "Investments" sub-score is a natural, non-pushy entry point into a recommendation, and as a retention surface: customers have a reason to open the app even when they have no specific task.

---

## 12. Life-Event Detection

Major life events are usually visible in transaction patterns before a customer ever tells the bank about them. The system infers *candidate* life events (never asserts them with false confidence) and offers relevant products contextually:

| Detected pattern | Possible life event | Contextual offer |
|---|---|---|
| Wedding-related vendor payments cluster | Marriage | Joint account, family insurance, long-term savings plan |
| Large one-time deposit + new EMI | Home purchase | Home loan top-up, insurance bundling |
| Recurring tuition/fee payments begin | Education expense | Education loan, fee-linked savings goal |

This is framed deliberately as a *possible* inference with a low-friction confirmation step — never an unprompted assumption stated as fact, which matters both for trust and for avoiding incorrect, presumptive messaging.

---

## 13. Smart Contextual Nudges & Explainable AI

Generic banking nudges ("Open an FD") perform poorly because they carry no context. Every nudge from this system is grounded in the customer's own numbers:

> Instead of: *"Invest ₹10,000."*
>
> The system says: *"Your average monthly expenses are ₹38,000. Your emergency fund already covers 2.8 months of expenses, so investing ₹10,000 now won't affect your liquidity."*

This explainability isn't just good UX — it's the same mechanism referenced in the compliance section below: every action is traceable to the numbers that justified it, which is what regulators and skeptical customers both need to trust an autonomous recommendation.

---

## 14. Responsible-AI & Compliance Guardrails

For a banking-sector judge panel, this section matters as much as the AI architecture — it shows the idea is bankable, not just buildable.

- **Explicit, granular consent**: customers opt in per data category (transactions, credit bureau pull, investment holdings) — not one blanket toggle.
- **Human-in-the-loop for every money-moving action**: the system *never* executes a transaction, investment, or payment without explicit per-action approval. It can only *prepare* and *suggest*.
- **Explainability by design**: every recommendation surfaces the underlying numbers (the "why"), not just the action — required for RBI's fair-practice and algorithmic-transparency expectations.
- **Full audit trail**: every agent decision, recommendation, and approval/rejection is logged immutably for regulatory review and model-behavior debugging.
- **Reversibility**: scheduled actions (bill payments, SIP starts) include a cancellation window before execution.
- **Bias & suitability checks**: investment recommendations are constrained by a rules-based suitability layer (KYC risk category, age, income band) that the LLM cannot override — the LLM explains and personalizes language, it does not decide eligibility.
- **Data residency & model boundary**: customer financial data is processed within SBI's controlled environment; no raw PII is sent to a third-party hosted LLM without anonymization/tokenization.

---

## 15. Technical Architecture

```
                         React Frontend
                    (Web / Android / iOS)
                               │
                               ▼
                       FastAPI Backend
                               │
                               ▼
                  LangGraph Orchestrator
                               │
        ┌──────────────┬───────┴───────┬──────────────┐
        ▼              ▼               ▼              ▼
 Spending Agent   Goal Agent     Credit Agent   Life-Event Agent
        │              │               │              │
        └──────────────┴───────┬───────┴──────────────┘
                                ▼
                  Conflict Resolution Agent
                                │
                                ▼
               Recommendation Ranking Engine
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
     Customer Memory Database          RAG Knowledge Base
     (goals, preferences, history)   (product T&Cs, rates, RBI rules)
                └───────────────┬───────────────┘
                                ▼
                       LLM (GPT / Llama 3)
                                │
                                ▼
                   Suitability Rules Engine
                     (hard constraints layer)
                                │
                                ▼
                     Human-in-the-Loop Approval
                                │
                                ▼
                      SBI Sandbox APIs
                                │
                                ▼
                       Banking Services
                                │
                                ▼
                  Update Customer Memory + Audit Log
```

### Technology Stack

| Layer | Technology |
|---|---|
| Frontend | React (Web, Android, iOS via shared component layer) |
| Backend | FastAPI |
| AI Orchestration | LangGraph |
| LLM | GPT / Llama 3 (swappable; on-prem option for data residency) |
| Knowledge Base | RAG + Vector Database |
| Database | PostgreSQL (transactional) + Redis (event/session state) |
| ML Models | Spending forecasting, transaction categorization, anomaly detection |
| Auth | OAuth 2.0 + JWT |
| Banking Integration | SBI Sandbox APIs |
| Deployment | Docker + Kubernetes |
| Observability | Structured audit logging, agent decision tracing |

---

## 16. What We'd Actually Build in the Hackathon Window (MVP Scope)

Judges weigh feasibility heavily — being explicit about scope shows engineering maturity.

**In scope for the demo:**
- 2–3 agents fully working end-to-end on the SBI Sandbox API: **Spending Analysis**, **Bill Reminder**, and either **Goal Planning** or **Credit Health**.
- A working (if simplified) **Conflict Resolution Agent** — even a basic priority rule (debt repayment > goal funding > discretionary investment) demonstrates the collaborative-reasoning concept without a full multi-agent negotiation protocol.
- A minimal **persistent memory store** (e.g., a simple keyed store of goals + rejected recommendations) to demonstrate the "remembers you" behavior across two simulated sessions — this doesn't need full long-term learning to make the point convincingly.
- LangGraph orchestrator with a working approval gate (mocked push notification → approve/reject → mock execution call).
- One realistic seeded dataset (synthetic transaction history) driving a live "salary credited" demo scenario end-to-end.
- A simple audit log view showing every agent decision and its outcome.

**Explicitly out of scope for the demo (roadmap only):**
- Full investment-grade suitability engine (would show a simplified rules stub).
- Full adaptive learning model (would show a rules-based stand-in: "3 rejections of category X → stop suggesting X").
- Life-event detection and the financial digital twin (described qualitatively in this proposal, not built for the demo).
- Voice/multilingual interface.
- Production-grade fraud detection.

Being upfront about this split signals to judges that the team understands the difference between a hackathon demo and a production system — and that the architecture is designed to scale into the full vision without rework.

---

## 17. Example End-to-End User Journey

**Morning — salary credited**

1. Event Detection Agent fires on the credit.
2. Spending Agent updates the monthly budget model.
3. Goal Planning Agent recalculates progress on active goals.
4. Investment Agent computes safely investable surplus.
5. Bill Reminder Agent surfaces upcoming dues.
6. Orchestrator merges and ranks these into a single, uncluttered card:

> Welcome back! Based on your latest activity:
> - Save ₹5,000 toward your Emergency Fund
> - Invest ₹10,000 in an SBI Mutual Fund SIP
> - Electricity bill due in 2 days
> - Credit card payment due next week
>
> Review and approve only what you'd like.

7. Customer approves selectively; every other suggestion is dismissed with one tap and logged for model feedback (did they ignore it because it was wrong, or just not now?).

---

## 18. Customer Acquisition & Digital Adoption Impact

**Acquisition**
- Personalized onboarding nudges convert new-to-bank customers into SIP/RD/insurance holders within their first 30–60 days, rather than leaving cross-sell to branch staff or generic push notifications.
- Personalized guidance increases trust signals that matter for word-of-mouth acquisition in a market where most new banking relationships still come from referral.

**Digital adoption**
- Teaches customers how to use UPI, SIPs, bill-pay, and investment features *in context*, rather than via a separate tutorial nobody opens.
- Surfaces underused SBI digital features exactly when they're relevant, not as generic promotional banners.

---

---

## 19. Competitive Comparison

| Dimension | Traditional Banking Apps | SBI Smart Financial Coach |
|---|---|---|
| Interaction model | Reactive | Proactive |
| Recommendations | Generic | Personalized, explained |
| Underlying logic | Rule-based | Multi-agent AI with collaborative reasoning |
| Memory | None (session-only) | Persistent, consented, long-term |
| Product discovery | Manual browsing | AI-surfaced at the relevant moment |
| Learning | Static | Continuous, behavior-adapted |
| Decision-making | Single rule engine | Collaborative agents + conflict resolution |
| Financial coaching | Not offered | Core feature |

---

## 20. Expected Business Impact

Rather than presenting fabricated baseline-to-target numbers (which invite an easy "where did these come from?" from judges), we frame impact directionally, tied to the specific mechanism that drives it — this is more credible and more defensible in Q&A.

| KPI | Direction of Impact | Why (the mechanism, not a guess) |
|---|---|---|
| Investment & insurance product adoption | ↑ | Recommendations appear at the moment of demonstrated surplus or need, not as generic catalog browsing |
| Digital feature usage breadth (SIP, bill-pay, etc.) | ↑ | In-context teaching replaces unused tutorials — customers act where they already are |
| Session frequency / engagement | ↑ | The app gives customers a reason to open it even without a specific task (health score, goal progress) |
| Retention | ↑ | Persistent memory means switching banks means losing a coaching relationship, not just an account |
| Cross-sell conversion | ↑ | Suggestions are explained with the customer's own numbers, which converts better than blanket promotions |
| Late payment / credit utilization incidents | ↓ | Bill and credit-health agents intervene before the deadline, not after |

**If the brief or judges want hard numbers:** the credible path is to commit to **measuring these via a pilot** (e.g., a 90-day cohort test comparing app behavior with vs. without the assistant enabled) rather than presenting invented figures now. Proposing the *measurement plan* itself is a strong signal of product maturity — it shows the team knows the difference between a hackathon pitch and a real business case.

---

## 21. Future Roadmap (Post-Hackathon)

- Voice-enabled, multilingual financial assistant (critical for Bharat-scale adoption).
- AI-assisted fraud detection layered onto the same event stream.
- Family/joint financial management view.
- Tax-optimization recommendations timed to the fiscal year.
- Personalized insurance gap analysis.
- ESG/sustainable investment recommendations.
- Wearable integration for spend alerts (consent-gated).
- **Financial Digital Twin** — a simulation layer customers can query directly: *"What if I increase my SIP by ₹2,000?"*, *"What if I buy a ₹12 lakh car?"*, *"What if I lose my job for three months?"* — projecting the impact on savings goals, emergency fund runway, loan eligibility, and retirement timeline before the customer commits to a real decision. This is the natural long-term endpoint of the persistent-memory and multi-agent reasoning work in Sections 8–10: once the system already models a customer's full financial picture, simulating hypothetical futures is a logical extension rather than a new system.


**One-sentence pitch for judges:** *Smart Financial Coach replaces "ask and we'll answer" with "we noticed, here's why, approve if you agree" — and because it remembers you, it gets better at being your financial coach every month it runs.*
