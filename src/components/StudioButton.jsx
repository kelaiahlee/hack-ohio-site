import React from "react";
import { useState } from 'react'

function StudioButton(){
    return (
    <div className="studio-btn">
       <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                aria-hidden="true"
            >
                <path d="M12 4v16" />
                <path d="M4 12h16" />
        </svg>
        <p className="p1text">Studio</p>
    </div>
    );
}

export default StudioButton;