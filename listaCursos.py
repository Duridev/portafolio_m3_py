catalogo = [
    {
        "id": 1,
        "nombre": "JavaScript Moderno Guía Definitiva Construye +20 Proyectos",
        "Categoria": "Javascript",
        "Horas": 53,
        "Nivel": "Básico",
        "precio": 9900,
    },
    {
        "id": 2,
        "nombre": "React y TypeScript - La Guía Completa Creando +10 Proyectos",
        "Categoria": "React",
        "Horas": 58,
        "Nivel": "Básico",
        "precio": 9900
    },
    {
        "id": 3,
        "nombre": "Vue.js 3 - La Guía Completa - Composition Pinia MEVN 10 Apps",
        "Categoria": "Vue",
        "Horas": 41,
        "Nivel": "Básico",
        "precio": 9900
    },
    {
        "id": 4,
        "nombre": "Full Stack Node.js React TS NestJS Next.js Creando Proyectos",
        "Categoria": "Fullstack",
        "Horas": 46,
        "Nivel": "Intermedio",
        "precio": 9900
    },
    {
        "id": 5,
        "nombre": "React Native - Crea aplicaciones para Android y iOS c/ React",
        "Categoria": "Movil",
        "Horas": 29,
        "Nivel": "Intermedio",
        "precio": 9900
    },
]

carrito_de_compras = []

estado = True




def menu():
    print("\n***** Bienvenido a tu Ecommerce *****\n")
    print("""
    1) Ver catálogo de productos 
    2) Buscar producto por nombre o categoría 
    3) Agregar producto al carrito 
    4) Ver carrito y total 
    5) Vaciar carrito 
    0) Salir 
    """)
    return int(input("Elige la opción que necesitas: "))

def opcion(op):
    if op == 1:
        ver_catalogo()
    elif op == 2:
        pass
    elif op == 3:
        agregar_producto_al_carrito(catalogo)
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 0:
        estado = False

def ver_catalogo():
    #print(*catalogo, sep="\n")
    n = 1
    for curso in catalogo:
        print(f""" **** Curso N{n}
id: {curso["id"]}
nombre: {curso["nombre"]}
Categria: {curso["Categoria"]}
Horas: {curso["Horas"]}
Nivel: {curso["Nivel"]}
precio: {curso["precio"]}
""")
        n += 1





#while estado:
 