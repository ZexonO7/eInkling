from src.app import create_app
from config import BIND_HOST, BIND_PORT

app = create_app()

if __name__ == "__main__":
    app.run(host=BIND_HOST, port=BIND_PORT, debug=True)
