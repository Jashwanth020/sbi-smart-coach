import { useState, useEffect } from 'react'
import './index.css'

function App() {
  const [healthScore, setHealthScore] = useState(null)
  const [nudges, setNudges] = useState([])
  const [auditLogs, setAuditLogs] = useState([])
  const [loading, setLoading] = useState(false)
  const [selectedEvent, setSelectedEvent] = useState('Salary Credited')

  const API_URL = 'http://localhost:8000'

  const bankingEvents = [
    { id: 'Salary Credited', amount: 62000, desc: 'Monthly salary from Employer' },
    { id: 'FD Maturing Soon', amount: 150000, desc: '1-Year Term Deposit maturing in 7 days' },
    { id: 'Upcoming EMI Shortfall', amount: 25000, desc: 'Home Loan EMI due in 3 days, insufficient balance' },
    { id: 'Large Unusual Inflow', amount: 300000, desc: 'Annual performance bonus credited' },
    { id: 'High Credit Card Utilization', amount: 85000, desc: 'Credit card utilized at 85% of limit' },
    { id: 'Sustained High Idle Balances', amount: 450000, desc: 'High balance maintained for over 3 months' },
    { id: 'Missing Salary', amount: 0, desc: 'Expected monthly salary not credited' },
    { id: 'First-Time International Travel', amount: 45000, desc: 'Transaction on international airline portal' }
  ]

  useEffect(() => {
    fetchHealthScore()
    fetchAuditLogs()
  }, [])

  const fetchHealthScore = async () => {
    try {
      const res = await fetch(`${API_URL}/health_score`)
      const data = await res.json()
      setHealthScore(data)
    } catch (e) {
      console.error(e)
    }
  }

  const fetchAuditLogs = async () => {
    try {
      const res = await fetch(`${API_URL}/audit_logs`)
      const data = await res.json()
      setAuditLogs(data)
    } catch (e) {
      console.error(e)
    }
  }

  const triggerEvent = async () => {
    setLoading(true)
    const eventConfig = bankingEvents.find(e => e.id === selectedEvent)
    
    try {
      const res = await fetch(`${API_URL}/trigger_event`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          event_type: eventConfig.id,
          amount: eventConfig.amount,
          description: eventConfig.desc
        })
      })
      const data = await res.json()
      setNudges(data.recommendations)
      fetchAuditLogs()
    } catch (e) {
      console.error(e)
    }
    setLoading(false)
  }

  const handleAction = async (id, action) => {
    try {
      await fetch(`${API_URL}/respond_to_nudge`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          recommendation_id: id,
          action: action
        })
      })
      setNudges(nudges.filter(n => n.id !== id))
      fetchAuditLogs()
    } catch (e) {
      console.error(e)
    }
  }

  return (
    <div className="app-container">
      <header className="header">
        <div className="logo">
          <span className="logo-icon">●</span>
          SBI Smart Coach
        </div>
      </header>

      <div className="left-panel">
        <div className="glass-card health-score">
          <h2>Financial Health</h2>
          {healthScore ? (
            <>
              <div className="score-circle">
                <h1>{healthScore.score}</h1>
                <span>/ 100</span>
              </div>
              <div className="health-metrics">
                <div className="metric">
                  <span>Income Stability</span>
                  <div className="status-indicator">
                    <div className={`dot ${healthScore.income_stability ? 'good' : 'warning'}`}></div>
                  </div>
                </div>
                <div className="metric">
                  <span>Emergency Fund</span>
                  <div className="status-indicator">
                    <div className={`dot ${healthScore.emergency_fund ? 'good' : 'warning'}`}></div>
                  </div>
                </div>
                <div className="metric">
                  <span>Investments</span>
                  <div className="status-indicator">
                    <div className={`dot ${healthScore.investments ? 'good' : 'warning'}`}></div>
                  </div>
                </div>
              </div>
            </>
          ) : (
            <p>Loading...</p>
          )}
        </div>

        <div className="glass-card demo-trigger" style={{ marginTop: '2rem' }}>
          <h3>Demo Simulation</h3>
          <p style={{ marginBottom: '1rem', fontSize: '0.9rem', color: 'var(--text-secondary)' }}>
            Trigger an event to watch the AI orchestrator generate personalized nudges.
          </p>
          
          <select 
            value={selectedEvent} 
            onChange={(e) => setSelectedEvent(e.target.value)}
            style={{ 
              width: '100%', 
              padding: '0.8rem', 
              marginBottom: '1rem',
              borderRadius: '8px',
              border: '1px solid rgba(255,255,255,0.2)',
              backgroundColor: 'rgba(0,0,0,0.2)',
              color: 'white',
              fontFamily: 'inherit'
            }}
          >
            {bankingEvents.map(evt => (
              <option key={evt.id} value={evt.id}>{evt.id}</option>
            ))}
          </select>

          <button className="btn-primary" onClick={triggerEvent} disabled={loading} style={{ width: '100%' }}>
            {loading ? 'Analyzing Event...' : `Trigger: ${selectedEvent}`}
          </button>
        </div>
      </div>

      <div className="right-panel">
        <div className="glass-card" style={{ marginBottom: '2rem' }}>
          <h2>Smart Nudges</h2>
          {nudges.length === 0 ? (
            <p style={{ color: 'var(--text-secondary)', textAlign: 'center', padding: '2rem 0' }}>
              No active nudges. Trigger an event to see the agents in action.
            </p>
          ) : (
            <div className="nudge-list">
              {nudges.map((nudge) => (
                <div key={nudge.id} className={`glass-card nudge-card ${nudge.category.toLowerCase()}`}>
                  <div className="nudge-header">
                    <span className="nudge-category">{nudge.category}</span>
                  </div>
                  <div className="nudge-title">{nudge.title}</div>
                  <div className="nudge-desc">{nudge.description}</div>
                  <div className="nudge-actions">
                    <button className="btn-primary" onClick={() => handleAction(nudge.id, 'APPROVE')}>
                      {nudge.action_text}
                    </button>
                    <button className="btn-secondary" onClick={() => handleAction(nudge.id, 'REJECT')}>
                      Dismiss
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        <div className="glass-card">
          <h2>Agent Audit Trail</h2>
          <div className="audit-list">
            {auditLogs.map((log) => (
              <div key={log.id} className="audit-item fade-in">
                <span className="audit-time">{log.timestamp.split(' ')[1]}</span>
                <strong>{log.event_type}</strong>: {log.details}
              </div>
            ))}
            {auditLogs.length === 0 && <p>No logs available.</p>}
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
