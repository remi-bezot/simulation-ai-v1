import React, { useRef, useEffect } from "react";
import * as THREE from "three";
import WorldCard from "./WorldCard"; // Utilisé pour afficher des informations supplémentaires

const WorldList = ({ worlds }) => {
  const mountRef = useRef(null);

  useEffect(() => {
    // Configuration de la scène Three.js
    const scene = new THREE.Scene();

    // Configuration de la caméra
    const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
    camera.position.z = 5;

    // Configuration du renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(600, 400); // Taille fixe, ou dynamique si nécessaire
    mountRef.current.appendChild(renderer.domElement);

    // Ajout de lumière
    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(10, 10, 10);
    scene.add(light);

    // Ajout des mondes comme sphères
    const spheres = worlds.map((world, index) => {
      const geometry = new THREE.SphereGeometry(0.5, 32, 32);
      const material = new THREE.MeshStandardMaterial({
        color: world.color || 0x007bff,
      });
      const sphere = new THREE.Mesh(geometry, material);
      sphere.position.x = index * 2 - (worlds.length - 1); // Espacement des sphères
      scene.add(sphere);
      return sphere;
    });

    // Animation
    const animate = () => {
      requestAnimationFrame(animate);
      spheres.forEach((sphere) => (sphere.rotation.y += 0.01)); // Rotation des sphères
      renderer.render(scene, camera);
    };
    animate();

    // Nettoyage
    return () => {
      renderer.dispose();
      mountRef.current.removeChild(renderer.domElement);
    };
  }, [worlds]);

  return (
    <div>
      {/* Rendu Three.js */}
      <div ref={mountRef} style={{ marginBottom: "20px" }} />

      {/* Liste des informations des mondes */}
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}>
        {worlds.map((world) => (
          <WorldCard key={world.id} world={world} />
        ))}
      </div>
    </div>
  );
};

export default WorldList;
