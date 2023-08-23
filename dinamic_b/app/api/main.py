from fastapi import FastAPI

app = FastAPI(title="MIT",
              version="2.0")


@app.get('/v2/root')
async def root():
    return {"root": "hello"}
