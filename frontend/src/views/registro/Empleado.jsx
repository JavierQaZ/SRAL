import React, {useState} from 'react';
// import axios from "axios";

function Empleado() {

    const [rut, setRut] = useState("")
    const [nombre, setNombre] = useState("")
    const [apellido1, setApellido1] = useState("")
    const [apellido2, setApellido2] = useState("")
    const [exitoRegistrarEmpleado, setExitoRegistrarEmpleado] = useState("")

    const handleOnChangeRut = (e) => {
        console.log(e.target.value)
        setRut(e.target.value)
    }

    const handleOnChangeNombre = (e) => {
        console.log(e.target.value)
        setNombre(e.target.value)
    }
    const handleOnChangeApellido1 = (e) => {
        console.log(e.target.value)
        setApellido1(e.target.value)
    }
    const handleOnChangeApellido2 = (e) => {
        console.log(e.target.value)
        setApellido2(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const nuevoEmpleado = {
            //revisar nombres de la bdd
            "": rut,
            "": nombre,
            "": apellido1,
            "": apellido2,
        }
    }

    //axios

    return (
        <>
            <form onSubmit={handleSubmit}>
                <div className='d-flex flex-column'>

                    <label className="form-label mt-3">
                        RUT
                        <input type="text" className="form-control"
                        value={rut}
                        onChange={handleOnChangeRut}
                        />
                    </label>

                    <label className="form-label mt-3">
                        Nombre
                        <input type="text" className="form-control"
                        value={nombre}
                        onChange={handleOnChangeNombre}
                        />
                    </label>

                    <label className="form-label mt-3">
                        Primer Apellido
                        <input type="text" className="form-control"
                        value={apellido1}
                        onChange={handleOnChangeApellido1}
                        />
                    </label>

                    <label className="form-label mt-3">
                        Segundo Apellido
                        <input type="text" className="form-control"
                        value={apellido2}
                        onChange={handleOnChangeApellido2}
                        />
                    </label>

                    <label className='form-label mt-3'>
                        Rol
                        <br/>
                        <select
                            className='custom-select'
                            id='inlineFormCustomSelectPref'
                            defaultValue='-1'
                        >

                            <option value='-1'>SELECT</option>
                            <option value='1'> ROL1</option>
                            <option value='2'> ROL2</option>
                            <option value='3'> ROL3</option>
                        </select>
                    </label>
                </div>

                <button type="submit" className="btn btn-warning ms-4 mt-3 text-white">
                    Registrar Empleado
                </button>
                {exitoRegistrarEmpleado}
            </form>
        </>
    )
}

export default Empleado;
