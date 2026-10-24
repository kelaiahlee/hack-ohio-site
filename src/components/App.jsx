import React from 'react';
import { useState } from 'react';
import TitleCase from './TitleCase';
import Navbar from './Navbar';


function App() {
    return (
    <div>
        <TitleCase />
        <Navbar />
        <Page1desc />
    </div>
    );
}

export default App;