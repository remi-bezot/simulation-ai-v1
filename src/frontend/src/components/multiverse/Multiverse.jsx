import React, { useRef, useEffect } from "react";
import * as THREE from "three";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { Typography, Box } from "@mui/material";

const Multiverse = ({ dimensions, highlightedDimension, rotationSpeed = 1, onDimensionClick }) => {
  const defaultDimensions = [
    { name: "Dimension Alpha", color: 0xff4500 },
    { name: "Dimension Beta", color: 0x1e90ff },
    { name: "Dimension Gamma", color: 0x32cd32 },
  ];

  const dataToRender = dimensions && dimensions.length ? dimensions : defaultDimensions;
  const mountRef = useRef(null);

  useEffect(() => {
    if (!dataToRender.length) return;

    // Création de la scène
    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0xeeeeee);

    // Configuration de la caméra
    const camera = new THREE.PerspectiveCamera(75, mountRef.current.clientWidth / mountRef.current.clientHeight, 0.1, 1000);
    camera.position.z = 5;

    // Configuration du renderer
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(mountRef.current.clientWidth, mountRef.current.clientHeight);
    mountRef.current.appendChild(renderer.domElement);

    // Ajout d'OrbitControls pour interagir avec la caméra
    const controls = new OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxDistance = 20;
    controls.minDistance = 2;

    // Ajout de la lumière ambiante et ponctuelle
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
    scene.add(ambientLight);

    const pointLight = new THREE.PointLight(0xffffff, 1);
    pointLight.position.set(10, 10, 10);
    scene.add(pointLight);

    // Création des sphères
    const spheres = dataToRender.map((dimension, index) => {
      const geometry = new THREE.SphereGeometry(0.5, 32, 32);
      const material = new THREE.MeshStandardMaterial({
        color: dimension.color || 0x007bff,
        metalness: 0.5,
        roughness: 0.2,
      });
      const sphere = new THREE.Mesh(geometry, material);
      sphere.position.x = index * 2 - (dataToRender.length - 1);
      sphere.userData = dimension;
      scene.add(sphere);
      return sphere;
    });

    // Gestion des clics et des survols
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    const onMouseMove = (event) => {
      mouse.x = (event.clientX / mountRef.current.clientWidth) * 2 - 1;
      mouse.y = -(event.clientY / mountRef.current.clientHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(spheres);

      spheres.forEach((sphere) => {
        sphere.material.emissive.set(0x000000); // Réinitialise la surbrillance
      });

      intersects.forEach((intersect) => {
        intersect.object.material.emissive.set(0x444444); // Surbrillance sur survol
      });
    };

    const onMouseClick = (event) => {
      mouse.x = (event.clientX / mountRef.current.clientWidth) * 2 - 1;
      mouse.y = -(event.clientY / mountRef.current.clientHeight) * 2 + 1;

      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(spheres);

      if (intersects.length > 0) {
        const selectedSphere = intersects[0].object.userData;
        onDimensionClick && onDimensionClick(selectedSphere);

        // Zoom et centrage sur la sphère cliquée
        const targetPosition = intersects[0].object.position;
        camera.position.set(targetPosition.x, targetPosition.y, targetPosition.z + 3);
        camera.lookAt(targetPosition);
      }
    };

    mountRef.current.addEventListener("mousemove", onMouseMove);
    mountRef.current.addEventListener("click", onMouseClick);

    // Animation des sphères
    const animate = () => {
      requestAnimationFrame(animate);
      controls.update();

      spheres.forEach((sphere) => {
        sphere.rotation.y += 0.01 * rotationSpeed;

        // Animation de pulsation pour la dimension mise en évidence
        if (highlightedDimension && sphere.userData.name === highlightedDimension.name) {
          sphere.scale.set(1.2, 1.2, 1.2);
        } else {
          sphere.scale.set(1, 1, 1);
        }
      });

      renderer.render(scene, camera);
    };
    animate();

    // Nettoyage
    return () => {
      if (mountRef.current) {
        mountRef.current.removeEventListener("mousemove", onMouseMove);
        mountRef.current.removeEventListener("click", onMouseClick);
        mountRef.current.removeChild(renderer.domElement);
      }
    
      spheres.forEach((sphere) => scene.remove(sphere));
      scene.remove(pointLight);
      scene.remove(ambientLight);
      controls.dispose();
      renderer.dispose();
    };
    
  }, [dataToRender, rotationSpeed, highlightedDimension]);

  if (!dataToRender.length) {
    return (
      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        height="400px"
        bgcolor="#f9f9f9"
      >
        <Typography color="textSecondary">Aucune donnée à afficher.</Typography>
      </Box>
    );
  }

  return <div ref={mountRef} style={{ width: "100%", height: "400px" }} />;
};

export default Multiverse;
