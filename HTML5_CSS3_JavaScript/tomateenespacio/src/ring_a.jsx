export function RingA({ position }) {
  const style = {
    position: 'absolute',
    width: '300px',
    height: '300px',
    borderRadius: '50%',
    border: '2px solid black',
    boxSizing: 'border-box',
    left: position.x,
    top: position.y,
    animation: 'pulsateA 3s infinite',
    transition: 'left 0.10s ease, top 0.10s ease',
  };

  return <div style={style}></div>;
}
