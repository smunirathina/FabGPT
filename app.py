# -*- coding: utf-8 -*-

import gradio as gr
import plotly.express as px
import pandas as pd

def hello_plot():
    # Sample data
    df = pd.DataFrame({
        "Tool": ["Scanner-A", "Scanner-B", "Scanner-C"],
        "Errors": [12, 5, 18]
    })

    # Plotly chart
    fig = px.bar(df, x="Tool", y="Errors", title="Hello World FabGPT Chart")

    return "Hello World from FabGPT 🚀", fig


with gr.Blocks() as demo:
    gr.Markdown("# FabGPT Hello World Dashboard")

    btn = gr.Button("Generate Hello + Plotly Chart")

    text_out = gr.Textbox(label="Message")
    plot_out = gr.Plot(label="Plotly Output")

    btn.click(fn=hello_plot, outputs=[text_out, plot_out])

demo.launch(server_name="0.0.0.0", server_port=7860)
