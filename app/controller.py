# app/controller.py
from models.summarizer_gemini import summarize
from models.emotion_classifier import classify_emotion
from processing.vector_db_qdrant import search_similar_images
from models.caption_generator import generate_caption
from processing.image_renderer import render_caption

def pipeline(news_file: str):
    # 1. Summarize news
    with open(news_file, "r") as f:
        news_content = f.read()
        
    summary = summarize(news_content)
    print(f"Summary: {summary}")

    # 2. Classify Emotion
    emotion = classify_emotion(summary)
    print(f"Classified Emotion: {emotion}")

    # 3. Search Qdrant for matching images
    matching_images = search_similar_images(summary, emotion)
    print(f"Retrieved {len(matching_images)} matching images")

    # 4. Generate caption
    caption = generate_caption(summary)
    print(f"Generated caption: {caption}")

    # 5. Combine caption with image
    rendered_file = render_caption(matching_images[0], caption)
    print(f"Rendered meme at {rendered_file}")

    return rendered_file
