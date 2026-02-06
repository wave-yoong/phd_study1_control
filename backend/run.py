# run.py
import os
from backend.app import create_app
from backend.database.db_manager import DatabaseManager

def main():
    """
    Control Group 챗봇 실행 파일
    """
    # 환경 변수 확인
    if not os.getenv('OPENAI_API_KEY'):
        print("⚠️  경고: OPENAI_API_KEY가 설정되지 않았습니다.")
        print("📝 .env 파일에 OPENAI_API_KEY를 추가해주세요.")
        return
    
    # 데이터베이스 초기화
    print("🔧 데이터베이스 초기화 중...")
    db = DatabaseManager()
    db.initialize_database()
    print("✅ 데이터베이스 준비 완료")
    
    # Flask 앱 생성
    app = create_app()
    
    # 서버 실행
    print("\n" + "="*50)
    print("🤖 Control Group 챗봇 서버 시작")
    print("="*50)
    print("📍 URL: http://localhost:5000")
    print("🛑 종료하려면 Ctrl+C를 누르세요")
    print("="*50 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

if __name__ == '__main__':
    main()