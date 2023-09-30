import typing as t
import yaml


class UpdateRasaFunc:

    def __init__(self) -> None:
        self.__rasa_path = '../rasa'

    async def __update_domain(self, intents: t.Sequence[t.Mapping[str, str]]) -> None:
        with open(f'{self.__rasa_path}/domain.yml', 'r', encoding='utf-8') as f:
            d = yaml.load(f, Loader=yaml.Loader)

        for intent in intents:
            d['intents'].append(intent['name'])
            d['responses'].update({f'utter_{intent["name"]}': [{'text': intent['ans']}]})

        with open(f'{self.__rasa_path}/domain.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(d, sort_keys=False, allow_unicode=True))

    async def __update_nlu(self, intents: t.Sequence[t.Mapping[str, str]]) -> None:
        with open(f'{self.__rasa_path}/data/nlu.yml', 'r', encoding='utf-8') as f:
            n = yaml.load(f, Loader=yaml.Loader)

        for intent in intents:
            n['nlu'].append({
                'intent': intent['name'],
                'examples': '\n'.join([str(i) for i in ['- {}'.format(num) for num in intent['qs']]])
            })

        with open(f'{self.__rasa_path}/data/nlu.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(n, sort_keys=False, allow_unicode=True))

    async def __update_rules(self, intents: t.Sequence[t.Mapping[str, str]]) -> None:
        with open(f'{self.__rasa_path}/data/rules.yml', 'r', encoding='utf-8') as rul:
            r = yaml.load(rul, Loader=yaml.Loader)

        for intent in intents:
            r['rules'].append({
                'rule': intent['name'],
                'steps': [{'intent': intent['name']}, {'action': f'utter_{intent["name"]}'}]
            })

        with open(f'{self.__rasa_path}/data/rules.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(r, sort_keys=False, allow_unicode=True))

    async def __call__(self, intents: t.Sequence[t.Mapping[str, str]]) -> None:
        await self.__update_domain(intents)
        await self.__update_nlu(intents)
        await self.__update_rules(intents)
