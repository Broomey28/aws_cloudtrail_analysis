# Splunk searches
[Who is getting objects from S3 buckets](#who-is-getting-objects-from-s3-buckets-successfully)

[policy changes](#who's-been-making-policy-changes)


## Who is getting objects from S3 buckets (successfully):
```
index="<indexname>"  eventName=GetObject  "requestParameters.bucketName"="<s3bucketname>"
| search  NOT errorMessage=*
| rename userIdentity.accountId as accountID
| rename sourceIPAddress as src_ip 
| rename resources{}.type as res_type
| rename requestParameters.bucketName as bucket
| rename requestParameters.key as files
| table eventTime awsRegion  errorCode accountID src_ip res_type bucket files

| sort 0 +eventTime
```

## Is there key generation
#num2

```
index="nub_cloudtrail"  eventName=CreateKeyPair "userIdentity.userName"="<insert IAM user if you want to narrow down>"
| table eventTime eventSource awsRegion eventName requestParameters.keyFormat requestParameters.keyName  userIdentity.userName userIdentity.type
 sourceIPAddress userAgent responseElements.keyPairId


| sort 0 +eventTime
```

## How many EC2 instances have been launched? (Per IAM user)

```
index="nub_cloudtrail" eventName=RunInstances 
| search NOT errorCode="*Invalid*" NOT eventName=*describe*
| stats count by userIdentity.userName, requestParameters.instancesSet.items{}.minCount
| eval total_ec2s='requestParameters.instancesSet.items{}.minCount' * count
| stats sum(total_ec2s) as total_launched_ec2s by userIdentity.userName
| table userIdentity.userName total_launched_ec2s
```

## Information about created EC2 instances:

```
index="nub_cloudtrail" eventName=RunInstances 
| rename eventTime as time 
| rename userIdentity.userName as username 
| rename userIdentity.type as usertype
| rename sourceIPAddress as src_ip 
| rename responseElements.instancesSet.items{}.instanceId as instanceID
| rename requestParameters.instancesSet.items{}.imageId as imageID  
| rename requestParameters.instanceType as instanceType 
| rename requestParameters.networkInterfaceSet.items{}.associatePublicIpAddress as public_ip 
| rename requestParameters.networkInterfaceSet.items{}.subnetId as subnet
| rename responseElements.instancesSet.items{}.vpcId as vpc_id
| table time eventSource awsRegion eventName username usertype
 src_ip subnet vpc_id userAgent instanceID imageID instanceType public_ip
| sort 0 +eventTime
```

## Terminated EC2 instances:

```
index="nub_cloudtrail" eventName=*TerminateInstances* 
| table eventTime eventSource awsRegion eventName  userIdentity.type
 sourceIPAddress requestParameters.instancesSet.items{}.instanceId

| sort 0 +eventTime
```
## Who's been making policy changes?

```
index="nub-2-cloudtrail" eventName="*policy*" "userIdentity.arn"="arn:aws:iam::949622803460:user/dev-policy-specialist"
| rename eventTime as time 
| rename awsRegion as region
| rename requestParameters.policyArn as  policyarn 
| rename requestParameters.policyName as polName 
| rename requestParameters.policyDocument as polDoc 
| rename userIdentity.userName as username 
| rename sourceIPAddress as src_ip
| table time region readOnly policyarn polName polDoc username src_ip
| sort 0 +time
```
