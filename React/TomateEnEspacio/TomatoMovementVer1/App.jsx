import { useState, useEffect } from 'react';
import './App.css';
import { Tomato } from './tomato';
import { RingA } from './ring_a';
import { RingB } from './ring_b';

function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [moveDirection, setMoveDirection] = useState(null);
  const moveDistance = 15; // Adjust the movement speed as needed
  const moveInterval = 16; // Update the position every 16ms for smooth movement

  useEffect(() => {
    const handleKeyPress = (e) => {
      switch (e.key) {
        case 'ArrowLeft':
        case 'a':
        case 'A':
          setMoveDirection('left');
          break;
        case 'ArrowRight':
        case 'd':
        case 'D':
          setMoveDirection('right');
          break;
        case 'ArrowUp':
        case 'w':
        case 'W':
          setMoveDirection('up');
          break;
        case 'ArrowDown':
        case 's':
        case 'S':
          setMoveDirection('down');
          break;
        default:
          break;
      }
    };

    const handleKeyRelease = () => {
      setMoveDirection(null);
    };

    window.addEventListener('keydown', handleKeyPress);
    window.addEventListener('keyup', handleKeyRelease);

    return () => {
      window.removeEventListener('keydown', handleKeyPress);
      window.removeEventListener('keyup', handleKeyRelease);
    };
  }, []);

  useEffect(() => {
    let moveIntervalId;

    const moveTomato = () => {
      if (moveDirection === 'left') {
        setPosition((prevPosition) => ({
          ...prevPosition,
          x: prevPosition.x - moveDistance,
        }));
      } else if (moveDirection === 'right') {
        setPosition((prevPosition) => ({
          ...prevPosition,
          x: prevPosition.x + moveDistance,
        }));
      } else if (moveDirection === 'up') {
        setPosition((prevPosition) => ({
          ...prevPosition,
          y: prevPosition.y - moveDistance,
        }));
      } else if (moveDirection === 'down') {
        setPosition((prevPosition) => ({
          ...prevPosition,
          y: prevPosition.y + moveDistance,
        }));
      }
    };

    if (moveDirection) {
      moveIntervalId = setInterval(moveTomato, moveInterval);
    } else {
      clearInterval(moveIntervalId);
    }

    return () => {
      clearInterval(moveIntervalId);
    };
  }, [moveDirection]);

  return (
    <div className="App">
      <h1>Tomato in space</h1>
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          height: 'calc(100vh - 100px)',
          position: 'relative', // Add this for positioning the tomato
        }}
      >
        <RingA />
        
        <Tomato position={position} />
      </div>
      <div><RingB /></div>
    </div>
  );
}

export default App;
