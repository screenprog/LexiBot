import historywriter as hw
import historycreation as hc
import LexiBot as lb

history_file = "history.json"
hc.history = hw.read_from_json(history_file)
user_input = input("You: ")
definition = hc.find_in_history(user_input)
if definition:
    print(definition)
else:
  model_response = lb.lexiBot(user_input, hc.history[-5:])        
  hc.create_history("user", user_input)
  hc.create_history("model", model_response)
  print("LexiBot:\n  "+ model_response)
  hw.write_in_json(history_file, hc.history)