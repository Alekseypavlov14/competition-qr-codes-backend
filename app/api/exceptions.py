from werkzeug.exceptions import Unauthorized, NotFound, Conflict

UnauthorizedException = Unauthorized
NotFoundException = NotFound(404)
ConflictException = Conflict(409)
