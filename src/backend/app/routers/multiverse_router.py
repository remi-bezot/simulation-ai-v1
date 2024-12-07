from fastapi import APIRouter

router = APIRouter()


@router.get("/multiverse")
def list_multiverse():
    return {"dimensions": []}
