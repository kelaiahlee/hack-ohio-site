import React from "react";
import { useState } from 'react'

function LibraryButton(){
    return (
    <div className="lib-btn">
        <svg
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                strokeWidth="2"
                strokeLinecap="round"
                strokeLinejoin="round"
                aria-hidden="true"
            >
                <path d="M4 4v16" />
                <path d="M10 4v16" />
                <path d="M16 6l4 12" />
        </svg>
        <p className="p1text">Gallery</p>
    </div>
    );
}

export default LibraryButton;