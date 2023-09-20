import { useState, useEffect } from 'react';
import './App.css';
import { Tomato } from './tomato';
import { RingA } from './ring_a';

function App() {
  const [position, setPosition] = useState({ x: 0, y: 0 });
  const [moveDirection, setMoveDirection] = useState(null);
  const [ringPosition, setRingPosition] = useState({ x: 0, y: 0 });
  const [ringMoveDirection, setRingMoveDirection] = useState(null);
  const [isColliding, setIsColliding] = useState(false);

  const moveDistance = 10; // Adjust the movement speed as needed
  const moveInterval = 8; // Update the position every 16ms for smooth movement
  const tomatoRadius = 15; // Set the radius of the tomato
  const ringRadius = 50; // Set the radius of the ring

  useEffect(() => {
    const handleKeyPress = (e) => {
      switch (e.key) {
        case 'a':
        case 'A':
          setMoveDirection('left');
          break;
        case 'd':
        case 'D':
          setMoveDirection('right');
          break;
        case 'w':
        case 'W':
          setMoveDirection('up');
          break;
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

  useEffect(() => {
    const handleRingKeyPress = (e) => {
      switch (e.key) {
        case 'ArrowLeft':
          setRingMoveDirection('left');
          break;
        case 'ArrowRight':
          setRingMoveDirection('right');
          break;
        case 'ArrowUp':
          setRingMoveDirection('up');
          break;
        case 'ArrowDown':
          setRingMoveDirection('down');
          break;
        default:
          break;
      }
    };

    const handleRingKeyRelease = () => {
      setRingMoveDirection(null);
    };

    window.addEventListener('keydown', handleRingKeyPress);
    window.addEventListener('keyup', handleRingKeyRelease);

    return () => {
      window.removeEventListener('keydown', handleRingKeyPress);
      window.removeEventListener('keyup', handleRingKeyRelease);
    };
  }, []);

  useEffect(() => {
    let ringMoveIntervalId;

    const moveRing = () => {
      if (ringMoveDirection === 'left') {
        setRingPosition((prevPosition) => ({
          ...prevPosition,
          x: prevPosition.x - moveDistance,
        }));
      } else if (ringMoveDirection === 'right') {
        setRingPosition((prevPosition) => ({
          ...prevPosition,
          x: prevPosition.x + moveDistance,
        }));
      } else if (ringMoveDirection === 'up') {
        setRingPosition((prevPosition) => ({
          ...prevPosition,
          y: prevPosition.y - moveDistance,
        }));
      } else if (ringMoveDirection === 'down') {
        setRingPosition((prevPosition) => ({
          ...prevPosition,
          y: prevPosition.y + moveDistance,
        }));
      }
    };

    if (ringMoveDirection) {
      ringMoveIntervalId = setInterval(moveRing, moveInterval);
    } else {
      clearInterval(ringMoveIntervalId);
    }

    return () => {
      clearInterval(ringMoveIntervalId);
    };
  }, [ringMoveDirection]);

  useEffect(() => {
    const handleResetKeyPress = (e) => {
      if (e.key === 'r' || e.key === 'R') {
        // Reset the positions to the left-top part of the screen
        setPosition({ x: 0, y: 0 });
        setRingPosition({ x: 0, y: 0 });
        setIsColliding(false);
      }
    };

    window.addEventListener('keydown', handleResetKeyPress);

    return () => {
      window.removeEventListener('keydown', handleResetKeyPress);
    };
  }, []);

  useEffect(() => {
    const tomatoCenterX = position.x + tomatoRadius;
    const tomatoCenterY = position.y + tomatoRadius;
    const ringCenterX = ringPosition.x + ringRadius;
    const ringCenterY = ringPosition.y + ringRadius;
    const distance = Math.sqrt(
      (tomatoCenterX - ringCenterX) ** 2 + (tomatoCenterY - ringCenterY) ** 2
    );

    if (distance < tomatoRadius + ringRadius) {
      setIsColliding(true);
    } else {
      setIsColliding(false);
    }
  }, [position, ringPosition]);

  return (
    <div className="App">
      <h1>Tomato in space</h1>
      <div
        style={{
          display: 'flex',
          justifyContent: 'center',
          alignItems: 'center',
          position: 'relative',
        }}
      >
        <RingA position={ringPosition} />
        <Tomato position={position} />
        {isColliding && (
          <div
            style={{
              position: 'absolute',
              top: '50%',
              left: '50%',
              transform: 'translate(-50%, -50%)',
              backgroundColor: 'red',
              color: 'white',
              padding: '10px',
              borderRadius: '5px',
            }}
          >
            Collision detected!
          </div>
        )}
      </div>
    </div>
  );
}

export default App;