# ==============================================================================
# Problema 2: Gestión de Menú de Restaurante con Promoción
# ==============================================================================

# Precios base de referencia del menú del restaurante
PRECIOS_REFERENCIA = {
    "bandeja paisa": 35000,
    "churrasco": 42000,
    "pasta boloñesa": 24000,
    "pasta bolonesa": 24000,
    "empanadas": 12000,
    "empanadas x4": 12000,
    "ceviche": 28000,
    "ceviche de camarón": 28000,
    "ceviche de camaron": 28000,
    "limonada": 11000,
    "limonada de coco": 11000,
    "cheesecake": 16000,
    "cheesecake de maracuyá": 16000,
    "cheesecake de maracuya": 16000,
    "hamburguesa": 26000,
    "pizza": 30000,
    "jugo natural": 9000,
    "gaseosa": 6000,
    "helado": 12000,
    "sopa del día": 15000,
    "sopa": 15000
}


def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral_precio):
    """
    Calcula el precio final de un producto aplicando un 15% de descuento si:
    - Pertenece a la categoría objetivo previamente definida, Y
    - Tiene un precio base mayor al umbral establecido.
    En caso contrario, mantiene el precio base.
    """
    if categoria.strip().lower() == categoria_objetivo.strip().lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        return precio_base - descuento
    return precio_base


def ingresar_productos(minimo_productos=6):
    """
    Solicita al usuario ingresar al menos 6 productos por teclado y
    retorna la matriz con formato: [Nombre del producto, Categoría, Precio base].
    Muestra el precio sugerido del producto y permite aceptarlo con Enter o escribir otro.
    """
    menu = []
    print("=" * 72)
    print(f"       REGISTRO DEL MENÚ (Mínimo {minimo_productos} productos de distintas categorías)")
    print("=" * 72)
    print("Productos de ejemplo con precio automático:")
    print(" - Platos Fuertes : Bandeja Paisa ($35,000), Churrasco ($42,000), Pasta Boloñesa ($24,000)")
    print(" - Entradas       : Empanadas ($12,000), Ceviche ($28,000)")
    print(" - Bebidas        : Limonada ($11,000), Jugo Natural ($9,000)")
    print(" - Postres        : Cheesecake ($16,000), Helado ($12,000)")
    print("-" * 72)

    contador = 1
    while True:
        print(f"\n--- Producto #{contador} ---")
        nombre = input("Nombre del producto: ").strip()
        while not nombre:
            nombre = input("El nombre no puede estar vacío. Nombre del producto: ").strip()

        categoria = input("Categoría (ej. Platos Fuertes, Entradas, Bebidas, Postres): ").strip()
        while not categoria:
            categoria = input("La categoría no puede estar vacía. Categoría: ").strip()

        # Buscar si el producto tiene un precio base automático en la carta
        precio_sugerido = PRECIOS_REFERENCIA.get(nombre.lower(), 20000)
        print(f"-> Precio base del producto '{nombre}': ${precio_sugerido:,.2f}")

        while True:
            entrada_precio = input(
                f"Presione ENTER para usar ${precio_sugerido:,.0f} o escriba otro precio base: "
            ).strip()

            if entrada_precio == "":
                precio_base = float(precio_sugerido)
                break

            try:
                precio_base = float(entrada_precio)
                if precio_base < 0:
                    print("El precio no puede ser negativo. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("Entrada inválida. Ingrese un valor numérico o presione ENTER.")

        # Agregar fila a la matriz: [Nombre del producto, Categoría, Precio base]
        menu.append([nombre, categoria, precio_base])
        print(f"Registrado: [{nombre}, {categoria}, ${precio_base:,.2f}]")
        contador += 1

        # Verificar si ya se alcanzó el mínimo de 6 productos
        if len(menu) >= minimo_productos:
            continuar = input("\n¿Desea ingresar otro producto? (s/n): ").strip().lower()
            if continuar != 's':
                break

    return menu


def main():
    # 1. Crear la matriz con al menos 6 productos
    menu = ingresar_productos(6)

    print("\n" + "=" * 72)
    print("            CONFIGURACIÓN DE PROMOCIÓN DEL RESTAURANTE")
    print("=" * 72)

    # Mostrar las categorías que el usuario ingresó para facilitarle la elección
    categorias_registradas = sorted(list(set(p[1] for p in menu)))
    print("Categorías registradas en el menú:", ", ".join(categorias_registradas))

    # Solicitar categoría objetivo y umbral de precio por teclado (input)
    categoria_objetivo = input(
        "Ingrese la categoría objetivo para el 15% de descuento (Enter = 'Platos Fuertes'): "
    ).strip()
    if not categoria_objetivo:
        categoria_objetivo = "Platos Fuertes"

    while True:
        entrada_umbral = input(
            "Ingrese el umbral de precio base mínimo (Enter = 25000): "
        ).strip()
        if not entrada_umbral:
            umbral_precio = 25000.0
            break
        try:
            umbral_precio = float(entrada_umbral)
            if umbral_precio < 0:
                print("Por favor, ingrese un valor positivo.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para el umbral.")

    # 2. Mostrar salida con Nombre, Precio base y Precio final
    print("\n" + "=" * 72)
    print("                 MENÚ DEL RESTAURANTE - PROMOCIONES")
    print("=" * 72)
    print(f"Promoción activa: 15% de descuento en '{categoria_objetivo}'")
    print(f"Condición: Precio base mayor a ${umbral_precio:,.2f}")
    print("-" * 72)
    print(f"{'Producto':<25} | {'Categoría':<16} | {'Precio Base':>12} | {'Precio Final':>12}")
    print("-" * 72)

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        precio_final = calcular_precio_final(
            categoria, precio_base, categoria_objetivo, umbral_precio
        )

        print(f"{nombre:<25} | {categoria:<16} | ${precio_base:>11,.2f} | ${precio_final:>11,.2f}")

    print("=" * 72)


if __name__ == "__main__":
    main()
