import React from "react";
import Header from "src/components/shared/Header"; // Utilisation de l'alias
import Footer from "src/components/shared/Footer"; // Utilisation de l'alias

const Home: React.FC = () => {
  return (
    <div>
      <Header />
      <main>
        <h1>Welcome to the Home Page!</h1>
        <p>This is the home page of your app.</p>
      </main>
      <Footer />
    </div>
  );
};

export default Home;
