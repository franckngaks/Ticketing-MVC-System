from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
# On importe ton service et ton modèle de résultat
from src.main.python.ia_analyses_service.service.nlp_service import NLPService, AnalyseResult

router = APIRouter()
nlp_service = NLPService() # On initialise le cerveau une seule fois

# On définit le format de ce que l'utilisateur doit envoyer
class IncidentRequest(BaseModel):
    description: str

@router.post("/analyse", response_model=AnalyseResult)
async def post_analyse(request: IncidentRequest):
    if not request.description:
        raise HTTPException(status_code=400, detail="La description ne peut pas être vide")
    
    # On appelle ton service NLP
    resultat = nlp_service.analyser_incident(request.description)
    return resultat