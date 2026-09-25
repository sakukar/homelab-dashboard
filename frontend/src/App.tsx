import './App.css'

const metrics = ['CPU usage', 'Memory usage', 'Disk usage', 'Load average']

function App() {
  return (
    <main className="dashboard">
      <header className="dashboard-header">
        <div>
          <p className="eyebrow">HOME LAB / OVERVIEW</p>
          <h1>HomeLab Dashboard</h1>
          <p>Your infrastructure at a glance.</p>
        </div>
        <span className="connection-status">Awaiting server data</span>
      </header>

      <section aria-labelledby="metrics-heading">
        <h2 id="metrics-heading">Resource overview</h2>
        <div className="metrics">
          {metrics.map((metric) => (
            <article className="card" key={metric}>
              <h3>{metric}</h3>
              <p className="metric-value" aria-label="Unavailable">—</p>
              <p>No measurements yet</p>
            </article>
          ))}
        </div>
      </section>

      <section className="servers card" aria-labelledby="servers-heading">
        <h2 id="servers-heading">Servers</h2>
        <div className="empty-state">
          <h3>No servers connected</h3>
          <p>Server status and resource measurements will appear here once connected.</p>
        </div>
      </section>
    </main>
  )
}

export default App
