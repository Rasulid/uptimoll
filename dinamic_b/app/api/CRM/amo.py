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
        # tokens.default_token_manager.init(
        # code="def50200135491ad420f0dba74c159fdb4f9813960edcd8728d442185fc002279ee1562801cda3c2d7c96d4d52554637aeaec12f75510464207857752498b8b6d9a0c5b9f795716411a8ae020bcdc9dbbf0c9b79d251ed1a021357da3ea67c4030f029f73538d5232d6ccc630e540dac531683d8e9167409f6cdb4bc1dfdd51aa4a6723e027f3a0f4392becd0c54affdfd4f7374502c6989c329576b9e7c39c72743a6c2dfce4fefee7a0c6a7370a3285e307cec489d62f9cf69f752b679575ccc84e2bf779b006a89d9503f45a7e66222e95edd8076ac309f265427516c278d41fc9c71ba114ae983c73ce0de4251dee2b5ded5e354232ccbf6a0cdc8358130d7fe1cea18e99aa404cefea896b91a8af21e8b2bb9ad5362c6f8ef75ce6a5a1f5933ff7470874699e016269c912421e62705ec7e43c866a3dbbd3f7173568d052f356c99b9f4f41b53a00f890d667f7e924a8f97d91525ead9d9e5524c186f86b362e7f72338b5c104540ee5370862f519d8743bfcbfb76002570ffe7e6b31f5cb49b330753e203940d5cb7f92e1da15234577df71da3affdc97522078e48b789d15e4affacff9c93be94b4f4d4d315014b0e42cd9761c7e38c72538114f6c0d04aab7aa1573194f95224ef7b0ee1ae00c91cfe8cad86c1342847da8786cc83c3ddb74e9a1c9366b38e790d5d5033268",
        # skip_error=False)

        AMOSchema.name = f"name:{name}, phone_number:{phone_number}, cource: {cource}, region: {region}"

        lead = Lead.objects.create(name=AMOSchema.name)
        return {"status": "success", "lead_id": lead.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))