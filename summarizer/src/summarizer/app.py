from fastapi import FastAPI
from pydantic import BaseModel
from pprint import pprint

import json
from src.summarizer.crew import Summarizer

app = FastAPI()


class SummarizeRequest(BaseModel):
    text: str


@app.get("/")
def read_root():
    return {"message": "Summarizer service is running"}


@app.post("/summarize")
def summarize(request: SummarizeRequest):

    inputs = {
        'topic': request.text,
    }
    crew = Summarizer().crew()
    result = crew.kickoff(inputs= inputs)
    # print("")
    dict_task = json.loads(result.tasks_output[0].raw.strip())
    # print("--------------------")
    # pprint(result.tasks_output[0])
    # print("--------------------")
    # print("")
    return {"period": result.raw.strip(), "title":dict_task['title'], "abstract": dict_task['content']}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
