
import React, { useEffect, useState } from 'react';

function App() {
    const [worlds, setWorlds] = useState([]);

    useEffect(() => {
        fetch('/worlds/')
            .then((response) => response.json())
            .then((data) => setWorlds(data.worlds));
    }, []);

    return (
        <div>
            <h1>Simulation Dashboard</h1>
            <ul>
                {worlds.map((world) => (
                    <li key={world.id}>{world.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default App;

