from fastapi import FastAPI

app = FastAPI()

@app.get('/health')
def health_check():
    return {"status": "OK"}

if __name__ == "main":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000,reload=True)