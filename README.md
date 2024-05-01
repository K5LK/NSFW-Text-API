<p>This is a simple example of building an NSFW (Not Safe For Work) text classifier API using FastAPI, a modern web framework for building APIs with Python 3.7+. The API leverages a pre-trained NSFW text classifier model to classify text inputs as either safe or NSFW based on their content.</p>
<br>
<h2>Check the Demo</h2>
<p>🎯 <a href="https://nsfw-text-api.onrender.com/">NSFW Text Classifier Demo</a></p>
<h2>Usage</h2>
<h2>Usage</h2>

<h3>1. Running the Server</h3>
<p>First, you need to run the FastAPI server. Make sure you have Python installed on your system. Then, follow these steps:</p>
<ol>
  <li>Clone this repository:</li>
  <code>git clone https://github.com/your-username/your-repository.git</code>
  <li>Install dependencies:</li>
  <code>pip install -r requirements.txt</code>
  <li>Run the FastAPI server:</li>
  <code>uvicorn main:app --reload</code>
</ol>

<h3>2. Making Requests</h3>
<p>Once the server is running, you can make requests to it using tools like cURL, Postman, or Python's requests library. Here's an example:</p>
<pre><code>curl -X POST -H "Content-Type: application/json" -d '{"message": "Your text message here"}' -s  https://nsfw-text-ap
i.onrender.com/predict </code></pre>
<p>Replace "Your text message here" with the text you want to classify.</p>

<h3>3. Expected Response</h3>
<p>The server will respond with a JSON object containing the classification result. Here's an example response:</p>
<pre><code>{
  "label": "Safe",
  "confidences": [
    {"label": "Safe", "confidence": 0.95},
    {"label": "NSFW", "confidence": 0.05}
  ]
}</code></pre>
<p>The "label" field indicates whether the text is classified as "Safe" or "NSFW", and the "confidences" field provides confidence scores for each class.</p>

<h3>4. Using the Demo</h3>
<p>You can also try the NSFW text classifier demo hosted online. Follow these steps:</p>
<ol>
  <li>Open your web browser and navigate to the <a href="https://nsfw-text-api.onrender.com/">NSFW Text Classifier Demo</a>.</li>
  <li>Enter your text {"message": "ENTER CONTENT"}</li>
  <li>Send the post request to /predict</li>
  <li>View the classification result displayed.</li>
</ol>


