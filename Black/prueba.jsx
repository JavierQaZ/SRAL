import React, { useState } from 'react';
import axios from 'axios';

function AddEmpleadoForm() {
  const [formData, setFormData] = useState({
    Rut: '',
    Nombre: '',
    Apellidos: '',
    Cod_rol: '',
    Total_horas: '',
    Sueldo_total: ''
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:5000/add_empleado', formData);
      alert('Empleado agregado exitosamente');
    } catch (error) {
      alert('Error al agregar empleado');
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Add Employee</h1>
      <form onSubmit={handleSubmit}>
        <label>Rut:</label>
        <input type="text" name="Rut" value={formData.Rut} onChange={handleChange} required /><br />
        <label>Nombre:</label>
        <input type="text" name="Nombre" value={formData.Nombre} onChange={handleChange} required /><br />
        <label>Apellidos:</label>
        <input type="text" name="Apellidos" value={formData.Apellidos} onChange={handleChange} required /><br />
        <label>Cod_rol:</label>
        <input type="text" name="Cod_rol" value={formData.Cod_rol} onChange={handleChange} required /><br />
        <label>Total_horas:</label>
        <input type="number" name="Total_horas" value={formData.Total_horas} onChange={handleChange} required /><br />
        <label>Sueldo_total:</label>
        <input type="number" name="Sueldo_total" value={formData.Sueldo_total} onChange={handleChange} required /><br />
        <button type="submit">Add Employee</button>
      </form>
    </div>
  );
}

export default AddEmpleadoForm;
