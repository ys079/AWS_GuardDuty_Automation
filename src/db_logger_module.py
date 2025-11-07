# 대응 이력 및 롤백 데이터 로거 (팀 D 담당)
import logging
import datetime
# boto3는 3주차에 추가됩니다.

logger = logging.getLogger()

# 🚨 롤백을 위해 액션 실행 정보를 DynamoDB에 기록합니다.
# team_b_result: 팀 B의 actions_module 함수에서 반환된 데이터 (팀 D와의 약속)
def log_action(incident_id: str, team_b_result: dict):
    logger.info(f"MOCK: DynamoDB에 이력 저장 시도.")
    
    # 🚨🚨 Mock 로깅 로직 (실제 DB 코드 대신 출력만)
    log_entry = {
        "IncidentId": incident_id,
        "Timestamp": datetime.datetime.now().isoformat(),
        "ActionDetails": team_b_result 
    }
    
    logger.info(f"MOCK Log Entry: {json.dumps(log_entry)}")
    logger.info("MOCK: 로깅 완료. 팀 D는 이 데이터를 기반으로 롤백 로직을 구현합니다.")
    return {"status": "MOCK_LOGGED", "log_id": incident_id}
