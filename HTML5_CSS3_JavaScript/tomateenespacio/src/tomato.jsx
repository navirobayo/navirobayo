export function Tomato({ position }) {
  const tomatoStyle = {
    backgroundColor: 'red',
    borderRadius: '50%',
    width: '30px',
    height: '30px',
    position: 'absolute',
    left: position.x,
    top: position.y,
    transition: 'left 0.10s ease, top 0.10s ease', // Add transitions for left and top
  };

  return <div style={tomatoStyle}></div>;
}

  