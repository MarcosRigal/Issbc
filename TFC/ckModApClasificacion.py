#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trabajo Final de Curso ISBC

Aplicación Clasificador

En este fichero se almacena el modelo de la aplicación

Authors: Marcos Rivera Gavilan, Marcos Rodriguez Moreno, Moises Moyano Cejudo
Website: https://www.uco.es/~i92rigam/

Importante: Para reducir el número de comentarios,
y simplificar la lectura, solo comentaré las funciones
nuevas de este fichero. El resto que aparezcan sin
comentar, habrán sido comentadas en otros ficheros.
"""

import mcMotorcycles as mcf
import mcCars as mci


class Tarea():
    def __init__(self):
        self.objetivo = ''
        self.descripcion = ''
        pass


class Clasificacion(Tarea):
    def __init__(self, bc, objeto):
        self.objetivo = u'''    '''
        self.objeto = objeto
        self.bc = bc
        self.metodo = 'poda'
        self.salida = None

    def execute(self):
        print('Ejectutando la tarea')
        if self.metodo == 'poda':
            mt = MetodoPoda()
        pass


class MetodoPoda():

    def __init__(self, obj):
        self.obj = obj
        self.clasesCandidatas = []
        self.lAtributosUsados = []
        self.conjuntoNuevosValores = []
        self.explicacion = u''
        pass

    def execute(self, clasificacionDlg):
        g = Generar(self.obj)
        self.clasesCandidatas = g.execute(clasificacionDlg)
        self.explicacion += u'Se generan las clases candidatas que son:\n'
        for cc in self.clasesCandidatas:
            self.explicacion += cc.nombre+'\n'
        self.explicacion += '\n'
        newSolucion = True
        while newSolucion and len(self.clasesCandidatas) > 0:
            print('Inicio while-> Lista de atributos usados:',
                  self.lAtributosUsados)
            print('Clases candidatas:', self.clasesCandidatas)
            for clc in self.clasesCandidatas:
                print(clc.nombre)
            print('=======================')

            esp = Especificar(self.clasesCandidatas, self.lAtributosUsados)
            newLatr = esp.execute()

            if not newLatr == (None, None):
                self.lAtributosUsados = newLatr[1]
                print('new atributo seleccionado:', newLatr[0].nombre)
                for atu in self.lAtributosUsados:
                    print(atu.nombre)

                print
                self.explicacion += 'Seleccionamos  el atributo ' + \
                    newLatr[0].nombre+' '
                obt = Obtener(self.obj, newLatr[0])
                at = obt.execute()
                print(at)
                print('=======================')
                print('Atributo y valor atributo del objeto:',
                      at.atributo.nombre, at.valor)
                print('========================')

                self.explicacion += 'con el valor: '
                if not isinstance(at.valor, str):
                    self.explicacion += str(at.valor)+'\n'
                else:
                    self.explicacion += at.valor+'\n'

                self.conjuntoNuevosValores.append(at)

                newcc = []
                for cc in self.clasesCandidatas:
                    pass
                    self.explicacion += '    Probamos la clase candidata '+cc.nombre+'\n'
                    print
                    print('Probamos a equiparar la clase: ', cc.nombre)
                    print(' con el conjunto de nuevos pares atributos/valores: ')
                    for cnv in self.conjuntoNuevosValores:
                        print(cnv.atributo.nombre, '=', cnv.valor)
                    print('==================================')
                    print
                    eq = Equiparar(cc, self.conjuntoNuevosValores)
                    result, expl = eq.execute()
                    self.explicacion += expl

                    self.explicacion += '      Resultado de equiparar clase candidata ' + \
                        cc.nombre+' '+str(result)+'\n'
                    print('Resultado de equiparar la clase:', cc.nombre, result)
                    print
                    if result == True:
                        newcc.append(cc)
                        print('Clase aceptada:', cc.nombre)

            else:
                print('No quedan más atributos por especificar')
                print
                newSolucion = False
                continue
            print
            self.clasesCandidatas = newcc
            self.explicacion += u'\n Clases candidatas tras la equiparación: '
            for cc in self.clasesCandidatas:
                self.explicacion += ' '+cc.nombre+'  '
                self.explicacion += '\n'+cc.descripcion()+'\n'
            self.explicacion += '\n'

        return self.clasesCandidatas, self.explicacion


class Inferencia():
    def __init__(self):
        pass

    def execute(self):
        pass


class Equiparar(Inferencia):

    def __init__(self, candidata, nuevosValores):
        Inferencia.__init__(self)
        self.candidata = candidata
        self.nuevosValores = nuevosValores
        self.explicacion = u''

    def execute(self):

        print
        print('====================================')
        print('Ejecución de la inferencia equiparar')
        print('=====================================')
        print

        for nv in self.nuevosValores:
            print('Equiparando el atributo/valor del objeto:',
                  nv.atributo.nombre, '=', nv.valor)
            print('Con la clase candidata ', self.candidata.nombre)

            self.explicacion += '\t Equiparar el atributo '+nv.atributo.nombre+'= '
            if not isinstance(nv.valor, str):
                self.explicacion += str(nv.valor)+'\n '
            else:
                self.explicacion += nv.valor+'\n '

            for r in self.candidata.reglas:
                print('Nombre y tipo  de la regla:', r.idRegla, r.tipo)
                if r.atributo.nombre == nv.atributo.nombre:
                    if r.tipo == 'igual':
                        print('Compara valor del atributo en la regla',
                              r.valorEsperado, nv.valor)
                        if r.valorEsperado == nv.valor:
                            continue
                        else:
                            return False, self.explicacion
                    if r.tipo == 'rango':
                        print('Evaluo rango')
                        if nv.valor < r.valorEsperado[1] and nv.valor >= r.valorEsperado[0]:
                            continue
                        else:
                            return False, self.explicacion
                else:
                    print('Regla no aplicable a este atributo\n')
        return True, self.explicacion


class Generar(Inferencia):

    def __init__(self, objeto):
        Inferencia.__init__(self)
        self.objeto = objeto

    def execute(self, clasificacionDlg):
        print('===================================')
        print('Ejecución de la inferencia generar')
        print('===================================')
        print
        if clasificacionDlg.comboboxWidgetDominio.currentText() == 'Coches':
            clases = mci.clases()
        else:
            clases = mcf.clases()

        return clases


class Obtener(Inferencia):

    def __init__(self, objeto, atributo):
        Inferencia.__init__(self)
        self.objeto = objeto
        self.atributo = atributo

    def execute(self):
        print
        print('Ejecución de la inferencia obtener')
        print('==================================')
        print
        for cat in self.objeto.caracteristicas:
            if self.atributo.nombre == cat.atributo.nombre:
                return cat
        return None


class Especificar(Inferencia):

    def __init__(self, clasesCandidatas, lAtributosUsados):
        Inferencia.__init__(self)
        self.cc = clasesCandidatas
        self.lAtributosUsados = lAtributosUsados
        pass

    def execute(self):
        print('=================================')
        print('Inferencia especificando atributo')
        print('=================================')
        print
        if len(self.cc) > 0:
            clase = self.cc[0]
            for at in clase.atributos:
                if not at.nombre in [atu.nombre for atu in self.lAtributosUsados]:
                    self.lAtributosUsados.append(at)
                    return (at, self.lAtributosUsados)
            return None, None
