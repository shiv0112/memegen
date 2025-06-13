# Meme Generator

```
meme_generator/
│
├── app/                          # Main app orchestration
│   ├── __init__.py
│   ├── main.py                   # Pipeline entry point
│   ├── controller.py             # Coordinates steps (summary → search → caption → render)
│
├── data/                         # Static and manually input data
│   ├── raw_news/                 # Input news articles (text files or JSON)
│   ├── templates/                # Meme image templates
│   └── vector_db_backup.json     # Optional: Qdrant backup (JSON)
│
├── images/
│   ├── input/                    # Filtered candidate images from Qdrant
│   └── output/                   # Final memes with captions
│
├── models/                       # All AI model integrations
│   ├── summarizer_gemini.py      # Gemini summarizer
│   ├── emotion_classifier.py     # Emotion classifier (Gemini or other)
│   ├── caption_generator.py      # LLM caption generation
│   ├── image_describer.py        # Describes images using Gemini Vision / BLIP
│
├── processing/
│   ├── vector_db_qdrant.py       # Qdrant connection, insertion, search
│   ├── embedder.py               # Text embedding via OpenAI/Gemini/CLIP
│   ├── image_renderer.py         # OpenCV or PIL-based caption overlay
│
├── utils/
│   ├── logger.py
│   ├── config.py                 # API keys, paths, constants
│   ├── prompts.py                # Centralized LLM prompts (summary, caption, etc.)
│
├── tests/                        # Tests for each module
│   ├── test_vector_db.py
│   ├── test_pipeline.py
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview
└── .gitignore                    # Ignore virtualenvs, cache, etc.
```