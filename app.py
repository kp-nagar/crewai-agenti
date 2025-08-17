from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from src.techai.crew import Techai


class InputQuery(BaseModel):
    query: str


app = FastAPI()


def run_crew_in_background(inputs: dict):
    Techai().crew().kickoff(inputs=inputs)


@app.post("/generate-question/")
async def create_item(iqu: InputQuery, background_tasks: BackgroundTasks):
    inputs = {
        'topic': iqu.query,
    }
    background_tasks.add_task(run_crew_in_background, inputs)
    return "done"
