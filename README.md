# AWS Compromise playbook - Cloudtrail focussed
You're on an active incident, the threat actor is seen with access to your AWS environment and the devsecops folks have given you what seems like 50,000 log files inside 20000 folders - what are your next steps?

When cloudtrail is dumped from an S3 bucket storage and given to you, sometimes it's like this:
```
Cloudtrail/
└── eu-west-1/
    └── 2024/
        └── 02/
            └── 31/
                ├── 012345_CloudTrail_eu-west-1_20230118T1420Z_85IofXHXJ7eOjN3Y.json
                ├── 567890_CloudTrail_eu-west-1_20230118T1420Z_85IofXHXJ7eOjN3Y.json
                ├── 123456_CloudTrail_eu-west-1_20230118T1420Z_85IofXHXJ7eOjN3Y.json
                ├── 678901_CloudTrail_eu-west-1_20230118T1420Z_85IofXHXJ7eOjN3Y.json
                └── 234567_CloudTrail_eu-west-1_20230118T1420Z_85IofXHXJ7eOjN3Y.json
```

### Let's get this information overload under control and ready for analysis, fast and free:

1. Copy .json files out of the sub dirs and into one dir by using the [copy_into_dir.py](copy_into_dir.py) file.
2. Merge them into one file, unflatten them with:

```cat ./* | jq '.Records[]' >> all_files.json```

4. Get them into your SIEM of choice, I'm using splunk - because it takes me 10 seconds:
#### Add data
![image](https://github.com/Broomey28/aws_cloudtrail_analysis/assets/56151530/72fc62a9-4665-4941-9b92-45a2ce2d6e28)

#### Upload file

![image](https://github.com/Broomey28/aws_cloudtrail_analysis/assets/56151530/0ef7a782-25d2-4356-a7e5-f1eeb70f94be)

#### Make sure sourcetype is json + the fields are populated/normal

![image](https://github.com/Broomey28/aws_cloudtrail_analysis/assets/56151530/aae1f8f1-36f1-4570-ad85-7bb3dac67ad7)

#### Create a separate index + ensure it ONLY has the relevant incident data and is the same sourcetype
![image](https://github.com/Broomey28/aws_cloudtrail_analysis/assets/56151530/f1e594c3-803d-47bc-81e9-054ee282d78d)

# Ready for analysis, fast.
Check out some of the [pre-made searches](AWS_searches.md) for various use cases as your starting point and you're good to go.



