import React, { useState } from "react";
import axios from "axios";

function Roles() {

    const [nombreRol, setNombreRol] = useState("")
    const [salarioRol, setSalarioRol] = useState("")
    const [exitoEditarRol, setExitoEditarRol] = useState("")

    const handleOnChangeNombreRol = (e) => {
        console.log(e.target.value)
        setNombreRol(e.target.value)
    }

    const handleOnChangeSalarioRol = (e) => {
        console.log(e.target.value)
        setSalarioRol(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const nuevoRol = {
            "nombre_rol": nombreRol,
            "sueldoPorHora_rol": parseFloat(salarioRol)
        }

        axios.post('http://localhost:5000/rol/put', nuevoRol)
            .then((response) => {
                setExitoEditarRol("Rol editado exitosamente")
                console.log("Rol editado exitosamente", response.data)
            })
            .catch ((error) => {
                setExitoEditarRol("Error al editar el rol")
                console.error("Error al editar el rol: ", error)
            });
    }

    const ping = exitoEditarRol ? (
        <div className='mt-3'>
            <p>
                {exitoEditarRol}: <br/>
                {nombreRol}
            </p>
        </div>
    ): null;

    return (
        <>
            <form onSubmit={handleSubmit}>
                <h4>Editar Rol</h4>
                <div className='d-flex flex-column'>

                    <label className='form-label mt-3'>
                        Nombre del Rol
                        <input type="text" className='form-control'
                        value={nombreRol}
                        onChange={handleOnChangeNombreRol}
                        />
                    </label>

                    <label className='form-label mt-3'>
                        Salario del Rol (por hora)
                        <input type="text" className='form-control'
                        value={salarioRol}
                        onChange={handleOnChangeSalarioRol}
                        />
                    </label>
                </div>

                <button type="submit" className="btn btn-warning ms-4 mt-3 text-white">
                    Confirmar cambios
                </button>
                <br/>
                <br/>
                {ping}
            </form>
        </>
    )
}

export default Roles;