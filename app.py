from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

firebaseConfig = {

  'apiKey': "AIzaSyBsjbFVk5w3LYGYAxcYx-ipqMnIJJ5qs0k",
  'authDomain': "cedemapp.firebaseapp.com",
  'databaseURL': "https://cedemapp-default-rtdb.firebaseio.com",
  'projectId': "cedemapp",
  'storageBucket': "cedemapp.appspot.com",
  'messagingSenderId': "798113758726",
  'appId': "1:798113758726:web:c74ffbcb48f01736c18d87",
  'measurementId': "G-Y4DCCL02HS"
}


#Firebase
firebase = pyrebase.initialize_app(firebaseConfig)
#authentication
auth = firebase.auth()
#Storage
storage = firebase.storage()
#Database
db=firebase.database()

a1 = 'Demasiados clientes'
a2 = 'Dependencia en muy pocos clientes'
a3 = 'Creciente competencia'
a4 = 'Atendemos demasiados segmentos de mercado'
a5 = 'Desconocimiento de la competencia'
a6 = 'Baja rentabilidad'
a7 = 'Mercado poco fértil'
a8 = 'La empresa es demasiado pequeña'
a9 = 'Estamos más enfocados al producto que a las necesidades del cliente'
a10 = 'Debilidad ante la competencia'
a11 = 'Bajas ventas'
a12 = 'Dificultades de cobranza'
a13 = 'Negocio invalidado por el entorno'
a14 = 'Márgenes estrechos'
a15 = 'Nos hemos convertido en un competidor del montón'
a16 = 'Clientes insatisfechos'
a17 = 'Manejamos demasiados negocios'
a18 = 'Orientación al volumen'
a19 = 'Productos obsoletos'
a20 = 'Elevado número de quejas'
a21 = 'Nuestra propuesta al mercado se vuelve irrelevante'
a22 = 'Empresa con imagen pobre / desconocida'
a23 = 'Nuestra identidad no está alineada a nuestra propuesta al cliente'
a24 = 'Tenemos mala imagen en el mercado'
a25 = 'Dificultades familiares afectan el negocio'
a26 = 'Se ha perdido la confianza entre socios'
a27 = 'Demasiados conflictos / desunión'
a28 = 'Objetivos indefinidos o no compartidos'
a29 = 'La visión de los socios no es clara ni compartida'
a30 = 'No sabemos nuestros propósitos'
a31 = 'Hay problemas con la participación de familiares en el negocio'
a32 = 'Ya estoy cansado de no tener claro el camino'
a33 = 'Confusión en el manejo del dinero: sueldos, préstamos, etc.'
a34 = 'Desacuerdo en el concepto de negocio'
a35 = 'Diferencias entre socios'
a36 = 'Crecimiento demasiado rápido'
a37 = 'Crecimiento demasiado lento'
a38 = 'Carencia de equipo gerencial'
a39 = 'Baja capacidad administrativa'
a40 = 'Ceguera, sobreconfianza'
a41 = 'Excesiva centralización'
a42 = 'Demasiados proyectos a la vez'
a43 = 'Falta de coordinación entre departamentos'
a44 = 'Excesiva improvisación'
a45 = 'No hay trabajo en equipo'
a46 = 'Falta de consistencia en el avance'
a47 = 'Se cede ante la mediocridad  / falta de exigencia'
a48 = 'El rol de dueño no se ejerce con fuerza'
a49 = 'Falta desarrollo gerencial'
a50 = 'Estilo de mando ineficaz'
a51 = 'Vacío de poder'
a52 = 'Cambio frecuente de prioridades'
a53 = 'Lentitud en los cambios requeridos'
a54 = 'No hemos previsto cómo manejar la sucesión'
a55 = 'Se confunden los roles de dueño, directivo, empleado.'
a56 = 'Falta un líder claro y poderoso que dirija a la organización'
a57 = 'Rumbo perdido'
a58 = 'Problemas de relación con las autoridades'
a59 = 'Me falta capacidad directiva'
a60 = 'Nombramientos importantes por criterios familiares y afectivos'
a61 = 'Accionistas pasivos poco informados e involucrados'
a62 = 'Estructura de capital es una traba para crecer y atraer socios'
a63 = 'Los accionistas carecemos de un plan patrimonial'
a64 = 'Distribución pobre de dividendos'
a65 = 'Inquietudes no resueltas con relación al riesgo país'
a66 = 'Reuniones excesivas y/o inefectivas'
a67 = 'Estructura organizacional mal diseñada, inoperante'
a68 = 'Comunicación ineficaz'
a69 = 'Mal manejo del tiempo'
a70 = 'Mucha gente no domina los sistemas operativos'
a71 = 'Desánimo y baja moral'
a72 = 'No saber retener gente valiosa'
a73 = 'Descuido de la calidad'
a74 = 'Bajo nivel de servicio'
a75 = 'No hay evaluación objetiva del desempeño'
a76 = 'Delegación ineficaz'
a77 = 'Débil fuerza  de ventas'
a78 = 'Elevada rotación de personal'
a79 = 'El negocio es demasiado grande, organización rebasada'
a80 = 'Deficiencias en la contratación'
a81 = 'Conflictos laborales / intranquilidad'
a82 = 'Entregas tardías a clientes'
a83 = 'Personal excesivo'
a84 = 'No se cumplen internamente los compromisos'
a85 = 'Personal mal pagado'
a86 = 'Falta de capital'
a87 = 'Desaprovechamiento de recursos'
a88 = 'Equipos sub-utilizados'
a89 = 'Falta de liquidez'
a90 = 'Fallas de aprovisionamiento de proveedores'
a91 = 'Elevado punto de equilibrio'
a92 = 'Gastos fijos altos'
a93 = 'Inventarios desbalanceados / baja rotación'
a94 = 'Inversiones mal planeadas'
a95 = 'Elevados costos'
a96 = 'Tecnología obsoleta'
a97 = 'Equipo insuficiente o inadecuado'
a98 = 'Baja productividad'
a99 = 'Lentitud en nuestro proceso de transformación digital'
a100 = 'Indicadores desactualizados'
a101 = 'Limitada trazabilidad operativa'
a102 = 'Excesiva y costosa información que poco nos sirve'
a103 = 'No contamos con un ERP que nos dé el pulso del negocio'
a104 = 'Carecemos de un sistema de costeo ágil'

lista = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, 
a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, 
a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, 
a31, a32, a33, a34, a35, a36, a37, a38, a39, a40, 
a41, a42, a43, a44, a45, a46, a47, a48, a49, a50, 
a51, a52, a53, a54, a55, a56, a57, a58, a59, a60, 
a61, a62, a63, a64, a65, a66, a67, a68, a69, a70, 
a71, a72, a73, a74, a75, a76, a77, a78, a79, a80, 
a81, a82, a83, a84, a85, a86, a87, a88, a89, a90, 
a91, a92, a93, a94, a95, a96, a97, a98, a99, a100, a101, a102, a103, a104]

@app.route('/', methods = ['POST', 'GET'])
def index():

    nombre = ''
    correo = ''
    password = ''
    nivel = 1
    
    if request.method == "POST":
        nombre = str(request.form.get('nombre'))
        correo = str(request.form.get('correo'))
        password = str(request.form.get('password'))
        #Registro#
        user = auth.create_user_with_email_and_password(correo,password)
        #Sign in #
        user = auth.sign_in_with_email_and_password(correo, password)
        db.child(user['localId']).child('ID').set(user['localId'])
        db.child(user['localId']).child('NAME').set(nombre)
        db.child(user['localId']).child('EMAIL').set(correo)
        db.child(user['localId']).child('NIVEL').set(nivel)
        user = auth.refresh(user['refreshToken'])
        user_id = user['idToken']
        session['user'] = user_id
        return redirect(url_for('.home'))

    return render_template('index.html')

#########################################################################################
@app.route('/login', methods= ['POST', 'GET'])
def login():

    correo = ''
    password = ''
    message = ''

    if request.method == "POST":
        correo = str(request.form.get('correo'))
        password = str(request.form.get('password'))
        try:
            user = auth.sign_in_with_email_and_password(correo, password)
            user = auth.refresh(user['refreshToken'])
            user_id = user['idToken']
            session['user'] = user_id
            return redirect(url_for('.home'))
        except:
            message = 'Please check your credentials'
            return render_template('login.html', message=message)

    return render_template('login.html')

##############################################################################################
@app.route('/home')
def home():

    return render_template('home.html')

##############################################################################################
@app.route('/cuestionario0', methods= ['POST', 'GET'])
def cuestionario0():

    token = session['user']
    user = auth.get_account_info(token)
    localId = user['users'][0]['localId']

    if request.method == 'POST':
        listp = request.form.getlist('t1')

        if len(listp) >= 1:
            select = listp
        else:
            select = ['No hay registros']

        listainicial = []

        for i in select:
            if i != "":
                listainicial.append(i)

        db.child(localId).child('cuestionario100').child("listaP").set(listainicial)

        return redirect(url_for('.cuestionario'))

    return render_template('cuestionario0.html')

##############################################################################################
@app.route('/cuestionario', methods= ['POST', 'GET'])
def cuestionario():

    token = session['user']
    user = auth.get_account_info(token)
    localId = user['users'][0]['localId']

    if request.method == 'POST':
        listp = request.form.getlist('check1')

        if len(listp) >= 1:
            select = listp
        else:
            select = ['No hay registros']

        db.child(localId).child('cuestionario100').child("seleccion").set(select)

        return redirect(url_for('.seleccion'))

    return render_template('cuestionario.html', lista=lista)

####################################################################################################

@app.route('/seleccion', methods=['GET', 'POST'])
def seleccion():

    token = session['user']
    user = auth.get_account_info(token)
    localId = user['users'][0]['localId']
    
    listaSelect = []

    listap = db.child(localId).child('cuestionario100').child("listaP").get().val()

    for i in listap:
        listaSelect.append(i)

    BD = db.child(localId).child('cuestionario100').child('seleccion').get().val()

    for i in BD:
        listaSelect.append(i)

    if request.method == "GET":
        return render_template('seleccion.html', BD=BD, listap=listap, listaSelect=listaSelect)

    elif request.method == "POST":

        efecto = []
        causa = []
        noProblema = []

        for i in listaSelect:
            abc = request.form.getlist(i)
            for p in abc:
                if p == 'E':
                    efecto.append(i)
                elif p == 'C':
                    causa.append(i)
                elif p == 'N':
                    noProblema.append(i)

        db.child(localId).child('cuestionario100').child("Causas").set(causa)
        db.child(localId).child('cuestionario100').child("Efectos").set(efecto)
        db.child(localId).child('cuestionario100').child("NoProblemas").set(noProblema)

        return redirect(url_for('.causas'))

######################################################################################################
@app.route('/causas', methods=['GET', 'POST'])
def causas():
    
    token = session['user']
    user = auth.get_account_info(token)
    localId = user['users'][0]['localId']

    listaCausas = []

    prioridad1 = ''
    prioridad2 = ''
    prioridad3 = ''

    DDC = db.child(localId).child('cuestionario100').child("Causas").get().val()
    if DDC is not None:
        for i in DDC:
            listaCausas.append(i)

    if request.method == "GET":

        return render_template('causas.html', listaCausas=listaCausas)

    elif request.method == "POST":

        for i in listaCausas:
            abc = request.form.getlist(i)
            for a in abc:
                if a == '1':
                    prioridad1 = i
                elif a == '2':
                    prioridad2 = i
                elif a == '3':
                    prioridad3 = i

        db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad1').set(prioridad1)
        db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad2').set(prioridad2)
        db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad3').set(prioridad3)

        return redirect(url_for('.resultado'))

    return render_template('causas.html', listaCausas=listaCausas)

######################################################################################################
@app.route('/resultado', methods=['GET', 'POST'])
def resultado():

    token = session['user']
    user = auth.get_account_info(token)
    localId = user['users'][0]['localId']

    nada = ['No hay registro']

    listaCausas = []
    listaEfectos = []
    listaNoP = []
    causa1 = ''
    causa2 = ''
    causa3 = ''

    DDC = db.child(localId).child('cuestionario100').child("Causas").get().val()
    if DDC is not None:
        for i in DDC:
            listaCausas.append(i)

    DDE = db.child(localId).child('cuestionario100').child('Efectos').get().val()
    if DDE is not None:
        for i in DDE:
            listaEfectos.append(i)

    DDN = db.child(localId).child('cuestionario100').child('NoProblemas').get().val()
    if DDN is not None:
        for i in DDN:
            listaNoP.append(i)
    

    if request.method == "GET":

        causa1 = db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad1').get().val()
        causa2 = db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad2').get().val()
        causa3 = db.child(localId).child('cuestionario100').child('CausasDeCausas').child('prioridad3').get().val()

        return render_template('resultado.html', listaCausas=listaCausas, listaEfectos=listaEfectos, listaNoP=listaNoP, 
        causa1=causa1, causa2=causa2, causa3=causa3)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))