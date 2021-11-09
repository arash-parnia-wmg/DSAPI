from fastapi import APIRouter, Depends, HTTPException



router = APIRouter(
    prefix="/databricks",
    tags=["databricks"],
    responses={404: {"description": "Not found"}},
)



@router.get("/jobs", tags=["jobs"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

