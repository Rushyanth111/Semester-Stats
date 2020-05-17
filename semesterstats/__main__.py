from semesterstats import App
import uvicorn


def main():
    uvicorn.run(App, port=9000)


if __name__ == "__main__":
    main()
