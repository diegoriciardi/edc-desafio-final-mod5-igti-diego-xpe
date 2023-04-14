resource "aws_glue_crawler" "crawlerdadosenem2020" {
  database_name = "enem2020"
  name          = "enem"
  role          = aws_iam_role.glue_role.arn

  s3_target {
    path = "s3://dl-processing-zone-enem-2020-<BUCKET>/enem/"
  }
}