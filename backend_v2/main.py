import uvicorn

if __name__ == '__main__':
    uvicorn.run("code.app.main:app", host="0.0.0.0", reload=True)


