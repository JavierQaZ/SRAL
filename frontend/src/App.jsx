import React from "react";
import { Route, Routes } from 'react-router-dom';
import Home from './views/Home.jsx';

function App() {
  return (
    <Routes>
      {/* Redirigir de la raíz a /home */}
      <Route path ="*" element={<Home />}>
      </Route>

      {/* Definir la ruta /home */}
      <Route path ="/home" component={<Home />}/>

      {/* agregar rutas */}
    </Routes>
  );
};

export default App;