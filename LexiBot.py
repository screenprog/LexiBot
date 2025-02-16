import historywriter as hw
import historycreation as hc
import learnlm as llm

import time
import streamlit as st

def simulate_stream(model_response: str, chunk_size = 2, delay=0.02):
  for i in range(0, len(model_response), chunk_size):
    yield model_response[i:i + chunk_size]
    time.sleep(delay)
    


st.title("LexiBot")
history_file = "history-two.json"
hc.history = hw.read_from_json(history_file)
user_input = st.text_input("You: ")
if user_input:
  with st.container(height=500, border=True):
    definition = hc.find_in_history(user_input)
    if definition:
      st.write_stream(simulate_stream(definition))
    else:
      model_response = llm.lexiBot(user_input, hc.history[-5:])        
      hc.create_history("user", user_input)
      hc.create_history("model", model_response)
      st.write_stream(simulate_stream(model_response))
      hw.write_in_json(history_file, hc.history)