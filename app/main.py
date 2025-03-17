from fastapi import FastAPI

#Initialization of the app
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hola Mundo, soy Rodrigo"}

