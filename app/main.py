from structlog import get_logger
from acmecorp.filemanagement.v1 import service_pb2 as filemanagementservicev1
from acmecorp.filemanagement.v1 import data_pb2 as filemanagementdatav1

log = get_logger()

req = filemanagementservicev1.DownloadRequest(
    url="https://picsum.photos/200/300"
)
log.info('Download request: ', request=req)

resp = filemanagementservicev1.DownloadResponse(
    file=filemanagementdatav1.File(
        name="image.jpg"
    )
)
log.info('Download response: ', response=resp)