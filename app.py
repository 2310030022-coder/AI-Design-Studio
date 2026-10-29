"""AI Design Studio | OpenAI text-to-image + Gradio."""
import os
import io
import base64
import gradio as gr
from PIL import Image
from openai import OpenAI, OpenAIError

MODEL = os.getenv('OPENAI_IMAGE_MODEL', 'gpt-image-2.5-flare')
STYLE_HINTS = {
    'Cinematic': 'cinematic composition, dramatic lighting, professional movie key art',
    'Neon Futuristic': 'vibrant neon magenta and cyan, futuristic sci-fi design, high contrast',
    'Minimalist': 'clean modern design, refined typography-safe negative space, elegant shapes',
    'Fantasy': 'magical fantasy illustration, glowing accents, dramatic atmospheric lighting',
    'Luxury': 'luxury editorial advertisement, premium gold accents, elegant art direction',
}
SIZES = {'Square (social post)': '1024x1024', 'Landscape (banner)': '1536x1024', 'Portrait (poster)': '1024x1536'}

def generate_image(prompt, style, layout):
    """Generate one image from a prompt; keep secrets server-side."""
    if not prompt or not prompt.strip():
        raise gr.Error('Enter a design prompt before generating an image.')
    key = os.getenv('OPENAI_API_KEY', '').strip()
    if not key:
        raise gr.Error('OPENAI_API_KEY is missing. Configure it as a private environment variable or Colab secret.')
    composed = (
        f'Create a professional promotional poster or marketing banner. {prompt.strip()}. '
        f'Art direction: {STYLE_HINTS[style]}. '
        'Beautiful color palette, excellent composition, polished graphic design. '
        'No existing company logos or copyrighted characters unless explicitly authorized.'
    )
    try:
        client = OpenAI(api_key=key)
        response = client.images.generate(model=MODEL, prompt=composed, size=SIZES[layout], n=1)
        encoded = response.data[0].b64_json
        if not encoded:
            raise gr.Error('The API returned no image. Please try another prompt.')
        result = Image.open(io.BytesIO(base64.b64decode(encoded))).convert('RGB')
        return result, 'Image generated successfully. Use the image download icon to save it.'
    except OpenAIError as exc:
        # Do not print secrets or raw request headers.
        raise gr.Error(f'Image generation failed: {str(exc)[:250]}') from None

CSS = """
.gradio-container {max-width: 1180px !important; margin: auto !important;}
#hero {padding: 30px 28px; border-radius: 24px; margin-bottom: 18px; background: linear-gradient(115deg,#1d1144,#6029a6 55%,#d24f94); color: white; box-shadow:0 12px 35px #1a104933;}
#hero h1 {color:white !important; font-size: 35px !important; margin-bottom:8px;}
#hero p {color:#f4eaff !important;font-size:15px;}
#panel, #outputpanel {border:1px solid #d8caff; border-radius:20px; padding:18px; background:var(--block-background-fill);}
#generate {border-radius:14px !important; background:linear-gradient(100deg,#753af3,#ec4899) !important; color:white !important; border:0 !important; font-weight:700 !important;}
#footer {text-align:center; opacity:.8; font-size:12px; margin-top:20px;}
"""

def build_app():
    with gr.Blocks(title='AI Design Studio | Generative AI Poster Maker') as demo:
        gr.HTML('''<div id="hero"><div style="font-size:13px;letter-spacing:2px;font-weight:700;">✦ GENERATIVE AI CREATIVE LAB</div><h1>🎨 AI Design Studio</h1><p>Turn your idea into a stunning poster, campaign visual or banner with one prompt.</p></div>''')
        with gr.Row(equal_height=False):
            with gr.Column(scale=5, elem_id='panel'):
                gr.Markdown('### ✍️ Create your design')
                prompt = gr.Textbox(label='Describe your idea', placeholder='A futuristic sci-fi movie poster, neon skyline, dramatic violet lighting...', lines=5)
                style = gr.Dropdown(choices=list(STYLE_HINTS), value='Neon Futuristic', label='Visual style')
                layout = gr.Radio(choices=list(SIZES), value='Portrait (poster)', label='Canvas format')
                button = gr.Button('✨ Generate my design', variant='primary', elem_id='generate')
                gr.Examples(examples=[['A mysterious fantasy castle above the clouds, magical blue lights','Fantasy','Portrait (poster)'],['A colorful summer music festival banner with abstract shapes','Neon Futuristic','Landscape (banner)'],['Premium perfume advertisement with glass bottle on marble','Luxury','Square (social post)']], inputs=[prompt,style,layout], label='Try an example')
            with gr.Column(scale=6, elem_id='outputpanel'):
                gr.Markdown('### 🖼️ Your generated artwork')
                artwork = gr.Image(label='Preview and download', type='pil', interactive=False,  height=480)
                status = gr.Markdown('Your design will appear here after generation.')
        button.click(generate_image, inputs=[prompt,style,layout], outputs=[artwork,status])
        gr.HTML('<div id="footer">Made with Python · OpenAI Image API · Gradio | Course-End Project 2</div>')
    return demo

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    build_app().launch(
        server_name="0.0.0.0",
        server_port=port,
        theme=gr.themes.Soft(
            primary_hue="purple",
            secondary_hue="pink"
        ),
        css=CSS
    )
