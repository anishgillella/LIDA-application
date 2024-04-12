import streamlit as st  # Importing Streamlit for building web apps
from lida import Manager, TextGenerationConfig, llm  # Import LIDA library components
from dotenv import load_dotenv  # Import load_dotenv to load environment variables from .env
import os  # Import os for operating system interactions
import openai  # Import OpenAI's API library
from PIL import Image  # Import Image class from PIL for image processing
from io import BytesIO  # Import BytesIO for handling byte streams
import base64  # Import base64 for encoding/decoding base64 strings

# Load environment variables from the .env file
load_dotenv()
# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

def base64_to_image(base64_string):
    """Convert a base64 string to an image."""
    # Decode the base64 string into bytes
    byte_data = base64.b64decode(base64_string)
    # Convert byte data to an image
    return Image.open(BytesIO(byte_data))

# Initialize the LIDA Manager with a text generation model
lida = Manager(text_gen=llm("openai"))


#For using hugging face models
llm(provider = 'hf',model = "modelname",device_map = "auto")


# Configuration for text generation
textgen_config = TextGenerationConfig(n=1, temp=0.5, model='gpt-3.5-turbo-0301', use_cache=True)

# Streamlit sidebar for option selection
menu = st.sidebar.selectbox('Choose an Option', ['Summarize', 'Question based Graph'])

if menu == 'Summarize':
    # Subheader in Streamlit
    st.subheader("Summarization of your data")
    # File uploader widget in Streamlit
    file_uploader = st.file_uploader("Upload your file", type="csv")
    if file_uploader is not None:
        # Define the path where the uploaded file will be saved
        path_to_save = "filename.csv"
        # Write the content of the uploaded file to a new file
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())
        # Generate a summary of the uploaded file
        summary = lida.summarize("filename.csv", summary_method="default", textgen_config=textgen_config)
        st.write(summary)  # Display the summary in Streamlit
        goals = lida.goals(summary, n=2, textgen_config=textgen_config)
        for goal in goals:
            st.write(goal)  # Display each goal in Streamlit
        i = 0  # Index for selecting the first goal
        library = "seaborn"  # Specify the visualization library
        # Update text generation configuration for visualization
        textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
        # Generate visualization based on the summary and goal
        charts = lida.visualize(summary=summary, goal=goals[i], textgen_config=textgen_config, library=library)
        img_base64_str = charts[0].raster  # Base64 string of the first chart
        img = base64_to_image(img_base64_str)
        st.image(img)  # Display the image in Streamlit

elif menu == "Question based Graph":
    st.subheader("Query your data to Generate Graph")
    file_uploader = st.file_uploader("Upload your csv", type="csv")
    if file_uploader is not None:
        path_to_save = "filename1.csv"
        with open(path_to_save, "wb") as f:
            f.write(file_uploader.getvalue())

        text_area = st.text_area("Query your data to generate graph", height=200)
        if st.button("Generate button"):
            if len(text_area) > 0:
                st.info("Your query: " + text_area)
                lida = Manager(text_gen=llm("openai"))
                textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
                summary = lida.summarize("filename1.csv", summary_method="default", textgen_config=textgen_config)
                user_query = text_area
                charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
                image_base64 = charts[0].raster
                img = base64_to_image(image_base64)
                st.image(img)  # Display the generated graph image in Streamlit
