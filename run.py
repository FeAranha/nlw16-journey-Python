from src.main.server.server import app

if __name__ == "__main__":
  app.run(host="0.0.0.0", post=3000, debug=True)