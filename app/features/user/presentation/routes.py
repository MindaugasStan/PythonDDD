from fastapi import Depends, HTTPException, status, Response, Request, APIRouter

router = APIRouter(
    prefix='/users',
    tags=['users'],
)

@router.post(
    '/',
    response_model=UserReadModel,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_409_CONFLICT: {
            'model': ErrorMessageUserAlreadyExists
        }
    },
)
def create_user(
    data: UserCreateModel,
    response: Response,
    request: Request,
    create_user_use_case: CreateUserUseCase = Depends(get_create_user_use_case),
):
    try:
        user = create_user_use_case((data, ))
    except UserAlreadyExistsError as exception:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=exception.message
        )
    except Exception as _exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    response.headers['location'] = f"{request.url.path}{user.id_}"
    return user

@router.delete(
    '/{id_}/',
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUserNotFound
        }
    }
)
def delete_user(
    id_: int,
    delete_user_use_case: DeleteUserUseCase = Depends(get_delete_user_use_case)
):
    try:
        user = delete_user_use_case((id_, ))
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user


@router.get(
    '/{id_}/',
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUserNotFound
        }
    }
)
def get_user(
    id_: int,
    get_user_use_case_: GetUserUseCase = Depends(get_user_use_case)
):
    try:
        user = get_user_use_case_((id_, ))
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user


@router.get(
    '/',
    response_model=list[UserReadModel],
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUsersNotFound
        }
    }
)
def get_users(skip: int = 0, limit: int = 100, get_users_use_case_: GetUsersUseCase = Depends(get_users_use_case)):
    try:
        users = get_users_use_case_(None)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    if not users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )

    return users


@router.patch(
    '/{id_}/',
    response_model=UserReadModel,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            'model': ErrorMessageUserNotFound
        }
    }
)
async def update_user(
    id_: int,
    data: UserUpdateModel,
    update_user_use_case: UpdateUserUseCase = Depends(get_update_user_use_case)
):
    try:
        user = update_user_use_case((id_, data))
    except UserNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

    return user