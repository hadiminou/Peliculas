from collections import namedtuple, defaultdict
from datetime import date, time, datetime
import csv

Pelicula  =  namedtuple("Pelicula",  "fecha_estreno,  titulo,  director,  generos,  duracion, \
presupuesto, recaudacion, reparto")

def parser(cadena:str)->list[str]:
    return [elem.strip() for elem in cadena.split(",")]

def lee_peliculas(fichero:str)->list[Pelicula]:
    res = []
    with open(fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ';')
        next(lector)
        for fecha_estreno,  titulo,  director,  generos,  duracion, presupuesto, recaudacion,\
            reparto in lector:
            fecha_estreno = datetime.strptime(fecha_estreno, "%d/%m/%Y").date()
            generos = parser(generos)
            duracion = int(duracion)
            presupuesto = int(presupuesto)
            recaudacion = int(recaudacion)
            reparto = parser(reparto)
            res.append(Pelicula(fecha_estreno,  titulo,  director,  generos,  duracion, \
            presupuesto, recaudacion, reparto))
    return res

def pelicula_mas_ganancias(peliculas:list[Pelicula], genero:str=None)->tuple[str, int]:
    aux = defaultdict(int)
    aux = {i.titulo: i.recaudacion-i.presupuesto for i in peliculas if genero == None or genero in i.generos}
    return max(aux.items(), key = lambda e:e[1])

def media_presupuesto_por_genero(peliculas:list[Pelicula])->dict[str, float]:
    aux = defaultdict(list)
    res = defaultdict(float)
    for i in peliculas:
        for g in i.generos:
            aux[g].append(i.presupuesto)
    return {c: sum(v)/len(v) for c,v in aux.items()}

def peliculas_por_actor(peliculas:list[Pelicula], ano_i:int=None, ano_f:int=None)->dict[str, int]:
    res = defaultdict(int)
    for i in peliculas:
        for actor in i.reparto:
            if (ano_i == None or ano_i <= i.fecha_estreno.year) and \
                (ano_f == None or i.fecha_estreno.year <= ano_f):
                res[actor]+=1
    return res

def actores_mas_frecuentes(peliculas:list[Pelicula], n:int, ano_i:int=None, ano_f:int=None)->list[str]:
    return sorted([i[0] for i in sorted(peliculas_por_actor(peliculas, ano_i, ano_f).items(),\
        key = lambda e:e[1], reverse = True)[:n]])

def recaudacion_total_por_ano(peliculas:list[Pelicula], generos:set[str]=None)->dict[int, int]:
    res = defaultdict(int)
    for i in peliculas:
        if generos == None:
            res[i.fecha_estreno.year]+=i.recaudacion
        if generos != None:
            for genero in generos.intersection(i.generos):
                res[i.fecha_estreno.year]+=i.recaudacion
    return res

def incrementos_recaudacion_por_ano(peliculas:list[Pelicula], generos:set[str]=None)->list[int]:
    lista = sorted(recaudacion_total_por_ano(peliculas, generos).items())
    return [tupla2[1]-tupla1[1] for tupla1, tupla2 in zip(lista, lista[1:])]