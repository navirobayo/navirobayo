// Not used at the moment. 

export function Field() {
    const squares = [];

    // Create 10 rows of 10 squares each
    for (let i = 0; i < 10; i++) {
        const row = [];

        for (let j = 0; j < 10; j++) {
            // Alternate between white and gray squares
            const color = (i + j) % 2 === 0 ? 'white' : 'gray';
            const square = <div key={`${i}-${j}`} style={{ backgroundColor: color }} className="square"></div>;
            row.push(square);
        }

        squares.push(<div key={i} className="row">{row}</div>);
    }

    return (
        <div className="reticule">
            {squares}
        </div>
    );
}
