import React, {useState} from 'react';
import axios from "axios";

function Empleado() {

    const [rut, setRut] = useState("")
    const [nombre, setNombre] = useState("")
    const [apellidos, setApellidos] = useState("")
    const [exitoRegistrarEmpleado, setExitoRegistrarEmpleado] = useState("")

    const handleOnChangeRut = (e) => {
        console.log(e.target.value)
        setRut(e.target.value)
    }

    const handleOnChangeNombre = (e) => {
        console.log(e.target.value)
        setNombre(e.target.value)
    }
    const handleOnChangeApellidos = (e) => {
        console.log(e.target.value)
        setApellidos(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const nuevoEmpleado = {
            "rut_empleado": rut,
            "nombre_empleado": nombre,
            "apellidos_empleado": apellidos,
        }

        axios.post('http://localhost:5000/empleados/add', nuevoEmpleado)
            .then((response) => {
                setExitoRegistrarEmpleado("Empleado registrado exitosamente")
                console.log("Empleado registrado exitosamente", response.data)
            })
            .catch ((error) => {
                setExitoRegistrarEmpleado("Error al registrar el empleado")
                console.error("Error al registrar el empleado: ", error)
            });
    }

    const ping = exitoRegistrarEmpleado ? (
        <div className='mt-3'>
            <p>
                {exitoRegistrarEmpleado}: <br/>
                {nombre} {apellidos}
            </p>
        </div>
    ): null;

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
                        Apellidos
                        <input type="text" className="form-control"
                        value={apellidos}
                        onChange={handleOnChangeApellidos}
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
                            {/* verificar roles registrados */}
                            {/* P E N D I E N T E */}
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
                <br/>
                <br/>
                {ping}
            </form>
        </>
    )
}

export default Empleado;
