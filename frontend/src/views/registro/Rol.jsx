import React, { useState } from 'react';
// import axios from "axios";

function Roles() {

    const [nombreRol, setNombreRol] = useState("")
    const [salarioRol, setSalarioRol] = useState("")
    const [exitoRegistrarRol, setExitoRegistrarRol] = useState("")

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
            //revisar nombres de la bdd
            "": nombreRol,
            "": salarioRol
        }
    }

    //axios

    return (
        <>
            <form onSubmit={handleSubmit}>
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
                    Registrar Rol
                </button>
                {exitoRegistrarRol}
            </form>
        </>
    )
}

export default Roles;