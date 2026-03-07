# run.py
import os
import sys
from dotenv import load_dotenv

# Load .env before anything else
load_dotenv()

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.app import app
from database.db_manager import DatabaseManager

def main():
    """
    Control Group 챗봇 실행 파일
    """
    # 환경 변수 확인
    if not os.getenv('AZURE_OPENAI_API_KEY'):
        print("⚠️  경고: AZURE_OPENAI_API_KEY가 설정되지 않았습니다.")
        print("📝 .env 파일에 AZURE_OPENAI_API_KEY를 추가해주세요.")
        return
    
    # 데이터베이스 초기화 (DatabaseManager.__init__에서 자동 호출됨)
    print("🔧 데이터베이스 초기화 중...")
    db_path = os.getenv('DATABASE_PATH', 'database/chatbot.db')
    db = DatabaseManager(db_path=db_path)
    print("✅ 데이터베이스 준비 완료")
    
    # 서버 실행
    print("\n" + "="*50)
    print("🤖 Control Group 챗봇 서버 시작")
    print("="*50)
    print("📍 URL: http://localhost:5001")
    print("🛑 종료하려면 Ctrl+C를 누르세요")
    print("="*50 + "\n")
    
    app.run(
        host='0.0.0.0',
        port=5001,
        debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    )

if __name__ == '__main__':
    main()