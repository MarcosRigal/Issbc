#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Clasificador

En este fichero se almacenan las clases del dominio de los coches

Authors: Marcos Rivera Gavilan, Marcos Rodriguez Moreno, Moises Moyano Cejudo
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

class Clase():

    def __init__(self, nombre):
        self.nombre = nombre
        self.reglas = []  

    def descripcion(self):
        descripcion = u''
        descripcion += self.nombre+'\n'
        for r in self.reglas:
            descripcion += r.idRegla+' '+r.tipo+' ' + 'None' + ' ' + r.atributo.nombre+' '
            if isinstance(r.valorEsperado, str):
                descripcion += ' '+r.valorEsperado+'\n'
            elif isinstance(r.valorEsperado, int) or isinstance(r.valorEsperado, float):
                descripcion += ' '+str(r.valorEsperado)+'\n'
            elif isinstance(r.valorEsperado, list):
                for i in r.valorEsperado:
                    descripcion += ' '+str(i)+' '
                descripcion += '\n'
        return descripcion

class Coche(Clase):

    def __init__(self, nombre):
        Clase.__init__(self, nombre=nombre)

        self.atAS = Atributo('Marca', 'str', None)
        self.atLS = Atributo('Carroceria', 'str', 'None')
        self.atAP = Atributo('Plazas', 'int', 'nº')
        self.atLP = Atributo('Potencia', 'int', 'cv')

        self.atributos = [self.atAS, self.atLS, self.atAP, self.atLP]

class Mercedes_AMG_SL(Coche):

    def __init__(self):
        Coche.__init__(self, nombre='Mercedes-AMG SL')
        r1 = Rverifica(idRegla='r1', tipo='igual', subtipo=None,
                       atributo=self.atAS, valorEsperado="Mercedes")
        r2 = Rverifica(idRegla='r2', tipo='igual', subtipo=None,
                       atributo=self.atLS, valorEsperado="Deportivo")
        r3 = Rverifica(idRegla='r3', tipo='rango', subtipo=None,
                       atributo=self.atAP, valorEsperado=[2, 4])
        r4 = Rverifica(idRegla='r4', tipo='rango', subtipo=None,
                       atributo=self.atLP, valorEsperado=[300, 700])
        self.reglas = [r1, r2, r3, r4]
        pass


class BMW_iX3(Coche):
    def __init__(self):
        Coche.__init__(self, nombre='BMW iX3')
        r1 = Rverifica(idRegla='r1', tipo='igual', subtipo=None,
                       atributo=self.atAS, valorEsperado="BMW")
        r2 = Rverifica(idRegla='r2', tipo='igual', subtipo=None,
                       atributo=self.atLS, valorEsperado="SUV")
        r3 = Rverifica(idRegla='r3', tipo='rango', subtipo=None,
                       atributo=self.atAP, valorEsperado=[4, 8])
        r4 = Rverifica(idRegla='r4', tipo='rango', subtipo=None,
                       atributo=self.atLP, valorEsperado=[100, 450])

        self.reglas = [r1, r2, r3, r4]


class Audi_A5(Coche):
    def __init__(self):
        Coche.__init__(self, nombre='Audi A5')
        r1 = Rverifica(idRegla='r1', tipo='igual', subtipo=None,
                       atributo=self.atAS, valorEsperado="Audi")
        r2 = Rverifica(idRegla='r2', tipo='igual', subtipo=None,
                       atributo=self.atLS, valorEsperado="Berlina")
        r3 = Rverifica(idRegla='r3', tipo='rango', subtipo=None,
                       atributo=self.atAP, valorEsperado=[2, 5])
        r4 = Rverifica(idRegla='r4', tipo='rango', subtipo=None,
                       atributo=self.atLP, valorEsperado=[150, 575])
        self.reglas = [r1, r2, r3, r4]

class Regla():

    def __init__(self, idRegla, tipo):
        self.idRegla = idRegla
        self.tipo = tipo
        pass


class Rverifica(Regla):

    def __init__(self, idRegla, tipo, subtipo, atributo, valorEsperado):
        Regla.__init__(self, idRegla, tipo)
        self.subtipo = subtipo
        self.atributo = atributo
        self.valorEsperado = valorEsperado

    def execute(self, at):

        if self.atributo.nombre == at.nombre:

            if self.tipo == 'igual':
                if self.valorEsperado == at.valor:
                    return True
                else:
                    return False

            if self.tipo == 'rango':
                print('evaluo rango')
                if at.valor < self.valorEsperado[1] and at.valor >= self.valorEsperado[0]:
                    return True
                else:
                    return False
        else:
            return None

    def descripcion(self):
        descripcion = u''
        descripcion += 'idRegla: '+self.idRegla+'\n'
        descripcion += 'Tipo: '+self.tipo+'\n'
        descripcion += 'Atributo: '+self.atributo.nombre+'\n'
        if isinstance(self.valorEsperado, str):
            descripcion += 'Valor esperado: '+self.valorEsperado+'\n'
        elif isinstance(self.valorEsperado, int) or isinstance(self.valorEsperado, float):
            descripcion += 'Valor esperado: '+str(self.valorEsperado)+'\n'
        elif isinstance(self.valorEsperado, list):
            for ve in self.valorEsperado:
                descripcion += 'Valor esperado: '+str(self.valorEsperado)+'  '

        return descripcion

class Objeto():
    def __init__(self, identificador, caracteristicas):
        print('Se va a crear')
        self.identificador = identificador
        self.caracteristicas = caracteristicas
        self.clase = None
        print('Objeto creado')
        pass

    def describeObjeto(self):
        print('Identificador= ', self.identificador)
        for ct in self.caracteristicas:
            print(ct.atributo.nombre, ct.atributo.tipo,
                  ct.valor, ct.atributo.unidad)

class Atributo():

    def __init__(self, nombre, tipo, unidad):
        self.nombre = nombre
        self.tipo = tipo
        self.unidad = unidad


class Caracteristica():

    def __init__(self, atributo, valor):
        self.atributo = atributo
        self.valor = valor

def clases():

    mercedes_AMG_SL = Mercedes_AMG_SL()
    bMW_iX3 = BMW_iX3()
    audi_A5 = Audi_A5()
    lClases = [mercedes_AMG_SL, bMW_iX3, audi_A5]
    return lClases


def creaCaracteristicas(lct=[[Atributo('diametro', 'int', 'cm'), 30]]):
    print(lct)
    carats = []
    for ct in lct:
        caract = Caracteristica(ct[0], ct[1])
        carats.append(caract)
    return carats


def creaAtributosBC(lat=[('atAS', 'int', 'mm')]):
    ats = []
    for at in lat:
        nat = Atributo(at[0], at[1], at[2])
        ats.append(nat)
    return ats


def buscaReglaComparableEnUnaClase(ct, clase):
    for r in clase.reglas:
        print(r.atributo.nombre, ct.atributo.nombre)
        if r.atributo.nombre == ct.atributo.nombre:
            rb = r
            break

    print(rb.atributo.nombre)
    return rb