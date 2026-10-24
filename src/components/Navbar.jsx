import React from "react";
import { useState } from 'react';
import Logo from "./Logo";
import StudioButton from "./StudioButton";
import LibraryButton from "./LibraryButton";

function Navbar() {
    return (
    <div className="nav-bar">
        <Logo/>
        <div className="nav-actions">
            <StudioButton />
            <LibraryButton />
        </div>
    </div>
    );
}

export default Navbar;

