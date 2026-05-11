# Mini Home Furniture Dashboard

A full-stack web application designed for managing a digital furniture catalog. This project demonstrates a decoupled client-server architecture with a focus on code robustness, technical depth, and clean UI design.

## Technical Stack
- **Frontend:** React + Vite (for fast development and optimized builds).
- **Backend:** FastAPI (Python) for asynchronous, high-performance RESTful APIs.
- **Database:** SQLite with SQLModel (ORM) for reliable data structure and queries.

## Key Features & Robustness
- **Separation of Concerns:** Clear boundary between the React frontend and FastAPI backend.
- **Error Handling:** - Frontend utilizes `try/catch` blocks and loading states to prevent UI crashes and improve UX.
  - Backend implements `HTTPException` to safely handle invalid requests and missing data.
- **CORS Configuration:** Securely allows communication between the Vite development server and the FastAPI backend.
- **Interactive Documentation:** Automatic Swagger UI generation for API testing.

## Screenshots
Here are some views of the running application:
*(Ensure the backend is running and data is added via Swagger UI)*

1. **Frontend Dashboard:**
![Frontend Dashboard](screenshots/frontend_view.png)

2. **Backend API (Swagger UI):**
![Swagger UI](screenshots/swagger_success.png)

## How to Run the Project Locally

### 1. Start the Backend
Navigate to the `backend` directory, install dependencies, and start the Uvicorn server:
```bash
cd backend
pip install fastapi uvicorn sqlmodel
python -m uvicorn main:app --reload