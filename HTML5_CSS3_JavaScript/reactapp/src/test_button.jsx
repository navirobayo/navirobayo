export function TestButton({realtimetext, realtimecolor, func, msg}) {

    return (
        <button onClick={() => func(msg)} style={{backgroundColor: realtimecolor}}>
            <p>{realtimetext}</p>
        </button>
    );
}
