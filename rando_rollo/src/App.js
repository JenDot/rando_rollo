import React, { useState } from 'react'
import './App.css';

function App() {
  const [count, setCount] = useState(false)

  return (
    <div>
      {/* Click the btn to spin the wheel. */}
      <p><img className={`App-logo ${!!count ? "rotate" : ""}`} src="raffle_wheel.svg" /></p>
      <button onClick={() => setCount(true)}>Spin the wheel!</button>
      <button onClick={() => setCount(false)}>Stop the wheel!</button>
      {/* When the `spin` function completes, run  */}
    </div>
  )
}

export default App;
