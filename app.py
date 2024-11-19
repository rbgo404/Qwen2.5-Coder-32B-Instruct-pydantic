from vllm import LLM
from vllm.sampling_params import SamplingParams
from transformers import AutoTokenizer

class InferlessPythonModel:
    def initialize(self):
        model_id = "Qwen/Qwen2.5-Coder-32B-Instruct"
        self.llm = LLM(model=model_id,gpu_memory_utilization=0.9,max_model_len=5000)
        self.tokenizer = AutoTokenizer.from_pretrained(model_id)

    def infer(self, inputs):
        prompt = inputs["prompt"]
        system_prompt = inputs.get("system_prompt","You are a helpful coding bot.")
        temperature = inputs.get("temperature",0.7)
        top_p = inputs.get("top_p",0.1)
        repetition_penalty = inputs.get("repetition_penalty",1.18)
        top_k = int(inputs.get("top_k",40))
        max_tokens = inputs.get("max_tokens",256)

        sampling_params = SamplingParams(temperature=temperature,top_p=top_p,repetition_penalty=repetition_penalty,
                                         top_k=top_k,max_tokens=max_tokens)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        input_text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        result = self.llm.generate(input_text, sampling_params)
        result_output = [output.outputs[0].text for output in result]

        return {'generated_text': result_output[0]}

    def finalize(self):
        self.llm = None