import typing as t
import yaml


class UpdateRasaFunc:

    def __init__(self) -> None:
        self.__rasa_path = '../rasa'

    async def __update_domain(self, intent_names: t.Sequence[str]) -> None:
        with open(f'{self.__rasa_path}/domain.yml', 'r', encoding='utf-8') as f:
            d = yaml.load(f, Loader=yaml.Loader)

        for name in intent_names:
            d['intents'].append(name)
            d['responses'].update({f'utter_{name[:40]}': [{'text': name}]})

        with open(f'{self.__rasa_path}/domain.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(d, sort_keys=False, allow_unicode=True))

    async def __update_nlu(self, intents: t.Mapping[str, t.Any]) -> None:
        with open(f'{self.__rasa_path}/data/nlu.yml', 'r', encoding='utf-8') as f:
            n = yaml.load(f, Loader=yaml.Loader)

        for name, examples in intents.items():
            n['nlu'].append({
                'intent': name,
                'examples': '\n'.join([str(i) for i in ['- {}'.format(num) for num in examples]])
            })

        with open(f'{self.__rasa_path}/data/nlu.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(n, sort_keys=False, allow_unicode=True))

    async def __update_rules(self, intent_names: t.Sequence[str]) -> None:
        with open(f'{self.__rasa_path}/data/rules.yml', 'r', encoding='utf-8') as rul:
            r = yaml.load(rul, Loader=yaml.Loader)

        for name in intent_names:
            r['rules'].append({
                'rule': name,
                'steps': [{'intent': name}, {'action': 'utter_' + name}]
            })

        with open(f'{self.__rasa_path}/data/rules.yml', 'w', encoding='utf-8') as f:
            f.write(yaml.dump(r, sort_keys=False, allow_unicode=True))

    async def __call__(self, intents: t.Sequence) -> None:
        intents_dict = dict(intents)
        await self.__update_domain(intents_dict.keys())
        await self.__update_nlu(intents_dict)
        await self.__update_rules(intents_dict.keys())
