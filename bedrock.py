import boto3
import json
import pprint


session = boto3.Session() 
bedrock = session.client("bedrock-runtime", region_name="ap-northeast-1")

response = bedrock.invoke_model(
    body = json.dumps(
        {
            "inputText": "Provide some tips for effective programming.",
            "textGenerationConfig": {
                # "temperature": 0.7,  
                # "topP": 0.9,
                "maxTokenCount": 512,
                # "stopSequences": []
            }
        }
    ),
    modelId = "amazon.titan-text-express-v1",
    contentType = "application/json",
    accept = "application/json"
)
    
message = json.loads(response["body"].read())['results'][0]['outputText']

print("\n=== Effective Programming Tips ===\n")
pprint.pprint(message)
print("\n" + "=" * 40) 