import gradio as gr

def mostrar_tablero(tablero):
    tablero_str = "\n".join([" ".join(str(c) for c in fila) for fila in tablero])
    return tablero_str

iface = gr.Interface(fn=mostrar_tablero, inputs="textbox", outputs="text")