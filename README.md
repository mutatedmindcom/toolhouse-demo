# 💬 Toolhouse Playground

The Toolhouse Playground allows you to test [Toolhouse](https://toolhouse.ai) across with any LLM you like.

### How to run it on your own machine

1. Prepare environment variables

   ```shell 
   echo "OPENAI_API_KEY=<your-api-key>
   TOOLHOUSE_API_KEY=<your-api-key>" > .env
   ```

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```
   or

   ```shell 
   poetry install
   ```

2. Run the app

   ```
   $ streamlit run toolhouse_streamlit.py
   ```
   
   or

   ```shell 
   poetry run streamlit run toolhouse_streamlit.py
   ```
