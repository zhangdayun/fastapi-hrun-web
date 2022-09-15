"""
统一响应状态码
"""
from typing import Union

from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.encoders import jsonable_encoder


def r_200(*, data: Union[list, dict, str] = None, message: str = "Success") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'errcode': 200,
            'message': message,
            'data': data
        })
    )


def r_400(*, data: Union[list, dict, str] = None,
          message: Union[list, dict, str] = "Request Validation Error") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            'code': 400,
            'data': data,
            'message': message,
        })
    )


def r_403(*, data: Union[list, dict, str] = None, message: str = "") -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            'errcode': 403,
            'message': message,
            'data': data,
        })
    )


def r_404(*, message: str = "") -> Response:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            'errcode': 404,
            'message': message,
        })
    )
