import React from 'react'

function VisualizacionDatos() {

    const datos = [
        {rut: 12345678, nombre: 'Juan', rol: 'maestro', horas: 23, salario: 2000},
        {rut: 18765432, nombre: 'Jose', rol: 'jardinero', horas: 11, salario: 2000},
        {rut: 19456321, nombre: 'Jack', rol: 'auxiliar', horas: 47, salario: 2000},
    ]

    return (
        <>
        <h4 className="bg-payne-grey content-title shadow">VISUALIZACIÓN DE DATOS</h4>
            <div className="content-body">
                <div className="d-flex flex-column">
                    <h4>Tabla de Cosas</h4>
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
                                <tr key={item.rut}>
                                    <td>{item.rut}</td>
                                    <td>{item.nombre}</td>
                                    <td>{item.rol}</td>
                                    <td>{item.horas}</td>
                                    <td>{item.salario}</td>
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