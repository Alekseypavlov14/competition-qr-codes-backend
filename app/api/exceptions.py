from werkzeug.exceptions import BadRequest, Unauthorized, NotFound, Conflict, InternalServerError

BadRequestException = BadRequest()
UnauthorizedException = Unauthorized()
NotFoundException = NotFound()
ConflictException = Conflict()
InternalServerException = InternalServerError()
