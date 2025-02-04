from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load the tokenizer and model
tokenizer_path = "C:/Users/HP/Desktop/chatbot/Q&A/t5_chatbot_tokenizer"
model_path = "C:/Users/HP/Desktop/chatbot/Q&A/t5_chatbot_model"

tokenizer = T5Tokenizer.from_pretrained(tokenizer_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)
model.eval()

def generate_response_top_k_top_p(question, model, tokenizer, max_length=64, top_k=50, top_p=0.95, temperature=1.0):
    """
    Generates a response to a given question using Top-K and Top-P sampling.
    """
    # Format the question for the model
    formatted_question = f"Answer the following question: {question}"

    # Tokenize the input question
    inputs = tokenizer(
        formatted_question,
        return_tensors="pt",
        padding=True,
        truncation=True,
        max_length=128,
    )

    # Generate a response using Top-K and Top-P sampling
    outputs = model.generate(
        input_ids=inputs["input_ids"],
        attention_mask=inputs["attention_mask"],
        max_length=max_length,
        do_sample=True,
        top_k=top_k,
        top_p=top_p,
        temperature=temperature,
        pad_token_id=tokenizer.pad_token_id,
    )

    # Decode the generated response into a human-readable string
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response

@app.route("/")
def index():
    return render_template("index.html")  # Serves the frontend

@socketio.on("send_message")
def handle_message(data):
    user_message = data["message"]
    
    # Generate response using the AI model
    bot_response = generate_response_top_k_top_p(user_message, model, tokenizer)

    # Emit the bot's response to the frontend
    emit("receive_message", {"message": bot_response}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5000)
