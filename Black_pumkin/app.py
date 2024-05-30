from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1607'
app.config['MYSQL_DB'] = 'black_pumpkin'

mysql = MySQL(app)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/empleados')
def empleados():
    return render_template('empleado.html')

@app.route('/add_empleado', methods=['GET', 'POST'])
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
        
        return redirect(url_for('empleado'))
    
    # Si la solicitud no es POST, renderiza la plantilla para agregar un empleado
    return render_template('add_empleado.html')


@app.route('/edit_empleado')
def edit_empleado():
    return 'edit_empleado'

@app.route('/delete_empleado')
def delete_empleado():
    return 'delete empleado'

@app.route('/rol')
def rol():
    return render_template('rol.html')

@app.route('/add_rol', methods=['GET', 'POST'])
def add_rol():
    if request.method == 'POST':
        Codigo = request.form['Codigo']
        Nombre = request.form['Nombre']
        SueldoPorHora = request.form['SueldoPorHora']

        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO rol (Codigo, Nombre, SueldoPorHora) VALUES (%s, %s, %s)',
                    (Codigo, Nombre, SueldoPorHora))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('rol'))
    
    # Si la solicitud no es POST, renderiza la plantilla para agregar un empleado
    return render_template('add_rol.html')

@app.route('/edit_rol')
def edit_rol():
    return 'edit_rol'

@app.route('/delete_rol')
def delete_rol():
    return 'delete rol'

if __name__ == '__main__':
    app.run(port=3000, debug=True)
