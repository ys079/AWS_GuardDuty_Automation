# 시나리오 정의 및 액션 조립 (팀 C 담당)
from . import actions_module
from . import db_logger_module
import logging

logger = logging.getLogger()

# 🚨 시나리오 1: EC2 인스턴스 격리 (중간 난이도)
def playbook_ec2_isolate(event: dict):
    logger.info("플레이북 1: EC2 자동 격리 시작")
    
    # 1. 이벤트에서 리소스 ID 추출 (팀 C의 분석 역할)
    incident_id = event.get('id', 'N/A')
    instance_id = event.get('detail', {}).get('resource', {}).get('instanceId', 'i-mock-12345')
    
    # 2. 격리 액션 실행 (팀 B 함수 호출)
    isolate_result = actions_module.isolate_instance(instance_id)
    
    # 3. 대응 이력 로깅 (팀 D 함수 호출)
    db_logger_module.log_action(incident_id, isolate_result)

    # 4. 포렌식 준비 액션 실행 (팀 B 함수 호출)
    snapshot_result = actions_module.create_snapshot(instance_id)
    db_logger_module.log_action(incident_id, snapshot_result)

    # 5. 최종 알림
    actions_module.notify_to_slack(f"EC2 {instance_id} 격리 완료 및 스냅샷 생성. Incident ID: {incident_id}")
    
    return {"status": "EC2_ISOLATED_AND_LOGGED", "incident_id": incident_id}

# 🚨 시나리오 2: S3 퍼블릭 접근 차단 (쉬운 난이도)
def playbook_s3_public_access(event: dict):
    logger.info("플레이북 2: S3 퍼블릭 접근 차단 시작")

    # 1. 이벤트에서 리소스 ID 추출
    incident_id = event.get('id', 'N/A')
    bucket_name = event.get('detail', {}).get('resource', {}).get('bucketName', 's3-mock-bucket')

    # 2. IP 차단 액션은 없으므로, 격리 대신 바로 차단 액션 실행 (Mock)
    # (팀 B가 나중에 'block_s3_public_access' 함수를 구현했다고 가정)
    block_result = actions_module.block_ip(bucket_name) # 임시로 block_ip 사용

    # 3. 대응 이력 로깅
    db_logger_module.log_action(incident_id, block_result)

    # 4. 최종 알림
    actions_module.notify_to_slack(f"S3 {bucket_name} 퍼블릭 접근 차단 완료. Incident ID: {incident_id}")

    return {"status": "S3_BLOCKED_AND_LOGGED", "incident_id": incident_id}

```"
