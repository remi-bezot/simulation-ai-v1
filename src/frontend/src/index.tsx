import React from "react";
import ReactDOM from "react-dom/client";
import MainApp from "src/App";
import "src/index.css"; // Utilisation de l'alias

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);
root.render(
  <React.StrictMode>
    <MainApp />
  </React.StrictMode>
);
