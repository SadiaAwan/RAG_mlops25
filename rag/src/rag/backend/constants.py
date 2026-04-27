from pathlib import Path

ROOT_PATH = Path(__file__).parents[1]
BASE_PATH = ROOT_PATH / "data"

VECTOR_DB_PATH = ROOT_PATH / "knowledge_base"


EMBEDDING_MODEL = "embed-multilingual-light-v3.0"
MODEL_MEDIUM="openrouter:nvidia/nemotron-3-nano-30b-a3b:free"
MODEL_LARGE="openrouter:nvidia/nemotron-3-super-120b-a12b:free"

