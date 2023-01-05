def load_settings(app):
    from dotenv import load_dotenv, find_dotenv
    import os
    print("loading settings...")
    load_dotenv(find_dotenv())
    app.config.DEBUG = os.getenv("DEBUG", False)
    app.config.WORKERS = os.getenv("WORKERS", 8)