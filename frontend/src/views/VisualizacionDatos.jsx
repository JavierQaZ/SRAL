import React, {useState, useEffect} from 'react'
import axios from 'axios';

function VisualizacionDatos() {

    const [datos, setDatos] = useState([])

    useEffect(() => {
        axios.get('http://localhost:5000/empleados/get')
            .then(response => {
                setDatos(response.data);
            })
            .catch(error => {
                console.error('Error recolectando datos: ', error)
            })
    }, []);

    return (
        <>
        <h4 className="bg-payne-grey content-title shadow">VISUALIZACIÓN DE DATOS</h4>
            <div className="content-body">
                <div className="d-flex flex-column">
                    <table>
                        <thead>
                            <tr>
                                <th>RUT</th>
                                <th>Nombre</th>
                                <th>Rol</th>
                                <th>Horas</th>
                                <th>Salario</th>
                            </tr>
                        </thead>
                        <tbody>
                            {datos.map((item) => (
                                <tr key={item.rut_empleado}>
                                    <td>{item.rut_empleado}</td>
                                    <td>{item.nombre_empleado} {item.apellidos_empleado}</td>
                                    <td>{item.codigo_rol}</td>
                                    <td>{item.totalHorasTrabajadas_empleado}</td>
                                    <td>{item.sueldoTotal_empleado}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            </div>
        </>
    );
}

export default VisualizacionDatos;