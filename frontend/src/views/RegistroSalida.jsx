import React, { useState } from 'react'

function RegistroSalida() {

    const [rut, setRut] = useState("")
    const [exitoRegistroSalida, setExitoRegistroSalida] = useState("")

    const handleOnChangeRut = (e) => {
        console.log(e.target.value)
        setRut(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        const registroRutSalida = {
            //revisar nombres de la bdd
            "":  rut
        }
    }

    //axios

    return (
        <>
            <h4 className="bg-payne-grey content-title shadow">REGISTRO DE SALIDA</h4>
            <div className='content-body'>
                <div className='container'>
                    <div className='d-flex justify-content-around flex-wrap'>
                        <form onSubmit={handleSubmit}>
                            <div className='d-flex flex-column'>

                                <label className='form-label mt-3'>
                                    Rut del Empleado
                                    <input type="text" className='form-control'
                                    value={rut}
                                    onChange={handleOnChangeRut}
                                    />
                                </label>
                            </div>

                            <button type="submit" className="btn btn-warning ms-4 mt-3 text-white">
                                Registrar Salida
                            </button>
                            {exitoRegistroSalida}
                        </form>
                    </div>
                </div>
            </div>
        </>
    )
}

export default RegistroSalida;