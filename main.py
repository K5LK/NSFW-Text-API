from fastapi import FastAPI, HTTPException
from gradio_client import Client
from typing import List
from models import Message, ModelResponse

# Initialize the Gradio Client
client = Client("https://romzay-michellejieli-nsfw-text-classifier.hf.space/--replicas/el3zf/")

# Initialize the FastAPI app
app = FastAPI()

# Error handling middleware
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})

# Define the function to interact with the model
def call_model(message: str) -> dict:
    try:
        result = client.predict(
            message,  # Pass the message directly without using keyword argument
            api_name="/predict"
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

# Define the GET endpoint for checking server status
@app.get('/')
async def check_server_status():
    return {"message": "Server is running..."}

# Define the POST endpoint for getting model predictions
@app.post('/predict', response_model=ModelResponse)
async def get_model_response(item: Message):
    try:
        model_response = call_model(item.message)
        # Prepare the response in the expected format
        return {"label": model_response['label'], "confidences": model_response['confidences']}
    except KeyError:
        raise HTTPException(status_code=500, detail="Invalid response format from the model")

# Ensure HTTPS is used
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
