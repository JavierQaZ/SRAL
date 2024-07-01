import React, { useState, useEffect } from "react";
import axios from "axios";

function Roles() {
    const [rol, setRol] = useState("-1") //rol a borrar
    const [roles, setRoles] = useState([]) //roles backend
    const [exitoBorrarRol, setExitoBorrarRol] = useState("");

    useEffect(() => {
        axios.get('http://localhost:5000/rol/get')
            .then((response) => {
                setRoles(response.data)
            })
            .catch((error) => {
                console.error("Error al obtemer los roles: ", error);
            })
    }, []);
    const handleOnChangeRol = (e) => {
        console.log(e.target.value)
        setRol(e.targey.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        /* verificar PK roles */
        axios.delete('http:localhost:5000/roles/delete/${codigo_rol}')
        .then((response) => {
            setExitoBorrarRol("Rol borrado exitosamente")
            console.log("Rol borrado exitosamente", response.data)
        })
        .catch ((error) => {
            setExitoBorrarRol("Error al borrar el Rol")
            console.error("Error al borrar el Rol", error)
        });
    }
        const ping = exitoBorrarRol ? (
            <div className='mt-3'>
                <p>
                    {exitoBorrarRol}: <br/>
                    {rol}
                </p>
            </div>
        ): null;

    return(
        <>
            <form onSubmit={handleSubmit}>
                <div className='d-flex flex-column'>
                    <h4>Borrar Rol</h4>
                    <label className='form-label mt-3'>
                        Rol
                        <br/>
                        <select
                            className='custom-select'
                            id='inlineFormCustomSelectPref'
                            value={rol}
                            onChange={handleOnChangeRol}
                        >
                            <option value='-1'>Seleccione el Rol</option>
                            {roles.map((rol) => (
                                <option key={rol.codigo_rol} value={rol.codigo_rol}>{rol.nombre_rol}</option>
                            ))}
                        </select>
                    </label>
                </div>
                <button type="submit" className="btn btn-warning ms-4 mt-3 text-white">
                    Borrar Rol
                </button>
                <br/>
                <br/>
                {ping}
            </form>
        </>
    )
}

export default Roles;