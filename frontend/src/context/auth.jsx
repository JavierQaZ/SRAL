import axios from "axios";

const auth = {
    login: async (rut, contrasena) => {
        try {
            const userData = {
                rut_empleado: rut,
                contrasena: contrasena
            };

            const resp = await axios.post("http://localhost:5000/login", userData)
            return resp.data;
        } catch(error) {
            console.log(error);
        }
    }
}

export default auth;