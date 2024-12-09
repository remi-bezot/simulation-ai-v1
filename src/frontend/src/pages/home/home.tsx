import React from "react";
import Header from "../../components/shared/Header"; // Chemin vers le composant Header
import Footer from "../../components/shared/Footer"; // Assurez-vous que Footer existe

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
