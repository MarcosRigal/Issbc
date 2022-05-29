"""
Created on Sun Jan 19 12:19:10 2014

@author: acalvo
"""
import mcFrutos as mcf #Cambiar al cambiar el MC
import mcIris as mci #Cambiar al cambiar el MC

class Tarea():
    def __init__(self):
        self.objetivo=''
        self.descripcion=''
        pass
    
class Clasificacion(Tarea):
    def __init__(self,bc,objeto):
        self.objetivo=u'''    '''
        self.objeto=objeto
        self.bc=bc
        self.metodo='poda'
        self.salida=None
        
    def execute(self):
        print ('ejectutando la tarea')
        if self.metodo=='poda':
            mt=MetodoPoda()
        pass
    
class MetodoPoda():
    '''Dado un objeto clasificarlo como perteneciente a una clase
    '''
    def __init__(self,obj):
        self.obj=obj
        self.clasesCandidatas=[]
        self.lAtributosUsados=[]
        self.conjuntoNuevosValores=[]
        self.explicacion=u''
        pass
    def execute(self):
        # Se generan las posibles clases candidatas
        g=Generar(self.obj)
        self.clasesCandidatas=g.execute()
        self.explicacion+=u'Se generam las clases candidatas que son:\n'
        for cc in self.clasesCandidatas:
            self.explicacion+=cc.nombre+'\n'
        self.explicacion+='\n'
        newSolucion=True
        while newSolucion and len(self.clasesCandidatas)>0:#Mientras se esté buscando una nueva solución :
                                                           #y haya clases candidatas
            print             
            print ('inicio while-> Lista de atributos usados:', self.lAtributosUsados)
            print ('Clases candidatas:',self.clasesCandidatas)
            for clc in self.clasesCandidatas:
                print (clc.nombre)
            print ('=======================')
            print 
            
            esp=Especificar(self.clasesCandidatas,self.lAtributosUsados)#Especifica un atributo
            #print 'Número de clases candidatas:', len(self.clasesCandidatas)
            newLatr=esp.execute() #Se especifica el nuevo atributo
            
            if not newLatr==(None,None): #Si sigue habiendo atributos:
                self.lAtributosUsados=newLatr[1]#Tomamos la nueva lista de ATRIBUTOS usados
                print ('new atributo seleccionado:', newLatr[0].nombre)
                #print ('Atributos usados ',
                for atu in self.lAtributosUsados:
                    print (atu.nombre)
                    
                print
                self.explicacion+='Seleccionamos  el atributo '+newLatr[0].nombre+' '
                #Obtenemos el valor del atributo en el objeto
                obt=Obtener(self.obj,newLatr[0])
                at=obt.execute()
                print (at)
                print ('=======================')
                print ('atributo y valor atributo del objeto:', at.atributo.nombre,at.valor)
                print ('========================')
                
                self.explicacion+='con el valor: '
                if not isinstance(at.valor,str):
                    self.explicacion+=str(at.valor)+'\n'
                else:
                    self.explicacion+=at.valor+'\n'
                    
                self.conjuntoNuevosValores.append(at)#Se actualiza el conjunto de nuevos valores
                
                
                newcc=[]#La lista de de nuevas candidatas se pone a vacía
                for cc in self.clasesCandidatas: #Para cada clase en las clases candidatas
                    pass
                    #Equiparar el conjunto de nuevos valores con el conjunto de clases candidatas y eliminar 
                    #las clases candidatas que no satisfagan los valores del atributo
                    self.explicacion+='    Probamos la clase candidata '+cc.nombre+'\n'
                    print 
                    print ('Probamos a equiparar la clase: ', cc.nombre)
                    print (' con el conjunto de nuevos pares atributos/valores: ')
                    for cnv in self.conjuntoNuevosValores:
                        print (cnv.atributo.nombre,'=', cnv.valor)
                    print ('==================================')
                    print 
                    eq=Equiparar(cc, self.conjuntoNuevosValores)
                    result,expl = eq.execute()
                    self.explicacion+=expl
                    
                    self.explicacion+='      Resultado de equiparar clase candidata '+cc.nombre+' '+str(result)+'\n'
                    print ('Resultado de equiparar la clase:', cc.nombre, result)
                    print 
                    if  result==True:#Sólo añadimos las clases candidatas que satisfagan el valor del atributo
                        newcc.append(cc)
                        print ('Clase aceptada:',cc.nombre)
                    
            else:
                print ('No quedan más atributos por especificar')
                print 
                newSolucion=False #No quedan más atributos por explorar
                continue
            print
            self.clasesCandidatas=newcc
            self.explicacion+=u'\n Clases candidatas tras la equiparación: '
            for cc in self.clasesCandidatas:
                self.explicacion+=' '+cc.nombre+'  '
                self.explicacion+='\n'+cc.descripcion()+'\n'
            self.explicacion+='\n'
            
        return self.clasesCandidatas, self.explicacion
        

class Inferencia():
    def __init__(self):
        pass
    def execute(self):
        pass

class Equiparar(Inferencia):
    '''
    '''
    def __init__(self,candidata,nuevosValores):
        Inferencia.__init__(self)
        self.candidata=candidata
        self.nuevosValores=nuevosValores
        self.explicacion=u''
    
    def execute(self):
        '''
        Equipara una clase candidata con el conjunto de nuevos
        valores devolviendo False si es rechazada la clase candidata.
        '''
        print 
        print ('====================================')
        print ('Ejecución de la inferencia equiparar')
        print ('=====================================')
        print 
        #Para cada valor comprobar que es compatible con la definición de la clase
        for nv in self.nuevosValores: #Para cada nuevo atributo-valor 
            print ('Equiparando el atributo/valor del objeto:',nv.atributo.nombre,'=', nv.valor)
            print ('Con la clase candidata ', self.candidata.nombre)
            
            self.explicacion+='\t Equiparar el atributo '+nv.atributo.nombre+'= '
            if not isinstance(nv.valor,str):
                self.explicacion+=str(nv.valor)+'\n '
            else:
                self.explicacion+=nv.valor+'\n '
                
            for r in self.candidata.reglas:#Para cada regla en la clase candidata:
                print ('Nombre y tipo  de la regla:', r.idRegla,r.tipo)
                if r.atributo.nombre==nv.atributo.nombre: #Si los atributos son comparables:
                    if r.tipo=='igual':#Si el atributo es de tipo igual:
                        print ('Compara valor del atributo en la regla',r.valorEsperado,nv.valor)
                        if r.valorEsperado==nv.valor:
                            continue #Es compatible con la clase
                        else:
                            return False,self.explicacion #No es compatible con la clase
                    if r.tipo=='rango':#Si el atributo de la regla es de tipo rango
                        print ('evaluo rango')
                        if nv.valor <r.valorEsperado[1] and nv.valor >=r.valorEsperado[0]:
                            continue #Es compatible con la clase
                        else:
                            return False,self.explicacion  #No es compatible y retorna False
                else:
                    print ('Regla no aplicable a este atributo\n')
        return True,self.explicacion #Ha pasado el test a todos los nuevos valores del objeto
    
    
        
    


class Generar(Inferencia):
    '''Dado un objeto genera un conjunto de clases candidatas
       Esta inferencia es básica se devuelven todas las clases 
       candidatas que ofrece la base de conocimiento.
    '''
    def __init__(self,objeto):
        Inferencia.__init__(self)
        self.objeto=objeto
    def execute(self): #Ejecución del método de la inferencia:
        print ('===================================')
        print ('Ejecución de la inferencia generar')
        print ('===================================')
        print 
        if self.comboboxWidgetDominio.currentText() == 'Iris':
            clases=mci.clases() #Se ha simplificado mucho y devuelve todas 
        else:
            clases=mcf.clases() #Se ha simplificado mucho y devuelve todas 
                             #las clases candidatas
        return clases
        
class Obtener(Inferencia):
    '''Dado un aributo obtener un valor para ese atributo en 
       el objeto a clasificar.
    '''
    def __init__(self,objeto,atributo):
        Inferencia.__init__(self)
        self.objeto=objeto
        self.atributo=atributo
    def execute(self): #Ejecución del método de la inferencia:
        print 
        print ('Ejecución de la inferencia obtener')
        print ('==================================')
        print 
        for cat in self.objeto.caracteristicas:#Para cada caracteristica del objeto
            if self.atributo.nombre==cat.atributo.nombre:#Si el nombre coincide
                return cat #Devuelve la caracteristica del objeto          
        return None #Si no ha encontrado nada devuelve None
        
class Especificar(Inferencia):
    '''Dado un conjunto de clases candidatas no vacío 
       especifica un atributo para extraer su valor en otra inferencia.
    '''
    def __init__(self,clasesCandidatas,lAtributosUsados):
        '''
        @param lLlasesCandidatas: Lista de clases candidatas
        @param lAtributosUsados: Lista de atributos ya seleccionados
        '''
        Inferencia.__init__(self)
        self.cc=clasesCandidatas
        self.lAtributosUsados=lAtributosUsados
        pass
    def execute(self):
        '''Ejecución del método de la inferencia
        @return: Devuelve en una tupla el atributo especificado y la lista de atributos ya
                 usados.
        '''
        print ('=================================')
        print ('Inferencia especificando atributo')
        print ('=================================')
        print 
        if len(self.cc)>0: # El conjunto de clases candidatas no es vacío
            clase=self.cc[0] #especificamos la primera clase en la lista
            for at in clase.atributos:
                #print 'at:,',at,at.nombre, '->',self.lAtributosUsados
                if not at.nombre in [atu.nombre for atu in self.lAtributosUsados]:#Si ek atributo no está en los usados 
                    self.lAtributosUsados.append(at)#Se añade a la lista
                    return (at, self.lAtributosUsados)#Se retorna un atributo no usado y la lista de atributos
                                                      #que ya se han usado
            
            return None,None #Si todos los atributos están        
    
       
       
       
         
        
        
        
    

    
    
    