import React from "react";
import { Routes, Route, Link, Navigate } from "react-router-dom";

import "../styles/Sidebar.css";
import "../styles/Content.css";

import RegistroInicio from "./RegistroInicio.jsx";
import RegistroSalida from "./RegistroSalida.jsx";
import VisualizacionDatos from "./VisualizacionDatos.jsx";
import Registro from "./Registro.jsx";
import Gestion from "./Gestion.jsx";

function Home(){
    return(
        <div>
            <div className="container-fluid p-0 overflow-hidden">
                <div className="row">
                    <div className="sidebar col-auto col-sm-4 col-md-3 col-lg-3 col-xl-2 flex-column bg-mint min-vh-100 d-flex justify-content-between ">
                        <div className="d-flex flex-column m-1" id="sidebar-container">
                            <Link to=""className="d-inline-flex p-2" id="side-item-brand">
                                <img
                                src="/vite.svg" /* reemplazar con ícono real */
                                alt="logo "
                                width="40px"
                                height="40px"
                                />
                                <h5 className="ms-2 mt-3">SRAL</h5>
                            </Link>
                            <Link to="registroInicio" className="side-item">
                                Registro Inicio
                            </Link>
                            <Link to="registroSalida" className="side-item">
                                Registro Salida
                            </Link>
                            <Link to="visualizacionDatos" className="side-item">
                                Visualización
                            </Link>
                            <Link to="registro" className="side-item">
                                Registro
                            </Link>
                            <Link to="gestion" className="side-item">
                                Gestión
                            </Link>
                        </div>
                    </div>

                    <main className="col-auto col-sm-9 col-md-9 col-lg-9 col-xl-10 content ps-0">
                        <Routes>
                            /* añadir rutas */
                            <Route path="/registroInicio" element={<RegistroInicio/>}></Route>
                            <Route path="/registroSalida" element={<RegistroSalida/>}></Route>
                            <Route path="/visualizacionDatos" element={<VisualizacionDatos/>}></Route>
                            <Route path="/registro/*" element={<Registro/>}></Route>
                            <Route path="/gestion" element={<Gestion/>}></Route>
                        </Routes>
                    </main>
                </div>
            </div>
        </div>
    )
}

export default Home;