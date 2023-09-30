from transformers import M2M100ForConditionalGeneration

from ..tokenization_small100 import SMALL100Tokenizer


class TranslateRuFunc:

    def __init__(self, batch: int = 256) -> None:
        self.__batch = batch
        self.__model = M2M100ForConditionalGeneration.from_pretrained('alirezamsh/small100')
        self.__tokenizer = SMALL100Tokenizer.from_pretrained('alirezamsh/small100')
        self.__tokenizer.tgt_lang = 'ru'

    async def __call__(self, data: str) -> str:
        words = data.split()
        ru_data = ''
        for i in range(0, len(words), self.__batch):
            batch_data = ' '.join(words[i: i + self.__batch])
            encoded_hi = self.__tokenizer(batch_data, return_tensors='pt')
            generated_tokens = self.__model.generate(**encoded_hi)
            ru_data += self.__tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0] + ' '
        return ru_data
