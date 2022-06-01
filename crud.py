import pyrebase

firebaseConfig = {
  'apiKey': "AIzaSyD5mRUV08gkotpiTMoigFJd9Bfb9O8_hgQ",
  'authDomain': "cedem-db.firebaseapp.com",
  'databaseURL': "https://cedem-db-default-rtdb.firebaseio.com/",
  'projectId': "cedem-db",
  'storageBucket': "cedem-db.appspot.com",
  'messagingSenderId': "272607335771",
  'appId': "1:272607335771:web:dff8951eb8e08f8eef367e",
  'measurementId': "G-ZT3V8MY4NC"
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
a10 = 'Debilidad ante la competencia',
a11 = 'Bajas ventas',
a12 = 'Dificultades de cobranza',
a13 = 'Negocio invalidado por el entorno',
a14 = 'Márgenes estrechos',
a15 = 'Nos hemos convertido en un competidor del montón',
a16 = 'Clientes insatisfechos',
a17 = 'Manejamos demasiados negocios',
a18 = 'Orientación al volumen',
a19 = 'Productos obsoletos',
a20 = 'Elevado número de quejas',
a21 = 'Nuestra propuesta al mercado se vuelve irrelevante'
a22 = 'Empresa con imagen pobre / desconocida',
a23 = 'Nuestra identidad no está alineada a nuestra propuesta al cliente',
a24 = 'Tenemos mala imagen en el mercado'
a25 = 'Dificultades familiares afectan el negocio',
a26 = 'Se ha perdido la confianza entre socios',
a27 = 'Demasiados conflictos / desunión',
a28 = 'Objetivos indefinidos o no compartidos',
a29 = 'La visión de los socios no es clara ni compartida',
a30 = 'No sabemos nuestros propósitos',
a31 = 'Hay problemas con la participación de familiares en el negocio',
a32 = 'Ya estoy cansado de no tener claro el camino',
a33 = 'Confusión en el manejo del dinero: sueldos, préstamos, etc.',
a34 = 'Desacuerdo en el concepto de negocio',
a35 = 'Diferencias entre socios'
a36 = 'Crecimiento demasiado rápido',
a37 = 'Crecimiento demasiado lento',
a38 = 'Carencia de equipo gerencial',
a39 = 'Baja capacidad administrativa',
a40 = 'Ceguera, sobreconfianza',
a41 = 'Excesiva centralización',
a42 = 'Demasiados proyectos a la vez',
a43 = 'Falta de coordinación entre departamentos',
a44 = 'Excesiva improvisación',
a45 = 'No hay trabajo en equipo',
a46 = 'Falta de consistencia en el avance',
a47 = 'Se cede ante la mediocridad  / falta de exigencia',
a48 = 'El rol de dueño no se ejerce con fuerza',
a49 = 'Falta desarrollo gerencial',
a50 = 'Estilo de mando ineficaz',
a51 = 'Vacío de poder',
a52 = 'Cambio frecuente de prioridades',
a53 = 'Lentitud en los cambios requeridos',
a54 = 'No hemos previsto cómo manejar la sucesión',
a55 = 'Se confunden los roles de dueño, directivo, empleado.',
a56 = 'Falta un líder claro y poderoso que dirija a la organización',
a57 = 'Rumbo perdido',
a58 = 'Problemas de relación con las autoridades',
a59 = 'Me falta capacidad directiva',
a60 = 'Nombramientos importantes por criterios familiares y afectivos'
a61 = 'Accionistas pasivos poco informados e involucrados',
a62 = 'Estructura de capital es una traba para crecer y atraer socios',
a63 = 'Los accionistas carecemos de un plan patrimonial',
a64 = 'Distribución pobre de dividendos',
a65 = 'Inquietudes no resueltas con relación al riesgo país'
a66 = 'Reuniones excesivas y/o inefectivas',
a67 = 'Estructura organizacional mal diseñada, inoperante',
a68 = 'Comunicación ineficaz',
a69 = 'Mal manejo del tiempo',
a70 = 'Mucha gente no domina los sistemas operativos',
a71 = 'Desánimo y baja moral',
a72 = 'No saber retener gente valiosa',
a73 = 'Descuido de la calidad',
a74 = 'Bajo nivel de servicio',
a75 = 'No hay evaluación objetiva del desempeño',
a76 = 'Delegación ineficaz',
a77 = 'Débil fuerza  de ventas',
a78 = 'Elevada rotación de personal',
a79 = 'El negocio es demasiado grande, organización rebasada',
a80 = 'Deficiencias en la contratación',
a81 = 'Conflictos laborales / intranquilidad',
a82 = 'Entregas tardías a clientes',
a83 = 'Personal excesivo',
a84 = 'No se cumplen internamente los compromisos',
a85 = 'Personal mal pagado',
a86 = 'Falta de capital',
a87 = 'Desaprovechamiento de recursos',
a88 = 'Equipos sub-utilizados',
a89 = 'Falta de liquidez',
a90 = 'Fallas de aprovisionamiento de proveedores',
a91 = 'Elevado punto de equilibrio',
a92 = 'Gastos fijos altos',
a93 = 'Inventarios desbalanceados / baja rotación',
a94 = 'Inversiones mal planeadas',
a95 = 'Elevados costos',
a96 = 'Tecnología obsoleta',
a97 = 'Equipo insuficiente o inadecuado',
a98 = 'Baja productividad',
a99 = 'Lentitud en nuestro proceso de transformación digital'
a100 = 'Indicadores desactualizados',
a101 = 'Limitada trazabilidad operativa',
a102 = 'Excesiva y costosa información que poco nos sirve',
a103 = 'No contamos con un ERP que nos dé el pulso del negocio',
a104 = 'Carecemos de un sistema de costeo ágil'
    
listo = []

listaCausas = db.child('DGax7rq0VhTjsck8o4NEFIdq4Vl1').child('dolencias').child("listaPEfectos").get().val()
    
causaDcausas = db.child('OWzxKwliOHQJRTBDwffl3KCPuH82').child('cuestionario100').child('CausasDeCausas').get().val()
'''
for i in causaDcausas:
  if i['prioridad'] == '1':
    causa1 = str(i)
  elif i['prioridad'] == '2':
    causa2 = i
  elif i['prioridad'] == '3':
    causa3 = i
'''
print(causaDcausas)