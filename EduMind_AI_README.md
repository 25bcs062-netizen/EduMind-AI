# EduMind AI – Smart AI-Powered Learning Assistant

## Project Overview

EduMind AI is a Smart AI-Powered Learning Assistant designed to support students through a single web-based learning platform.

The project uses Generative AI to provide:
- Question answering
- Concept explanations
- Quiz generation
- Study notes
- Content summarization
- Learning-path recommendations

## Team Members

1. K. ANNAMALAI
2. R. YASWANTH
3. A. ELANCHEZHIYAN
4. S. LOKESH
5. V. SANJAI

## Project Structure

```text
EduMind AI
│
├── 01. Problem Discovery & Ideation
│   ├── Idea Generation & Brainstorming.pdf
│   ├── Problem Statement.pdf
│   └── Student Empathy Map.pdf
│
├── 02. User & Solution Requirements
│   ├── Student Journey Map.pdf
│   ├── EduMind AI Data Flow.pdf
│   ├── Functional & Non-Functional Requirements.pdf
│   └── Technology Requirements.pdf
│
├── 03. Solution Design
│   ├── Problem-Solution Fit.pdf
│   ├── Proposed EduMind AI Solution.pdf
│   └── EduMind AI System Architecture.pdf
│
├── 04. Project Planning
│   └── EduMind AI Project Plan.pdf
│
├── 05. Project Development
│   ├── Code-Layout, Readability and Reusability.pdf
│   ├── Coding of Solution.pdf
│   └── No. of Functional Features Implemented.pdf
│
├── 06. Project Testing
│   └── EduMind AI Performance Testing.pdf
│
├── 07. Project Documentation
│   ├── EduMind AI Executable Files.pdf
│   └── EduMind AI Project Documentation.pdf
│
└── 08. Project Demonstration
    ├── Project Communication.pdf
    ├── Demonstration of EduMind AI Features.pdf
    ├── EduMind AI Demo Planning.pdf
    ├── Scalability & Future Enhancements.pdf
    └── Team Involvement in Demonstration.pdf
```

## Technology Stack

- Python
- FastAPI
- Uvicorn
- HTML, CSS and JavaScript
- Google Gemini API / Google Gen AI SDK
- python-dotenv
- Visual Studio Code

## Core Workflow

```text
Student
   ↓
EduMind AI Web Interface
   ↓
FastAPI Backend
   ↓
Feature Module
   ↓
Gemini AI Service
   ↓
Generated Learning Response
   ↓
Student
```

## Functional Features

### 1. Question Answering
Answers questions across programming, mathematics, science, technology and general learning topics.

### 2. Concept Explanation
Explains difficult concepts in simple, beginner-friendly language with examples.

### 3. Quiz Generation
Generates topic-based practice questions for self-assessment and revision.

### 4. Study Notes
Creates structured study notes containing important points, terms and examples.

### 5. Content Summarization
Converts longer learning content into concise revision material.

### 6. Learning Path Recommendation
Suggests a structured learning sequence based on the selected topic and learner level.

## How to Run the Project

1. Open the EduMind AI project folder in Visual Studio Code.
2. Install the required Python packages from `requirements.txt`.
3. Create or update the local `.env` file with the Gemini API credential.
4. Start the application using Uvicorn.
5. Open the local website in a browser.

Example:

```powershell
python -m uvicorn main:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Security

- Keep the Gemini API key inside the local `.env` file.
- Do not hard-code the API key in source code.
- Do not upload the API key to GitHub or include it in public screenshots or documentation.

## Project Status

EduMind AI documentation and demonstration materials are organized into the eight project phases listed above.

## Date

September 2026
