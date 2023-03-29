import requests
import uvicorn
from fastapi import FastAPI, Body, HTTPException, Header
from fastapi.staticfiles import StaticFiles

from models.models import (
    QuickQuotationResponse, QuickQuotationRequest,
)

app = FastAPI()
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="static")


@app.post("/quotation/api/quotation/quick-quote-partnership", response_model=QuickQuotationResponse)
def quick_quote_partnership(req: QuickQuotationRequest = Body(...),
                            ocp_apim_subscription_key: str | None = Header(None)):
    url = 'https://azuh3-br-api-platform.azure-api.net/quotation/api/quotation/quick-quote-partnership'
    headers = {'Ocp-Apim-Subscription-Key': ocp_apim_subscription_key}
    result = ""
    try:
        result = requests.post(url, json=req.dict(), headers=headers)
        return QuickQuotationResponse(**result.json())
    except Exception as e:
        print("Error:", e)
        print("Result:", result)
        raise HTTPException(status_code=500, detail="Internal Service Error")


if __name__ == '__main__':
    uvicorn.run("server.main:app", host="0.0.0.0", port=8080, reload=True)
