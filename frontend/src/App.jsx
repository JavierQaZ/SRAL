import React from "react";
import { Navigate, Route, Routes } from 'react-router-dom';
import Home from './views/Home.jsx';
import Login from "./views/Login.jsx";

function App() {
  return (
    <Routes>
      {/* Redirigir de la raíz a /home */}
      <Route path ="/" element={<Navigate to='login'/>}/>

      <Route path ="/login" element = {<Login/>} ></Route>

      {/* Definir la ruta /home */}
      <Route path ="/home/*" element={<Home />}/>

      {/* agregar rutas */}
    </Routes>
  );
};

export default App;