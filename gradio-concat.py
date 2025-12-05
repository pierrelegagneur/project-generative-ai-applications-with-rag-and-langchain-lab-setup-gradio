import gradio as gr
from huggingface_hub import HfFolder

def concat(sentence1, sentence2):
    return f"{sentence1} {sentence2}"

# Define the interface
demo = gr.Interface(
    fn=concat, 
    inputs=[
        gr.Textbox(label="Input 1"),
        gr.Textbox(label="Input 2")
        ], 
    outputs =gr.Textbox(label="Output") 
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)