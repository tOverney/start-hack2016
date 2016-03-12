from typing import Iterable

from api.base import Base


class Concept:
    def __init__(self, id: str, label: str) -> None:
        self.id = id
        self.label = label

    def __repr__(self):
        return 'Concept({id!r}, {label!r})'.format(**self.__dict__)


class ConceptDetails:
    def __init__(self, abstract: str, id: str, label: str, link: str, ontology: Iterable[str], thumbnail: str,
                 concept_type: str) -> None:
        self.abstract = abstract
        self.id = id
        self.label = label
        self.link = link
        self.ontology = ontology
        self.thumbnail = thumbnail
        self.concept_type = concept_type

    def __repr__(self):
        return 'ConceptDetails({abstract!r}, {id!r}, {label!r}, {ontology!r}, {thumbnail!r}, {concept_type!r})'.format(
            **self.__dict__)


class Annotation:
    def __init__(self, concept: Concept, score: float, text_index: Iterable[int]) -> None:
        self.concept = concept
        self.score = score
        self.text_index = text_index

    def __repr__(self):
        return 'Annotation({concept!r}, {score!r}, {text_index!r})'.format(**self.__dict__)


class TextInsight(Base):
    def __init__(self) -> None:
        module = ('gateway', 'concept-insights/api/v2')
        username = '44601611-a7c8-46f2-9bbb-32fafdff3bb2'
        password = 'eKF8QtHBlj7H'
        super().__init__(module=module, username=username, password=password)

        self.account = "wikipedia"
        self.graph = "en-latest"

    def __get_path(self, endpoint: str) -> str:
        return 'graphs/{}/{}/{}'.format(self.account, self.graph, endpoint)

    def search(self, search: str) -> Iterable[Concept]:
        path = self.__get_path('label_search')
        params = {
            'query': search
        }

        ans = self._get(path=path, params=params)

        return {Concept(**match) for match in ans.json()['matches']}

    def annotate_text(self, body: str) -> Iterable[Annotation]:
        path = self.__get_path('annotate_text')
        json = {'body': body}
        headers = {'Content-Type': 'text/plain'}

        ans = self._post(path=path, json=json, headers=headers)

        return {Annotation(Concept(**annotation['concept']), annotation['score'], annotation['text_index']) for
                annotation in ans.json()['annotations']}

    def concepts(self, concept_name: str) -> ConceptDetails:
        path = self.__get_path('concepts/{}'.format(concept_name))

        ans = self._get(path=path)

        kwargs = ans.json()
        print(kwargs)
        kwargs['concept_type'] = kwargs.pop('type')

        return ConceptDetails(**kwargs)
