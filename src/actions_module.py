# Agent B의 모든 AWS 액션을 정의하는 모듈 (팀 B 담당)
import logging
import uuid # 롤백 데이터를 위한 고유 ID 생성 (Mock)

logger = logging.getLogger()

# 🚨 1. EC2 인스턴스를 격리용 SG로 교체합니다.
# 반환값에 원래 SG ID가 포함되어야 팀 D가 롤백을 준비할 수 있습니다.
def isolate_instance(instance_id: str):
    logger.info(f"MOCK: {instance_id} 격리 액션 호출됨.")
    
    # 🚨🚨 Mock 반환 데이터 (팀 D와의 약속)
    return {
        "action_id": str(uuid.uuid4()),
        "action_name": "isolate_instance",
        "resource_id": instance_id,
        "status": "MOCK_SUCCESS",
        "rollback_data": {
            "original_sg_id": "sg-original-1a2b3c4d5e", # 롤백에 필수
            "new_sg_id": "SG-ISOLATE-DENY-ALL"
        }
    }

# 🚨 2. 특정 IP 주소를 AWS WAF 블랙리스트에 추가합니다.
def block_ip(source_ip: str):
    logger.info(f"MOCK: {source_ip} WAF 블랙리스트 추가 호출됨.")
    
    # 🚨🚨 Mock 반환 데이터 (팀 D와의 약속)
    return {
        "action_id": str(uuid.uuid4()),
        "action_name": "block_ip",
        "resource_id": source_ip,
        "status": "MOCK_SUCCESS",
        "rollback_data": {
            "waf_set_id": "ipset-mock-12345", 
            "original_ip_set": "original_set_A"
        }
    }

# 🚨 3. EC2 디스크 스냅샷을 생성합니다 (포렌식 준비)
def create_snapshot(instance_id: str):
    logger.info(f"MOCK: {instance_id} 스냅샷 생성 호출됨.")
    return {
        "action_id": str(uuid.uuid4()),
        "action_name": "create_snapshot",
        "resource_id": instance_id,
        "status": "MOCK_SUCCESS",
        "snapshot_id": "snap-mock-abc12345"
    }

# 🚨 4. Slack으로 알림을 전송합니다.
def notify_to_slack(message: str):
    logger.info(f"MOCK: Slack 알림 전송 호출됨. 메시지: {message[:20]}...")
    return {"action_name": "notify_to_slack", "status": "MOCK_SUCCESS"}
