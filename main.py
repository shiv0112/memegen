# entrypoint main.py

from app.controller import pipeline

def main():
    news_file = "data/raw_news/example.txt"
    pipeline(news_file)


if __name__ == "__main__":
    main()
