# Tutorial - Deploy Qwen2.5-Coder-32B-Instruct using Inferless
[Qwen2.5-Coder-32B-Instruct](https://huggingface.co/qwen/Qwen2.5-Coder-32B-Instruct) is a SOTA coder LLM developed by Alibaba Cloud's Qwen team. This model is part of the Qwen2.5 series and is tailored for instruction-based tasks, particularly in code generation, reasoning, and repair.
It features a dense transformer architecture with 32.5 billion parameters, 64 layers, and supports a context length of up to 131,072 tokens, enabling it to handle extensive inputs effectively. The model utilizes the RoPE (Rotary Position Embedding) mechanism, SwiGLU activation functions, RMSNorm normalization, and Attention QKV bias to enhance its performance.

## TL;DR:
- Deployment of Qwen2.5-Coder-32B-Instruct model using [vllm](https://github.com/vllm-project/vllm).
- You can expect an average tokens/sec of `21.32` and a latency of `10.32 sec` for generating a text of `256` tokens. This setup has an average cold start time of `40.17 seconds`.
- Dependencies defined in `inferless-runtime-config.yaml`.
- GitHub/GitLab template creation with `app.py`, `inferless-runtime-config.yaml` and `inferless.yaml`.
- Model class in `app.py` with `initialize`, `infer`, and `finalize` functions.
- Custom runtime creation with necessary system and Python packages.
- Model import via GitHub with `Pydantic models`.
- Recommended GPU: NVIDIA A100 for optimal performance.
- Custom runtime selection in advanced configuration.
- Final review and deployment on the Inferless platform.

### Fork the Repository
Get started by forking the repository. You can do this by clicking on the fork button in the top right corner of the repository page.

This will create a copy of the repository in your own GitHub account, allowing you to make changes and customize it according to your needs.

### Create a Custom Runtime in Inferless
To access the custom runtime window in Inferless, simply navigate to the sidebar and click on the Create new Runtime button. A pop-up will appear.

Next, provide a suitable name for your custom runtime and proceed by uploading the **inferless-runtime-config.yaml** file given above. Finally, ensure you save your changes by clicking on the save button.

### Import the Model in Inferless
Log in to your inferless account, select the workspace you want the model to be imported into and click the `Add a custom model` button.

- Select `Github` as the method of upload from the Provider list and then select your Github Repository and the branch.
- Choose the type of machine, and specify the minimum and maximum number of replicas for deploying your model.
- Configure Custom Runtime ( If you have pip or apt packages), choose Volume, Secrets and set Environment variables like Inference Timeout / Container Concurrency / Scale Down Timeout
- Once you click “Continue,” click Deploy to start the model import process.

Enter all the required details to Import your model. Refer [this link](https://docs.inferless.com/integrations/git-custom-code/git--custom-code) for more information on model import.

---
## Curl Command
Following is an example of the curl command you can use to make inference. You can find the exact curl command in the Model's API page in Inferless.
```bash
curl --location '<your_inference_url>' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <your_api_key>' \
    --data '{
      "inputs": [
        {
          "name": "prompt",
          "shape": [1],
          "data": ["Implement a function to check if a given number is a prime number."],
          "datatype": "BYTES"
        },
        {
          "name": "system_prompt",
          "shape": [1],
          "data": ["You are a helpful coding bot."],
          "datatype": "BYTES"
        },
        {
          "name": "temperature",
          "optional": true,
          "shape": [1],
          "data": [0.7],
          "datatype": "FP32"
        },
        {
          "name": "top_p",
          "optional": true,
          "shape": [1],
          "data": [0.1],
          "datatype": "FP32"
        },
        {
          "name": "repetition_penalty",
          "optional": true,
          "shape": [1],
          "data": [1.18],
          "datatype": "FP32"
        },
        {
          "name": "max_tokens",
          "optional": true,
          "shape": [1],
          "data": [512],
          "datatype": "INT16"
        },
        {
          "name": "top_k",
          "optional": true,
          "shape": [1],
          "data": [40],
          "datatype": "INT8"
        }
      ]
    }'
```


For more information refer to the [Inferless docs](https://docs.inferless.com/).
