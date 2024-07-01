import React, {useState, useEffect} from 'react'
import axios from 'axios';

function Gestion() {

    const [datos, setDatos] = useState([])

    useEffect(() => {
        /* MODIFICAR */
        axios.get('http://localhost:5000/MODIFICAR/get')
            .then(response => {
                setDatos(response.data);
            })
            .catch(error => {
                console.error('Error recolectando datos: ', error)
            })
    }, []);

    return (
        <>
            <h4 className="bg-payne-grey content-title shadow">GESTIÓN</h4>
            <div className="content-body">
                <div className="d-flex flex-column">
                    <table>
                        <thead>
                            <tr>
                                <th>Nombre del KPI</th>
                                <th>Valor</th>
                            </tr>
                        </thead>
                        <tbody>
                            {datos.map((item) => (
                                /* MODIFICAR */
                                <tr key={MODIFICAR}>
                                    <td>{item.MODIFICAR}</td> /*Nombre del KPI*/
                                    <td>{item.MODIFICAR}</td> /*Valor del KPI*/
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