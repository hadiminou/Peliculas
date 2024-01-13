from peliculas import*

def test_lee_peliculas(datos:list[Pelicula]):
    print("\n1.test_lee_peliculas")
    print(f"total registros leidos: {len(datos)}")
    print(f"mostrando los tres primeros: {datos[:3]}")

def test_pelicula_mas_ganancias(datos:list[Pelicula]):
    print("\n2.test_pelicula_mas_ganancias")
    print("genero = None")
    print(pelicula_mas_ganancias(datos))
    print("genero = Drama")
    print(pelicula_mas_ganancias(datos, "Drama"))

def test_media_presupuesto_por_genero(datos:list[Pelicula]):
    print("\n3.test_media_presupuesto_por_genero")
    print(media_presupuesto_por_genero(datos))

def test_peliculas_por_actor(datos:list[Pelicula]):
    print("\n4.test_peliculas_por_actor")
    print("ano inicial = None , ano final = None")
    print(peliculas_por_actor(datos))
    ano_inicial = 2010
    ano_final = 2020
    print(f"\nano inicial = {ano_inicial} , ano final = {ano_final}")
    print(peliculas_por_actor(datos, ano_inicial, ano_final))

def test_actores_mas_frecuentes(datos:list[Pelicula]):
    print("\n5.test_actores_mas_frecuentes")
    print(actores_mas_frecuentes(datos, 3, 2005, 2015))

def test_recaudacion_total_por_ano(datos:list[Pelicula]):
    print("\n6.test_recaudacion_total_por_ano")
    print("generos = None")
    print(recaudacion_total_por_ano(datos))
    generos = {'Drama', 'Acción'}
    print(f"\ngeneros = {generos}")
    print(recaudacion_total_por_ano(datos, generos))

def test_incrementos_recaudacion_por_ano(datos:list[Pelicula]):
    print("\n7.test_incrementos_recaudacion_por_ano")
    print("generos = None")
    print(incrementos_recaudacion_por_ano(datos))
    generos = {'Drama', 'Acción'}
    print(f"\ngeneros = {generos}")
    print(incrementos_recaudacion_por_ano(datos, generos))

if __name__ == "__main__":
    datos = lee_peliculas("data\peliculas.csv")
    test_lee_peliculas(datos)
    test_pelicula_mas_ganancias(datos)
    test_media_presupuesto_por_genero(datos)
    test_peliculas_por_actor(datos)
    test_actores_mas_frecuentes(datos)
    test_recaudacion_total_por_ano(datos)
    test_incrementos_recaudacion_por_ano(datos)