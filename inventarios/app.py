from flask import Flask, render_template, request, redirect, session
from db import get_db

app = Flask(__name__)
app.secret_key = "tu_clave_secreta"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE username=%s AND password=%s', (username, password))
        user = cursor.fetchone()

        if user:
            session['logged_in'] = True
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect('/')
        else:
            return "Usuario o contraseña incorrecta"
    
    return render_template('login.html')

@app.route('/')
def index():
    if 'logged_in' not in session:
        return redirect('/login')
    else:
         return render_template('index.html')
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # En producción, se debería encriptar

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute('INSERT INTO usuarios (username, password) VALUES (%s, %s)', (username, password))
        db.commit()
        
        return redirect('/login')
    return render_template('register.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if 'logged_in' not in session:
        return redirect('/login')

    if request.method == 'POST':
        nombre = request.form['nombre']
        stock = int(request.form['stock'])
        costo = float(request.form['costo'])
        precio = float(request.form['precio'])

        db = get_db()
        cursor = db.cursor(dictionary=True)

        cursor.execute('INSERT INTO productos (nombre, stock, costo, precio) VALUES (%s, %s, %s, %s)', (nombre, stock, costo, precio))
        db.commit()
        
        return redirect('/')
    return render_template('add_product.html')



@app.route('/calculate_eoq/<int:producto_id>', methods=['GET'])
def calculate_eoq(producto_id):
    if 'logged_in' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    print(producto_id)
    costo_mantener = 5.0  # Este es un ejemplo. Puedes obtenerlo desde una interfaz o tenerlo predefinido
    costo_pedido = 10.0  # Igual que el costo de mantener

    print(producto_id, costo_mantener,  costo_pedido)
    # Llama al procedimiento almacenado y pasa los parámetros
    cursor.execute("CALL CalcularEOQSUPER(%s, %s, %s, @eoq)", (producto_id, costo_mantener, costo_pedido))
    cursor.execute("SELECT @eoq")
    eoq = cursor.fetchone()  # Obtiene el valor de eoq

    print(eoq)

    return render_template('eoq.html', eoq=eoq)



    
@app.route('/calculate_parametros/<int:producto_id>/<float:costo_mantener>/<float:costo_pedido>', methods=['GET'])
def calculate_eoq_parametros(producto_id,costo_mantener, costo_pedido):
    if 'logged_in' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)

    print(producto_id)

    print(producto_id, costo_mantener,  costo_pedido)
    # Llama al procedimiento almacenado y pasa los parámetros
    cursor.execute("CALL CalcularEOQSUPER(%s, %s, %s, @eoq)", (producto_id, costo_mantener, costo_pedido))
    cursor.execute("SELECT @eoq")
    eoq = cursor.fetchone()  # Obtiene el valor de eoq

    print(eoq)

    return render_template('eoq.html', eoq=eoq)

@app.route('/view_eoqparams', methods=['GET', 'POST'])
def listarProductosParams():
    if 'logged_in' not in session:
        return redirect('/login')
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        costo_mantener = request.form['costo_mantener']
        costo_pedido = request.form['costo_pedido']
        
        # Llama directamente a la función calculate_eoq_parametros con los valores
        return calculate_eoq_parametros(producto_id, costo_mantener, costo_pedido)
    
    return render_template('eoq_params.html', productos=productos)






@app.route('/view_providers')
def viewProviders():
    if 'logged_in' not in session:
        return redirect('/login')
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM proveedores')
    proveedores = cursor.fetchall()
    
    return render_template('lista_proveedores.html', proveedores=proveedores)
    




@app.route('/view_products', methods=['GET', 'POST'])
def listarProductos():
    if 'logged_in' not in session:
        return redirect('/login')
    
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    
    if request.method == 'POST':
        producto_id = request.form['producto_id']
        return redirect(f'/calculate_eoq/{producto_id}')
    
    return render_template('lista_productos.html', productos=productos)

    
@app.route('/add_provider', methods=['GET', 'POST'])
def add_provider():
    if 'logged_in' not in session:
        return redirect('/login')

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    if request.method == 'POST':
        nombre = request.form['nombre']
        producto_id = request.form['producto_id']

        cursor.execute('INSERT INTO proveedores (nombre, producto_id) VALUES (%s, %s)', (nombre, producto_id))
        db.commit()
        
        return redirect('/')
    return render_template('add_provider.html', productos=productos)


@app.route('/ayuda')
def secondary():
    
    return str("<h1>nose como declarar impuestos<h1>")

app.run(debug=True)