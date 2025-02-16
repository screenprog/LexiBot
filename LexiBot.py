import os
import dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Create the model
def lexiBot(user_input: str ,history: list):
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }
  dotenv.load_dotenv()
  genai.configure(api_key=os.environ["GEMINI_API_KEY"])
  
  model = genai.GenerativeModel(
    model_name="learnlm-1.5-pro-experimental",
    generation_config=generation_config,
    safety_settings={
       HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT : HarmBlockThreshold.BLOCK_NONE,
       HarmCategory.HARM_CATEGORY_HARASSMENT : HarmBlockThreshold.BLOCK_NONE,
       HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT : HarmBlockThreshold.BLOCK_NONE,
       HarmCategory.HARM_CATEGORY_HATE_SPEECH : HarmBlockThreshold.BLOCK_NONE,
    },
    # here this is a system prompt
    system_instruction=
    """You are a language teacher and intended to teach multiple languages by providing a definition and examples \
  of use for any provided word or sentence.
  Things you have to keep in your mind:
    {
      1. Stay specific and to the point no jargon and no questions.
      2. Keep the definition simple and understandable, if requried use multiple definitions for different usecases.
      3. Give two examples and if required give more examples as well.
      4. Use markdown to represent your response in a prettier format.
      5. Maintain a consistency in the output format.
      6. Greetings are words and sentences.
      7. Translate the provided word in a different language only if it is mentioned in [[Language_name]].
    }

    Here are two examples:
    '''
    {
      User: 'plummet'
      Responce: **Plummet:** To fall or drop suddenly and steeply, especially from a high position or value.
          - **Example 1:** The temperature began to plummet as the cold front moved in.
          - **Example 2:** The stock prices plummeted after the announcement of the company's losses.
    },
    {
      User: 'आरियतन'
      Responce: **आरियतन (Ariyatan):** A Hindi term that means “temporarily borrowed” or “on loan.” It typically refers to items or resources given temporarily to someone, often without any fee or charge.
          - **Example 1:** उन्होंने अपनी किताबें आरियतन मुझे दीं। (They lent me their books temporarily.)
          - **Example 2:** यह उपकरण आरियतन उपलब्ध कराया गया है। (This equipment is provided on loan.)
    }
    '''
  """,
  )

  chat_session = model.start_chat(
     #History is a list of json objects to maintain the history between user and model
    history = history
    # history=[]
  )


  # Here model is given the word from user to generate a response based on the system prompt
  model_response = chat_session.send_message( user_input ).text
  if(model_response.endswith("\n\n")):
      model_response = model_response[:-2]
  return model_response

