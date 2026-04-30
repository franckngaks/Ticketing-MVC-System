"""Naturel Language Processing = Traitement Automatique de Language"""

import spacy
from pydantic import BaseModel
from typing import List

class AnalyseResult(BaseModel):
    priority_score: int
    keywords: List[str]
    category: str

class NLPService:
    def __init__(self):
        # Chargement du modèle français
        self.nlp = spacy.load("fr_core_news_sm")

    def analyser_incident(self, text: str) -> AnalyseResult:
        doc = self.nlp(text)
        # Logique d'analyse ici
        # ...
        return AnalyseResult(
            priority_score=1, 
            keywords=[token.text for token in doc if token.pos_ == "NOUN"],
            category="A définir"
        )