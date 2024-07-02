import axios from "axios";

const auth = {
    login: async (user, password) => {
        try {
            const userData = {
                MODIFICAR: user, //modificar con bdd
                MODIFICAR1: password //modificar bdd
            };
        } catch(error){
            console.log(error);
        }
    }
}

export default auth;