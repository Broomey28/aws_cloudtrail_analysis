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

Firstly, let's copy all of the files out of the sub dirs and into one dir by using the 
