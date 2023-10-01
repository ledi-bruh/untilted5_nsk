import typing as t

from question_generator.questiongenerator import QuestionGenerator
from Questgen.main import QGen


class QuestionGenerateFunc:

    def __init__(self, batch: int = 128) -> None:
        self.__batch = batch
        self.__qg = QuestionGenerator()

    async def __call__(self, data: str, n: int = 8, n_extra: int = 2) -> t.MutableSequence:
        
        words = data.split()

        res = []

        for i in range(0, len(words), self.__batch):
            batch_data = ' '.join(words[i: i + self.__batch])

            qa_list = self.__qg.generate(
                batch_data,
                num_questions=n,
                answer_style='sentences'
            )

            questions = [qa['question'] for qa in qa_list]

            pay = []
            for question in questions:
                payload = {
                    'input_text': question,
                    'max_questions': n_extra,
                }
                qg = QGen()
                output = qg.paraphrase(payload)
                pay.append(output)

            res += [
                [
                    qa_list[k]['answer'],
                    [q, *[pq.lstrip('ParaphrasedTarget: ') for pq in pay[k]['Paraphrased Questions']]],
                ]
                for k, q in enumerate(questions)
            ]
        return res
