# backend/app/run.py
from app import create_app  # Relative import to the current directory

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
