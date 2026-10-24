import React from 'react';
import { useState } from 'react';
import TitleCase from './TitleCase';
import Navbar from './Navbar';
import Page1desc from "./Page1desc";


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