# Dataproc
1. Dataproc runs spark, hive, pig, hadoop natively
1. Dataproc cluster is made of compute instances
1. Hadoop or Spark cluster is a fixed cluster.. It doesn’t auto-scale.

## Simple DataProc Job
1. cloud.google.com/dataproc/docs/guides/submit-job
  
   - code: github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/unstructured/lab2.py
  
   - data: github.com/GoogleCloudPlatform/training-data-analyst/blob/master/courses/unstructured/lab2-input.txt

### Extra Resources
- Migrating On-prem Hadoop to GCP.
  - cloud.google.com/solutions/migration/hadoop/hadoop-gcp-migration-overview
  - cloud.google.com/solutions/migration/hadoop/hadoop-gcp-migration-jobs
  - cloud.google.com/solutions/migration/hadoop/hadoop-gcp-migration-data
- Preemptible compute in Dataproc
  - medium.com/google-cloud/google-clouds-spot-instances-win-big-and-you-should-too-5b244ca3facf
- Autoscaling Dataproc automatically External
  - blog.doit-intl.com/autoscaling-google-dataproc-clusters-21f34beaf8a3
- Autoscaling Dataproc Alpha
  - cloud.google.com/dataproc/docs/concepts/configuring-clusters/autoscaling
- Scaling pre-existing running cluster
  - cloud.google.com/dataproc/docs/concepts/configuring-clusters/scaling-clusters
- Restartable Jobs
  - cloud.google.com/dataproc/docs/concepts/jobs/restartable-jobs
- Cluster Scheduled Deletion
  - Cannot create such cluster from Web Console.. Only command-line or rest api. cloud.google.com/dataproc/docs/concepts/configuring-clusters/scheduled-deletion

**BigQuery & DataProc**
- cloud.google.com/blog/big-data/2016/05/bigquery-and-dataproc-shine-in-independent-big-data-platform-comparison
- Big Data Pricing
  - cloud.google.com/blog/big-data/2016/03/understanding-cloud-pricing-part-6-big-data-processing-engines

- Dataproc & Spark for Machine Learning 
  - cloud.google.com/dataproc/docs/tutorials/bigquery-sparkml
