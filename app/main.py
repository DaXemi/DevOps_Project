from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "This is part of a devops project."}


# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run(app, port=8000)
