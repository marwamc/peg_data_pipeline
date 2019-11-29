# PEGAfrica Generic Data Pipeline
A generic data  pipeline - inspired by SparkContext


### RELEASE PROCESS

tags:
    v0.0.1-Alpha   (Private)
    v0.0.1-Beta    (DEV)
    v0.0.1         (PROD)
   

### LOCAL DEVELOPMENT
    ap data-dev 
    ./run docker-build
    ./run shell
    ./run setup
    
    (happy coding in IDE of choice...)


### DEPLOYMENT PROCESS

Before deploying, ensure the following externally managed infra exists:
    
    S3:
    (deployment bucket)
    (config bucket)
    
    SNS TOPICS:
    (low urgency)
    (high urgency)

      
    
###### DEPLOY STACK TO DEV:
    aws-vault --debug exec data-dev-admin --session-ttl=1h --assume-role-ttl=1h
    
    ./run docker-build
    ./run shell
    ./run setup
    ./run sls-dev
    
###### DEPLOY STACK TO PROD:
    aws-vault --debug exec datap-rod-admin --session-ttl=1h --assume-role-ttl=1h
    
    ./run docker-build
    ./run shell
    ./run setup   
    ./run sls-prod

      
# MISC Commands
     ap data-dev-admin
     aws-vault --debug exec data-dev-admin --session-ttl=1h --assume-role-ttl=1h
     npm install serverless-pseudo-parameters
     pip3 install pynamodb==4.2.0 -t `pwd`
     SLS_DEBUG=* sls deploy -v --force --stage dev
     sls logs -f Requestor -t
     sls logs -f Extractor -t
     
     sls deploy -v --aws-profile data-dev -f CompressJob
     
     SLS_DEBUG=* sls deploy -v  --force --stage dev -f Scheduler

