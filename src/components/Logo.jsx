import React from "react";
import { useState } from 'react'

function Logo() {
    return (<div className="logo">
        <div className="syn-logo-icon">
            <svg
                    viewBox="0 0 48 48"
                    xmlns="http://www.w3.org/2000/svg"
                    aria-label="Synesthesia waveform"
                    role="img"
            >
                <path
                        d="M8 28 V20
                           C8 16 14 16 14 20
                           V34
                           C14 38 20 38 20 34
                           V12
                           C20 8 26 8 26 12
                           V36
                           C26 40 32 40 32 36
                           V18
                           C32 14 38 14 38 18
                           V27"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="3.2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                />
            </svg>
        </div>
        <h3 className="syn-logo-text">synesthesia.</h3>
    </div>);
}

export default Logo;