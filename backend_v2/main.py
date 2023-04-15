import uvicorn

from code.app.core.config import settings

if __name__ == '__main__':
    uvicorn.run("code.app.main:app",host='0.0.0.0' ,port=settings.SVC_PORT, reload=True)


# export PYTHONPATH=:$/home/rasulabduvaitov/Desktop/uptimoll/backend_v2/code/app/