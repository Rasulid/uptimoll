from fastapi import APIRouter
from fastapi import HTTPException
from amocrm.v2 import tokens, Lead

from pydantic import BaseModel
from api.core.config import settings

router = APIRouter(
    prefix='/api/amo',
    tags=["CRM integration"]
)


class AMOSchema(BaseModel):
    name: str


@router.post('/create-lead')
async def create_amo_lead(name: str,
                          phone_number: str,
                          cource: str,
                          region: str):
    try:
        tokens.default_token_manager(
            client_id=settings.CLIENT_ID,
            client_secret=settings.CLIENT_SECRET,
            subdomain=settings.SUBDAMAIN,
            redirect_url=settings.REDIRECT_URL,
            storage=tokens.FileTokensStorage(),  # by default FileTokensStorage
        )
        tokens.default_token_manager.init(
        code=settings.TOKEN_CODE,
        skip_error=False)

        AMOSchema.name = f"name:{name}, phone_number:{phone_number}, cource: {cource}, region: {region}"

        lead = Lead.objects.create(name=AMOSchema.name)
        return {"status": "success", "lead_id": lead.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
