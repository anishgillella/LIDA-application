
# LIDA Application

Welcome to the LIDA Application repository! This web application uses Streamlit, LIDA, and OpenAI's GPT or Hugging Face models to provide functionalities for summarizing data and generating visualizations based on user queries. It's designed to help users interactively explore data through a simple and intuitive interface.

## Features

- **Data Summarization**: Summarizes CSV files to extract and present key information.
- **Question-Based Graphs**: Generates visual graphs based on textual queries, providing a dynamic way to visualize data insights.
- **Interactive Web UI**: Built with Streamlit for a seamless user experience, allowing easy file uploads and immediate feedback.

## Prerequisites

Before setting up the project, ensure you have the following:
- Python 3.6+
- Pip

## Installation

Clone the repository and install the required packages using these steps:

1. **Clone the Repository**
    ```bash
    git clone https://github.com/anishgillella/LIDA-application.git
    cd LIDA-application
    ```

2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Environment Setup**
    - Create a `.env` file in the root directory.
    - Populate it with your OpenAI API key:
      ```
      OPENAI_API_KEY=your_openai_api_key_here
      ```

## Usage

Run the application using the following command:

```bash
streamlit run app.py
```

Open your web browser and go to `http://localhost:8501` to use the app.

### How to Use the App

- **Summarize**: Upload your CSV file through the web interface to get a summarized version of your data along with key goals.
- **Question Based Graph**: After uploading a CSV, you can input a query related to the data which will generate a graph based on your query, visualizing the data as per the input specifications.

## Contributing

We encourage contributions! If you have suggestions or improvements, please fork the repo and submit a pull request, or open an issue with the tags "enhancement" or "bug".

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Anish Gillella - email@example.com - feel free to contact me!

Project Link:(https://github.com/anishgillella/LIDA-application)
