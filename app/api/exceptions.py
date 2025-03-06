from werkzeug.exceptions import BadRequest, Unauthorized, NotFound, Conflict

BadRequestException = BadRequest()
UnauthorizedException = Unauthorized()
NotFoundException = NotFound()
ConflictException = Conflict()
