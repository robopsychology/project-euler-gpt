from transformers import T5Tokenizer, T5ForConditionalGeneration

class Flan_T5:
    def __init__(self) -> None:
        self.model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xl")
        self.tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xl")

    def answer(self, input_text: str) -> str:
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(input_ids, max_new_tokens=1024)
        return self.tokenizer.decode(outputs[0])
