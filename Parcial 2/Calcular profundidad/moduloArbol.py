from graphviz import Digraph
class Arbol:
   __dato : object
   __izquierda : object
   __derecha : object
   
   def __init__(self, dato) -> None:
      self.__dato = dato
      self.__izquierda : Arbol = None
      self.__derecha : Arbol = None
   
   def getIzquierda(self):
      return self.__izquierda
   
   def getDerecha(self):
      return self.__derecha
   
   def getDato(self):
      return self.__dato
   
   def setDerecha(self, nodo):
      self.__derecha = nodo
   
   def insertar(self, dato):
      if dato < self.__dato:
         if self.__izquierda == None:
            self.__izquierda = Arbol(dato)
         else:   
            self.__izquierda.insertar(dato)
      elif dato > self.__dato:
         if self.__derecha == None:
            self.__derecha = Arbol(dato)
         else:   
            self.__derecha.insertar(dato)
      else:
         print("El dato ya existe en el arbol")
   
   def profundidad(self, dato):
      if dato == self.__dato:
         return 0
      elif dato < self.__dato and self.__izquierda != None:
         return 1 + self.__izquierda.profundidad(dato)
      elif dato > self.__dato and self.__derecha != None:
         return 1 + self.__derecha.profundidad(dato)
      return None
   
   def buscar(self, dato):
      if dato == self.__dato:
         return self
      elif dato < self.__dato and self.__izquierda != None:
         return self.__izquierda.buscar(dato)
      elif dato > self.__dato and self.__derecha != None:
         return self.__derecha.buscar(dato)
      return None
   
   def calcularDecendientes(self, dato):
      if dato == self.__dato:
         return self.cantidadDecendientes()
      elif dato < self.__dato and self.__izquierda != None:
         return self.__izquierda.buscar(dato)
      elif dato > self.__dato and self.__derecha != None:
         return self.__derecha.buscar(dato)
      return None
  
  
   def cantidadDecendientes(self):
      if self.__izquierda == None and self.__derecha == None:
         return 0
      elif self.__izquierda == None and self.__derecha != None:
         return 1 + self.__derecha.cantidadDecendientes()
      elif self.__derecha == None:
         return 1 + self.__izquierda.cantidadDecendientes()
      else:
         return 2 + self.__izquierda.cantidadDecendientes() + self.__derecha.cantidadDecendientes()
      
   def nodosHojas(self):
      if self.__izquierda != None:
         self.__izquierda.nodosHojas()
      if self.__izquierda == None and self.__derecha == None:
         print(self.__dato)
      if self.__derecha != None:
         self.__derecha.nodosHojas()
   
   def visualizar(self, nombre):
        dot = Digraph() # crea el objeto
        self.__visualizar(dot, self) # llama la funcion recursiva
        filename = f'arbol-{nombre}' # crea un nombre unico para cada imagen
        dot.render(filename, format='png', cleanup=True)  # Guarda el gráfico como 'arbol.png'
       

   def __visualizar(self, dot, nodo):
      if nodo is not None:
         label = f'{nodo.getDato()}' # crea el string para el nodo
         # dot.node(str(nodo.getDato()), str(nodo.getDato()), shape='circle')
         dot.node(str(nodo.getDato()), label, shape='circle') # crea el nodo con su ID y etiqueta
         if nodo.getIzquierda() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getIzquierda().getDato()))
               self.__visualizar(dot, nodo.getIzquierda())
         if nodo.getDerecha() is not None:
               dot.edge(str(nodo.getDato()), str(nodo.getDerecha().getDato()))
               self.__visualizar(dot, nodo.getDerecha())
   
   
   def buscarMayor(self, anterior):
      if self.__derecha != None:
         return self.__derecha.buscarMayor(self)
      else:
         anterior.setDerecha(self.__izquierda)
         return self.__dato      
   
   def suprimir(self, dato):
      if dato == self.__dato:
         datoAuxiliar = self.__izquierda.buscarMayor(self)
         self.__dato = datoAuxiliar
      elif dato < self.__dato and self.__izquierda != None:
         return self.__izquierda.suprimir(dato)
      elif dato > self.__dato and self.__derecha != None:
         return self.__derecha.suprimir(dato)
      return None