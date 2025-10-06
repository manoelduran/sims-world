from fastapi import Request, status
from fastapi.responses import JSONResponse
from ...application.exceptions.application_exceptions import SimNotFoundError


async def sim_not_found_exception_handler(request: Request, exc: SimNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": f"Handler de Exceção: {exc}"},
    )
