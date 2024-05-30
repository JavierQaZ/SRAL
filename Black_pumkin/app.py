from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1607'
app.config['MYSQL_DB'] = 'black_pumpkin'

mysql = MySQL(app)

@app.route('/')
def Index():
    return 'Hello World'

@app.route('/empleados')
def empleados():
    return render_template('empleado.html')

@app.route('/add_empleado', methods=['POST'])
def add_empleado():
    if request.method == 'POST':
        Rut = request.form['Rut']
        Nombre = request.form['Nombre']
        Apellidos = request.form['Apellidos']
        Cod_rol = request.form['Cod_rol']
        Total_horas = request.form['Total_horas']
        Sueldo_total = request.form['Sueldo_total']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO empleados (RUT, Nombre, Apellidos, CodigoRol, TotalHorasTrabajadas, SueldoTotal) VALUES (%s, %s, %s, %s, %s, %s)',
                    (Rut, Nombre, Apellidos, Cod_rol, Total_horas, Sueldo_total))
        mysql.connection.commit()
        cur.close()
        
        return 'listo'
    

@app.route('/edit_empleado')
def edit_empleado():
    return 'edit_empleado'

@app.route('/delete_empleado')
def delete_empleado():
    return 'delete_empleado'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
