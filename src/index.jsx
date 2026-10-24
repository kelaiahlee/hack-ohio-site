import React from "react";
import ReactDOM from "react-dom/client"; // 1. Note the "/client" path
import App from "./components/App";

// 2. Create the root first, then render your component
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />); 