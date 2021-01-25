from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3
)

class S3Stack(core.Stack):

    def _init_(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        s3.Bucket(
            self,
            id,
            bucket_name='Bucket-prado001'
        )
