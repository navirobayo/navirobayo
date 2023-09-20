import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { TestButton } from './test_button'
import './App.css'

function App() {
  function testnotify (msg) {
    alert(msg)
}

  return (
    <>
      <TestButton realtimetext={"Hello1"} realtimecolor ={"red"} func={testnotify} msg={"what is up my g"}/>
      <TestButton realtimetext={"Hello2"} realtimecolor ={"green"}/>
      <TestButton realtimetext={"Hello3"} realtimecolor ={"yellow"}/>
    </>
  )
}

export default App
