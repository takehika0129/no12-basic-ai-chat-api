# Response Check of Major AI Chats
A Python script to interact with three major AI chat APIs: **ChatGPT (OpenAI), Gemini (Google), and Titan (Amazon)**.  


## Set up API keys
Before running the script, set up your API keys using `export`.

⚠️ Important Note:
Using these APIs incurs charges based on the number of requests and tokens used. Before running this script, please review the pricing details to avoid unexpected costs.


## Usage
Run the script for each AI platform.

ChatGPT:
```sh
python chatgpt.py
```

Gemini:
```sh
python gemini.py
```

Titan:
- Before using Amazon Bedrock, you must activate the AI models you intend to use.

```sh
python bedrock.py
```


## Concept
[Visit (takehika0129.github.io)](https://takehika0129.github.io/takehika-github-pages/reviews/prototype12.html)


## Requirements
- Python >= 3.9
- `openai`
- `google-genai`
- `boto3`


Install dependencies:
```sh
pip install -r requirements.txt
```


## License
You are free to use this code for personal and educational purposes. Commercial use and redistribution are not allowed.