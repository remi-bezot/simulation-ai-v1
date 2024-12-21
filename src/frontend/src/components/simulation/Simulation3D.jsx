import React, { useRef, useEffect } from "react";
import * as THREE from "three";

const Simulation3D = ({ data, getObject3D, animation }) => {
  const mountRef = useRef(null);

  useEffect(() => {
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, 1, 0.1, 1000);
    camera.position.z = 5;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(600, 400);
    mountRef.current.appendChild(renderer.domElement);

    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(10, 10, 10);
    scene.add(light);

    const objects = data.map((item, index) => {
      const object3D = getObject3D(item, index);
      scene.add(object3D);
      return object3D;
    });

    const animate = () => {
      requestAnimationFrame(animate);
      animation(objects);
      renderer.render(scene, camera);
    };
    animate();

    return () => {
      renderer.dispose();
      mountRef.current.removeChild(renderer.domElement);
    };
  }, [data, getObject3D, animation]);

  return <div ref={mountRef} />;
};

export default Simulation3D;
