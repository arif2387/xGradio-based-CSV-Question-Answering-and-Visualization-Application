import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load CSV file
def load_csv(file):
    try:
        df = pd.read_csv(file.name)
        return df
    except Exception as e:
        return str(e)

# Answer questions using Pandas
def query_csv(df, question):
    question = question.lower()

    if "average" in question or "mean" in question:
        column = question.split()[-1]
        if column in df.columns:
            return f"Average {column}: {df[column].mean():.2f}"
    
    if "max" in question:
        column = question.split()[-1]
        if column in df.columns:
            return f"Maximum {column}: {df[column].max()}"

    if "min" in question:
        column = question.split()[-1]
        if column in df.columns:
            return f"Minimum {column}: {df[column].min()}"
    
    return "I can answer queries like 'average price', 'max age', 'min salary' based on your dataset."

# Generate and save a graph
def visualize_data(df, column_x, column_y, chart_type):
    plt.figure(figsize=(6,4))
    if chart_type == "Bar Chart":
        sns.barplot(x=df[column_x], y=df[column_y])
    elif chart_type == "Line Chart":
        sns.lineplot(x=df[column_x], y=df[column_y])
    elif chart_type == "Scatter Plot":
        sns.scatterplot(x=df[column_x], y=df[column_y])
    
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(f"{chart_type} of {column_x} vs {column_y}")
    
    plt.savefig("plot.png")
    return "plot.png"

# Processing function for Gradio
def process_csv(file, question, column_x, column_y, chart_type):
    df = load_csv(file)
    if isinstance(df, str):
        return df, None
    
    answer = query_csv(df, question)
    plot_path = visualize_data(df, column_x, column_y, chart_type)
    
    return answer, plot_path

# Gradio UI
iface = gr.Interface(
    fn=process_csv,
    inputs=[
        gr.File(label="Upload CSV File"),
        gr.Textbox(label="Ask a Question"),
        gr.Textbox(label="X-Axis Column"),
        gr.Textbox(label="Y-Axis Column"),
        gr.Radio(["Bar Chart", "Line Chart", "Scatter Plot"], label="Chart Type"),
    ],
    outputs=[
        gr.Textbox(label="CSV Answer"),
        gr.Image(label="Visualization"),
    ],
    title="xGradio CSV Insightsask basic data questions and answer ",
    description="Upload a CSV, ask basic data questions, and visualize the data."
)

# Use Render's dynamic port
port = int(os.environ.get("PORT", 10000))
iface.launch(server_name="0.0.0.0", server_port=port)
