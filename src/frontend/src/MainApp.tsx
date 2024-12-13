import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "src/pages/home/home";

const MainApp: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
};

export default MainApp;
