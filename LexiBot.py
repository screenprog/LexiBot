import os
import google.generativeai as genai


# Create the model
def lexiBot(user_input: str ,history: list):
  generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
  }

  genai.configure(api_key=os.environ["GEMINI_API_KEY"])
  
  model = genai.GenerativeModel(
    model_name="learnlm-1.5-pro-experimental",
    generation_config=generation_config,
    system_instruction=
    """You are a language teacher and I will talk to you for exploring word meanings, translations, and learning different languages.
    Things you have to keep in your mind:
    {
      1. Provide concise explanations, translate text between languages, and offer language learning tips. 
      2. Stay specific and to the point no long content and no questions.
      3. Keep it simple a understandable.
      4. Give two examples.
      5. Give a space of one line between example and definition
      7. Keep indentation of 4 spaces for examples and stick them (together one after another).
      8. Maintain the consistency in the output format.
      9. Greetings are words.
      10. Do not add a meaning section in the end.
    }
    '''
      {
        User: 'plummet'
        Responce: 'Plummet: To fall or drop suddenly and steeply, especially from a high position or value.
            Example 1: The temperature began to plummet as the cold front moved in.
            Example 2: The stock prices plummeted after the announcement of the company's losses.'
      },
      {
        User: 'आरियतन'
        Responce:'आरियतन (Ariyatan): A Hindi term that means “temporarily borrowed” or “on loan.” It typically refers to items or resources given temporarily to someone, often without any fee or charge.
            Example 1: उन्होंने अपनी किताबें आरियतन मुझे दीं। (They lent me their books temporarily.)
            Example 2: यह उपकरण आरियतन उपलब्ध कराया गया है। (This equipment is provided on loan.)'
      }
    '''
    """,
  )

  chat_session = model.start_chat(
    history = history
  )

  model_response = chat_session.send_message( user_input ).text
  if(model_response.endswith("\n\n")):
      model_response = model_response[:-2]
  return model_response