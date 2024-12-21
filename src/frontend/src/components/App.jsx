
import React from 'react';
import GlobalStyles from '../styles/globalStyles';
import Dashboard from './Dashboard';

function App() {
    return (
        <>
            <GlobalStyles />
            <div>
                <h1>Simulation Dashboard</h1>
                <Dashboard />
            </div>
        </>
    );
}

export default App;

