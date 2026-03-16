import boto3
import json

# Create Bedrock runtime client
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

MODEL_ID = "amazon.nova-lite-v1:0"


def ask_nova(prompt):

    body = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 400,
        "temperature": 0.7
    })

    response = client.invoke_model(
        modelId=MODEL_ID,
        body=body,
        contentType="application/json"
    )

    response_body = json.loads(response["body"].read())

    return response_body["output"]["message"]["content"][0]["text"]