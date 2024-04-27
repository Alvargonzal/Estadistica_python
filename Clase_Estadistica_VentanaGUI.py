"""
Este es un ejercicio de programaciòn. Se desarrolla una Clase Estadistica 

aunque existe una libreria para ello. Se programan todos los modulos para que 

se impriman los resultados de una lista "muestra".

### Raúl Jiménnez  AKA Alvar_g  29/03/2024
"""
from tkinter import *
import os
#import tkinter as tk


ventana = Tk() # Iniciamos la ventana
ventana.geometry("400x400+80+80")
ventana.title("Estadistica General")
entrada =Entry()


class Estadistica:
    

    def suma(self,elementos):
        xsuma=0
        for x in elementos:
            xsuma= xsuma +x
        return xsuma
    

    def conteo(self,elementos):     
        cont = len(elementos)
        return cont
    
    
    def max(self,elementos):
        max = 0
        for x in elementos:
            if x > max:
                max= x
        return max
    
                
    def min(self,elementos):
        min = 1000000
        for x in elementos:
            if x < min:
                min= x
        return min
    
    
    def rango(self,elementos):  
         el_rango= self.max(elementos) - self.min(elementos)
         return el_rango
    
    
    def media(self,elementos):  
          
         la_media = self.suma(elementos) / self.conteo(elementos)
         return round(la_media)
    
    
    def mediana(self,elementos):
         total = self.conteo(elementos)  # Cuenta los elementos en la lista
         elementos.sort() # La ordena de menos a mayor
         el_medio = total/2
         
         if el_medio % 2 == 0:   # si es Par
              int(el_medio)
              mediana_1 = elementos[el_medio]
              mediana_2 = elementos[el_medio-1]
              la_mediana = (mediana_1 + mediana_2) / 2 
              return round(la_mediana)
         else:    # Si es Impar  
              return elementos[int(el_medio)]
         
         
    def moda(self, elementos):  
         valor_max = 0
             # valor maximo del elemento mas repetido
         elem_mas_rep = 0 
         elem_mas_rep_2 = 0 #  Almacena el segundo elemento o mas que se repitan elemento de la lista que mas se repite
         lista_valores_max = []  # la lista vacia donde se introduciran los valores maximos
         
         for busqueda_elem in elementos:  # Buscamos el elemento que más se repite
            
            valor_lista = busqueda_elem    # va recorriendo elemento a elemento
            valor_repeticion = elementos.count(valor_lista)  # nos da el valor de repeticion del elemento
                    
            if valor_repeticion > valor_max :   # comprueba si es el mas repetido
                valor_max = valor_repeticion
                elem_mas_rep = valor_lista

         lista_valores_max.append(elem_mas_rep)

         for busqueda_elem_2 in elementos: # Buscamos si hay mas elementos se se repitan tanto como el primero
            valor_lista_2 = busqueda_elem_2  # va recorriendo elemento a elemento
            valor_repeticion_2 = elementos.count(valor_lista_2)  # nos da el valor de repeticion del elemento            

            if  valor_repeticion_2 == valor_max and not(valor_lista_2 in lista_valores_max): 
                    elem_mas_rep_2 = valor_lista_2
                    lista_valores_max.append(elem_mas_rep_2)  #introducimos los valores en la lista de maximos   

        #  La impresion
         print("Moda: ", end="") # end="" sirve para que la proxima impresión se haga a continuación de esta
         Label(ventana,text="Moda:").pack()
         for y in lista_valores_max:
             
             print(f" ( {y}, {valor_max} )", end=" ")
             Label(ventana, text=f" ( {y}, {valor_max} )").pack()
        
    
    

    def varianza(self, elementos):
        elementos_diferencia = []
        nuestra_media= self.media(elementos)
                
        for valores_muestra in elementos:
            difencias_muestras = abs(valores_muestra - nuestra_media)
            elementos_diferencia.append(difencias_muestras)

        elementos_cuadrado = []

        for muestras in elementos_diferencia:
            el_cuadrado = muestras ** 2
            elementos_cuadrado.append(el_cuadrado)
        
        Suma_cuadrados = sum(elementos_cuadrado)
        mi_varianza = Suma_cuadrados / (self.conteo(elementos))
        return round(mi_varianza,1)
    

    def desviacion_estandar(self, elementos):
        la_varianza = self.varianza(elementos)
        mi_desviacion = la_varianza ** 0.5  # Hacemos la raiz cuadrada (elevado a 1/2)
        return round(mi_desviacion, 1)
    

    
    def frecuencia_absoluta(self, elementos): 
        lista_valores_unicos = []
        el_unico = 0 
        elementos.sort()
        for datos_unicos in elementos:  # buscamos los valores sin repetir
            if datos_unicos > el_unico and not(datos_unicos in lista_valores_unicos):
                el_unico = datos_unicos
                lista_valores_unicos.append(el_unico)

        lista_valores_repes = []

        for datos_repes in lista_valores_unicos: # De los datos sin repetir contamos cuantas veces aparecen el la lista original
            cantidad_elemento = elementos.count(datos_repes)
            lista_valores_repes.append(cantidad_elemento)
        
        print(f"Frecuencia absoluta: ", end=" ")
        Label(ventana,text="Frecuencia Absoluta:").pack()
       
        for index in range (0, len(lista_valores_unicos)):
            print(f" ({lista_valores_unicos[index]}, {lista_valores_repes[index]} )", end=" ")
            Label(ventana, text=f"({lista_valores_unicos[index]}, {lista_valores_repes[index]} )").pack()
            
            

        print(f"\nFrecuencia relativa en % ", end=" ")
        Label(ventana,text="Frecuencia Relativa %:").pack()
        
        for index in range (0, len(lista_valores_unicos)):
            print(f" ({lista_valores_unicos[index]}, {round(lista_valores_repes[index] / self.conteo(elementos)*100, 1)} )", end=" ")
            Label(ventana, text=f"({lista_valores_unicos[index]}, {round(lista_valores_repes[index] / self.conteo(elementos)*100, 1)} )").pack()
            
        
        
     
        
        

    def descripcion(self,elementos):
         print (f" \n\n  Datos Estadisticos de la Muestra entregada (datos)\n")
         print (f"suma: {self.suma(elementos)}")
         print (f"Conteo: {self.conteo(elementos)}")
         print (f"Max: {self.max(elementos)}")
         print (f"Min: {self.min(elementos)}")
         print (f"Rango: {self.rango(elementos)}")
         print (f"Media: {self.media(elementos)}")
         print (f"Mediana: {self.mediana(elementos)}")
         print (self.moda(elementos))
         print (f"Varianza: {self.varianza(elementos)}")
         print (f"Desviación estandar: {self.desviacion_estandar(elementos)}")
         print (self.frecuencia_absoluta(elementos))



reg = Estadistica() # instaciamos reg como de la clase Estadistica
      # datos de muestra 
datos= [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26,]   


"""
Configuracion de la ventana para tomar datos y mostrar las estadisticas
"""


mi_lista_int =[]

def entry():
    mis_datos_ventana_str= int(entrada.get())
    mi_lista_int.append(mis_datos_ventana_str)
    
    print(mi_lista_int)
    return mi_lista_int


def imprimir():   #impresion en la ventana GUI
    mi_lista_extraida = entry()

    Label(ventana,text=f" Datos Estadisticos de la Muestra entregada (datos)").pack()
    Label(ventana,text=f" De la Muestra {mi_lista_extraida}").pack()
    Label(ventana, text=f"suma: {reg.suma(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Conteo: {reg.conteo(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Max: {reg.max(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Min: {reg.min(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Rango: {reg.rango(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Media: {reg.media(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Mediana: {reg.mediana(mi_lista_extraida)}").pack()   
    Label(ventana,text=(f"{reg.moda(mi_lista_extraida)}")).pack()
    Label(ventana,text=f"Varianza: {reg.varianza(mi_lista_extraida)}").pack()
    Label(ventana,text=f"Desviación estandar: {reg.desviacion_estandar(mi_lista_extraida)}").pack()
    Label(ventana,text=f"{reg.frecuencia_absoluta(mi_lista_extraida)}").pack()


Label(ventana, text="                                                                      ").pack()#grid(column=0, row=0)
Label(ventana, text="Este programa calcula los elentos estadisdisticos de una muestra dada.").pack()#grid(column=0, row=1)
Label(ventana, text="Introduce un nº y pulsa el botón").pack()#grid(column=0, row=2)

Boton_1=Button(ventana, text="Introducir", command=entry)
Boton_1.pack()

entrada =Entry()
entrada =Entry(ventana)

entrada.insert(0, "Introduce nº")
entrada.bind(("<Button-1>",lambda e:entrada.delete(0,END)))
entrada.pack()

Label(ventana, text="                                                                      ").pack()

Boton_2 = Button(ventana, text="Pulsa para calcular", command=imprimir)
Boton_2.pack()


ventana.mainloop()   # Hace el bucle para tener la venta abierta

 

print(reg.descripcion(datos))






