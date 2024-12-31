import transformers, torch, typing, My_Code_AI_interface

class My_Code_LM(My_Code_AI_interface.My_Code_AI_interface):
    
    LANGUAGE_MODEL: typing.Final[str] = f"TheBloke/CodeLlama-7B-GGUF"
    
    def __init__(self: typing.Self) -> None:
        self.tokenizer_for_lm: transformers.PreTrainedTokenizer = transformers.AutoTokenizer.from_pretrained(self.LANGUAGE_MODEL)
        self.pipeline_for_lm: transformers.Pipeline = transformers.pipeline(f"text-generation", model=self.LANGUAGE_MODEL, torch_dtype=torch.float16, device_map=f"auto", max_length=100, pad_token_id=self.tokenizer_for_lm.eos_token_id, eos_token_id=self.tokenizer_for_lm.eos_token_id)

    @typing.override
    async def __response__(self: typing.Self, prompt: str) -> str:
        self.user_query: list[dict[str, str]] = [{"role": "user", "content": prompt}]

        return self.pipeline_for_lm(self.user_query)[0].get("generated_text")[1].get("content")
