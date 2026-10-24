import React from "react";
import { useState } from 'react'
import "./Page1desc.css";

function Page1desc() {
    return (
       <section className="hero">
            <p className="hero-eyebrow">
                <span className="eyebrow-line"></span>
                A SMALL INSTRUMENT FOR REMEMBERING
            </p>

            <h1 className="hero-title">
                Every picture
                <br />
                has <span className="italic-text">a sound.</span>
            </h1>

            <p className="hero-description">
                Bring a photograph. We’ll listen to its colors, its light, its little
                <br className="desktop-break" />
                details — and turn them into a melody only you can hear.
            </p>
        </section>
    );
}

export default Page1desc;