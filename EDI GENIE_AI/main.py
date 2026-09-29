from pathlib import Path
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from notes_module import generate_notes
from summary_module import summarize_text
from learning_path import recommend_learning_path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduMind AI - Smart AI-Powered Learning Assistant",
    description="Smart AI-Powered Learning Assistant",
    version="1.0.0"
)

static_dir = BASE_DIR / "static"
if static_dir.exists():
    app.mount(
        "/static",
        StaticFiles(directory=str(static_dir)),
        name="static"
    )

templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request
        }
    )


@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "application": "EduGenie"
    }


@app.post("/qa")
async def qa(question: str = Form(...)):
    try:
        result = answer_question(question)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }


@app.post("/explain")
async def explain(text: str = Form(...)):
    try:
        result = explain_concept(text)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }


@app.post("/quiz")
async def quiz(text: str = Form(...)):
    try:
        result = generate_quiz(text)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }


@app.post("/notes")
async def notes(text: str = Form(...)):
    try:
        result = generate_notes(text)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }


@app.post("/summarize")
async def summarize(text: str = Form(...)):
    try:
        result = summarize_text(text)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }


@app.post("/learn/recommendations")
async def learning_recommendations(
    topic: str = Form(...),
    level: str = Form("Beginner")
):
    try:
        result = recommend_learning_path(topic, level)
        return {
            "success": True,
            "result": result
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "result": f"⚠️ {str(e)}"
        }