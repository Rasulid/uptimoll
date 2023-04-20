import uvicorn

from code.core.config import settings

if __name__ == '__main__':
    uvicorn.run("code.main:app",host='0.0.0.0',port=settings.SVC_PORT, reload=True)