# Agent B의 메인 엔진 핸들러 (팀 A 담당)
import json
import logging
from . import playbooks_module

# 로깅 설정
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 🚨 GuardDuty 위협 타입과 실행할 플레이북 함수 매핑
# 이 지도를 기반으로 런타임 이벤트가 라우팅됩니다. (팀 A와 C의 약속)
PLAYBOOK_MAP = {
    "S3-Policy-Change": playbooks_module.playbook_s3_public_access,
    "UnauthorizedAccess:EC2/MaliciousIPCaller.Custom": playbooks_module.playbook_ec2_isolate,
    # 여기에 다른 GuardDuty 위협 타입과 플레이북을 추가합니다.
}

def lambda_handler(event, context):
    """
    AWS EventBridge로부터 GuardDuty 이벤트를 수신하여 플레이북을 실행합니다.
    """
    try:
        # 이벤트 JSON에서 위협 타입 추출 (실제 GuardDuty 이벤트 구조를 기반으로 함)
        detail_type = event.get('detail', {}).get('type')
        
        # 매핑된 플레이북 함수를 찾습니다.
        playbook_function = PLAYBOOK_MAP.get(detail_type)

        if playbook_function:
            logger.info(f"위협 감지: {detail_type}. 플레이북 실행: {playbook_function.__name__}")
            # 팀 C의 플레이북 함수 호출
            result = playbook_function(event)
            return {"status": "SUCCESS", "result": result}
        else:
            logger.warning(f"알 수 없는 위협 타입: {detail_type}. 무시합니다.")
            return {"status": "SKIPPED", "message": "No matching playbook."}

    except Exception as e:
        logger.error(f"엔진 실행 중 오류 발생: {e}")
        return {"status": "ERROR", "message": str(e)}
