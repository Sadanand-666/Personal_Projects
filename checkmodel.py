import google.generativeai as genai

genai.configure(api_key="AIzaSyB0XXH9BACyNCY92DYRPV1GVG029IjVwz4")

models = genai.list_models()
for model in models:
    print(model.name)
