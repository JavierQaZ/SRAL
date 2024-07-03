import React, {useState, useEffect} from 'react'
import axios from 'axios';

function Gestion() {

    const [datos, setDatos] = useState([])
    const [mes, setMes] = useState("")
    const [anio, setAnio] = useState("")
    const [exitoFecha, setExitoFecha] = useState("")

    useEffect(() => {
        obtenerDatos();
    }, []);

    const obtenerDatos = () => {
        axios.get('http://localhost:5000/gestion/get')//verificar
            .then(response => {
                setDatos(response.data);
            })
            .catch(error => {
                console.error('Error recolectando datos: ', error)
            })
    }

    const handleOnChangeMes = (e) => {
        console.log(e.target.value)
        setMes(e.target.value)
    }

    const handleOnChangeAnio = (e) => {
        console.log(e.target.value)
        setAnio(e.target.value)
    }

    const handleSubmit = (e) => {
        e.preventDefault();

        if (mes === "" || anio === ""){
            setExitoFecha("Todos los campos son obligatorios")
            return;
        }

        const fecha = {
            "mes": mes,
            "anio": anio
        }

        axios.post('http://localhost:5000/kpi/gestion', fecha)
            .then((response) => {
                setExitoFecha("Fecha enviada")
                console.log("Fecha enviada", response.data)
                obtenerDatos();
            })
            .catch ((error) => {
                setExitoFecha("Error al enviar fecha")
                console.log("Error al enviar fecha", error)
            })
    }

    return (
        <>
            <h4 className="bg-payne-grey content-title shadow">GESTIÓN</h4>
            <div className="content-body">
                <div className="d-flex flex-column">
                    <form onSubmit={handleSubmit}>
                        <div className='d-flex justify'>
                            <label className='form-label mt-3'>Mes
                                <input type="text" className='form-control'
                                value={mes}
                                onChange={handleOnChangeMes}
                                placeholder='Ingrese el Mes (1 al 12)'>
                                </input>
                            </label>
                            <label className='form-label mt-3'>Año
                                <input type="text" className='form-control'
                                value={anio}
                                onChange={handleOnChangeAnio}
                                placeholder='Ingrese año (XXXX)'>
                                </input>
                            </label>
                            <button type="submit" className="btn btn-warning ms-4 mt-3 text-white">
                                Aceptar
                            </button>
                        </div>
                    </form>
                    <p>{exitoFecha}</p>
                    <table>
                        <thead>
                            <tr>
                                <th>Nombre del KPI</th>
                                <th>Valor</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>Costo Total por Mes</td>
                                <td>{datos.costo_total_por_mes}</td>
                            </tr>
                            <tr>
                                <td>Costo por Hora Trabajada</td>
                                <td>{datos.costo_por_hora_trabajada}</td>
                            </tr>
                            <tr>
                                <td>Promedio de Horas Trabajadas</td>
                                <td>{datos.promedio_horas_trabajadas}</td>
                            </tr>
                            {datos.costo_total_por_rol && datos.costo_total_por_rol.map((rol, index) => (
                                <tr key={index}>
                                    <td>Costo Total de {rol[1]}</td>
                                    <td>{rol[2]}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    )
}

export default Gestion;