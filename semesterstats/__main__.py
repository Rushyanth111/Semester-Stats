from semesterstats import App
from .DocxGenerator import docsGeneratorAlternate
import uvicorn


def main():
    uvicorn.run(App, port=9000)


if __name__ == "__main__":
    main()
