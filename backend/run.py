import uvicorn

if __name__ == "__main__":
    print("Starting fastapi-meetup app")
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=["backend"],
        log_config=None,
    )
