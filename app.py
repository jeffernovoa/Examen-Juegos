import gradio as gr
import random
from juegos.reinas.lanzador import resolver_n_reinas
from juegos.caballo.lanzador import resolver_caballo
from juegos.hanoi.lanzador import resolver_hanoi
import threading

# Función para N-Reinas
def jugar_n_reinas(n):
    try:
        soluciones = resolver_n_reinas(n)
        if soluciones:
            solucion = soluciones[0]
            resultado = f"Se encontraron {len(soluciones)} soluciones. Mostrando la primera:\n"
            resultado += "\n".join([f"Reina en fila {fila + 1}, columna {columna + 1}" for fila, columna in enumerate(solucion)])
        else:
            resultado = "No se encontraron soluciones para el número de reinas proporcionado."
        return resultado
    except Exception as e:
        return f"Error al resolver N-Reinas: {str(e)}"

# Función para el Problema del Caballo con límite de tiempo
def jugar_caballo():
    n = 8  # Tablero fijo de 8x8
    posicion_inicial = (random.randint(0, n - 1), random.randint(0, n - 1))
    resultado = []

    def resolver():
        nonlocal resultado
        resultado = resolver_caballo(n, posicion_inicial)

    # Crear un hilo para limitar el tiempo de ejecución
    hilo = threading.Thread(target=resolver)
    hilo.start()
    hilo.join(timeout=10)  # Límite de tiempo de 10 segundos

    if hilo.is_alive():
        return f"El cálculo tomó demasiado tiempo y fue interrumpido. Posición inicial: {posicion_inicial}"
    elif isinstance(resultado, str):
        return f"El caballo comienza en la posición: {posicion_inicial}\n{resultado}"
    elif resultado:
        recorrido = f"El caballo comienza en la posición: {posicion_inicial}\nRecorrido del caballo:\n"
        recorrido += "\n".join([f"Paso {paso}: ({fila}, {columna})" for paso, (fila, columna) in enumerate(resultado, start=1)])
        return recorrido
    else:
        return f"No se encontró un recorrido válido. Posición inicial: {posicion_inicial}"

# Función para Torres de Hanoi
def jugar_hanoi(n):
    try:
        movimientos = resolver_hanoi(n)
        resultado = "Secuencia de movimientos:\n"
        resultado += "\n".join([f"Mover de {mov[0]} a {mov[1]}" for mov in movimientos])
        return resultado
    except Exception as e:
        return f"Error al resolver Torres de Hanoi: {str(e)}"

# Crear la interfaz con Gradio
with gr.Blocks() as demo:
    gr.Markdown("# Juegos Interactivos")
    
    # N-Reinas
    with gr.Tab("N-Reinas"):
        gr.Markdown("### Resuelve el problema de las N-Reinas")
        n_reinas_input = gr.Number(label="Número de reinas", value=8, precision=0)
        n_reinas_output = gr.Textbox(label="Resultado")
        n_reinas_button = gr.Button("Resolver")
        n_reinas_button.click(jugar_n_reinas, inputs=n_reinas_input, outputs=n_reinas_output)
    
    # Problema del Caballo
    with gr.Tab("Problema del Caballo"):
        gr.Markdown("### Resuelve el problema del recorrido del caballo")
        caballo_output = gr.Textbox(label="Resultado")
        caballo_button = gr.Button("Generar Recorrido")
        caballo_button.click(jugar_caballo, inputs=None, outputs=caballo_output)
    
    # Torres de Hanoi
    with gr.Tab("Torres de Hanoi"):
        gr.Markdown("### Resuelve el problema de las Torres de Hanoi")
        hanoi_input = gr.Number(label="Número de discos", value=3, precision=0)
        hanoi_output = gr.Textbox(label="Resultado")
        hanoi_button = gr.Button("Resolver")
        hanoi_button.click(jugar_hanoi, inputs=hanoi_input, outputs=hanoi_output)

# Ejecutar la aplicación
if __name__ == "__main__":
    demo.launch()