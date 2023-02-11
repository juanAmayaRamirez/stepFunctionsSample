# StepFunctions Bookstore
## [WORK IN PROGRESS]
This Repo is completly based on the video **AWS Step Functions Crash Course | Step by Step Tutorial** which uses the serverless framework and nodejs.  
* https://github.com/mjzone/sfn-crash-course
* https://www.youtube.com/watch?v=jXxKRd_9nC0

The main diference are:  
* It is used cloudformation templates with SAM custom resources.
* Python is used for the lambdas.
* Logging is enabled with a custom loggroup
* ApiGateway direct integration with StepFunctions EXPRESS `StartSyncExecution` is used.
* more control over the IAM resources created (Roles and Policies)
