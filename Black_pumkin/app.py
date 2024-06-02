#Encargado de lanzar toda la aplicacion
from config import config
from src import create_app


configuration = config['development']
app = create_app(configuration)

if __name__ == '__main__':
   
    app.run()
