import web  # pip install web.py
import app
import json  # json parser
import csv

'''
    Controller Alumnos que es invocado cuando el usuario ingrese a la 
    URL: http://localhost:8080/alumnos?action=get&token=1234
    app_version = "0.01"  # version de la webapp
    file = 'static/csv/alumnos.csv'  # define el archivo donde se almacenan los datos

    def __init__(self):  # Método inicial o constructor de la clase
        pass  # Simplemente continua con la ejecución
'''
render=web.template.render('application/views/')

class Alumnos:
    def GET(self):
        try:
            data = web.input() 
            if (data['token'] =='1234'):  # valida el token que se recibe por url
                #http://localhost:8080/alumnos?action=get&token=1234
                if (data['action'] =="get"): 
                    Informacion = {}
                    Informacion['version']="0.1"
                    Informacion['status']="200 OK"
                    dato_inf="matricula,nombre,primer_apellido,segundo_apellido,carrera\n"
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        dato_inf = []
                        for fila in reader:
                            resul = {}
                            resul['matricula'] = str(fila['matricula'])
                            resul['nombre'] = str(fila['nombre'])
                            resul['primer_apellido'] = str(fila['primer_apellido'])
                            resul['segundo_apellido'] = str(fila['segundo_apellido'])
                            resul['carrera'] = str(fila['carrera'])
                            dato_inf.append(resul)# agrega el diccionario generado al array alumnos
                        Informacion['alumno'] = dato_inf
                        return json.dumps(Informacion)



                #Insercion
                #http://localhost:8080/alumnos?action=insert&token=1234&matricula=171811&nombre=Jose&apellido_paterno=Lira&apellido_materno=Castro&carrera=DN
                if(data['action']=="insert"):
                    Informacion={}
                    Informacion['version']="0.01"
                    Informacion['status']="200 OK"  
                    matricula=str(data['matricula'])
                    nombre=str(data['nombre'])
                    apellido_paterno=str(data['apellido_paterno'])
                    apellido_materno=str(data['apellido_materno'])
                    carrera=str(data['carrera'])
                    resp=[]
                    resp.append(matricula)
                    resp.append(nombre)
                    resp.append(apellido_paterno)
                    resp.append(apellido_materno)
                    resp.append(carrera)
                    result={}
                    result['matricula']=matricula
                    result['nombre']=nombre
                    result['apellido_paterno']=apellido_paterno
                    result['apellido_materno']=apellido_materno
                    result['carrera']=carrera
                    dato_inf=[]
                    dato_inf.append(result)
                    Informacion['alumnos']=dato_inf
                    with open('static/csv/alumnos.csv','a+', newline='') as variable_que_sea:
                        writer=csv.writer(variable_que_sea)
                        writer.writerow(result)
                    return json.dumps(Informacion)


                    #Busqueda
                    #http://localhost:8080/alumnos?action=search&token=1234&matricula=171813
                if(data['action']=='search'):
                    Informacion={}
                    Informacion['version']="0.01"
                    Informacion['status']="200 ok"
                    dato_inf="matricula,nombre,apellido_paterno,apellido_materno,carrera\n"
                    matricula=str(data['matricula'])
                    with open ('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        dato_inf=[]
                        for fila in reader:
                            if(fila['matricula'] == matricula):
                                result={}
                                result['matricula']=str(fila['matricula'])
                                result['nombre']=str(fila['nombre'])
                                result['apellido_paterno']=str(fila['apellido_paterno'])
                                result['apellido_materno']=str(fila['apellido_materno'])
                                result['carrera']=str(fila['carrera'])
                                dato_inf.append(result)
                            Informacion['alumno']=dato_inf
                    return json.dumps(Informacion)


                    #Actualizacion
                #http://localhost:8080/alumnos?action=update&token=1234&matricula=171810&nombre=Roberta&apellido_paterno=Perez&apellido_materno=Hernandez&carrera=TIC
                if(data['action']=='update'):
                    Informacion={}
                    Informacion['version']="0.01"
                    Informacion['status']="200 ok"  
                    dato_inf="matricula,nombre,apellido_paterno,apellido_materno,carrera"
                    matricula_2=str(data['matricula'])
                    nombre_2=str(data['nombre'])
                    apellido_paterno2=str(data['apellido_paterno'])
                    apellido_materno_2==str(data['apellido_materno'])
                    carrera_2=str(data['carrera'])
                    with open('static/csv/alumnos.csv', 'r') as csvfile:
                        reader = csv.DictReader(csvfile)
                        dato_inf=[] # se utilizará este arreglo para modificar los registros del CSV (obtiene una fila, si es necesario la modifica y al final envía al archivo)
                        for fila in reader:
                            result={}
                            # comprueba que la fila sea la indicada para modificar, en base a la matricula dada como parametro en la URL
                            if (fila['matricula'] == matricula_2):
                                result['matricula']=str(fila['matricula'])
                                result['nombre']=nombre_2
                                result['apellido_paterno']=apellido_paterno_2
                                result['apellido_materno']=apellido_materno_2
                                result['carrera']=carrera_2
                            else:
                                result['matricula']=str(fila['matricula'])
                                result['nombre']=str(fila['nombre'])
                                result['apellido_paterno']=str(fila['apellido_paterno'])
                                result['apellido_materno']=str(fila['apellido_materno'])
                                result['carrera']=str(fila['carrera'])
                            dato_inf.append(result)
                        Informacion['alumno']=dato_inf


                        # sobreescribe el archivo CSV con los valores modificados
                        with open('static/csv/alumnos.csv', 'w') as csvfile:
                            nombres_campos = ['matricula','nombre','primer_apellido','segundo_apellido','carrera']
                            writer = csv.DictWriter(csvfile, fieldnames=nombres_campos)
                            
                            writer.writeheader() # escribe los nombres de los campos en el encabezado del CSV
                            for i in range(0, len(dato_inf)):
                                # writer.writerow({'field1': 'A', 'field2': 'B', 'field3': 'C'})
                                writer.writerow(dato_inf[i])
                                print(dato_inf[i]) # print de prueba...
                        
                        return json.dumps(dato_inf)


        except Exception as e:
            dato_inf=[]    
            dato_inf.append('Ocurrio algun error'+ str(e.args))
            return dato_inf
                    



