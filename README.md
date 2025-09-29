# 데이터 통합 프로젝트

## 📋 프로젝트 개요

이 프로젝트는 Welcome과 Quickpoll 데이터를 통합하는 프로세스를 담고 있습니다.

### 🎯 목적
- **Welcome 파일 2개**와 **Quickpoll 파일 35개**를 `mb_sn`을 기준으로 통합
- **데이터 소스**: `../data/raw/` 폴더의 Excel 파일들
- **통합 기준**: `mb_sn` 컬럼을 사용한 Outer Join
- **결과**: 모든 패널 데이터를 포함한 통합 데이터셋 생성

## 📁 데이터 구조

### Welcome 파일
- **파일 수**: 2개
- **헤더 위치**: 첫 번째 행 (header=0)
- **특징**: 기본 패널 정보 포함
- **파일명**: `Welcome_1st.xlsx`, `Welcome_2nd.xlsx`

### Quickpoll 파일
- **파일 수**: 35개
- **헤더 위치**: 두 번째 행 (header=1)
- **특징**: 설문 응답 데이터 포함
- **파일명**: `qpoll_join_YYYYMMDD.xlsx` 형식

## 🔧 처리 과정

### 1단계: Welcome 파일 통합
```python
# Welcome 파일들을 먼저 통합하여 기본 DataFrame 생성
base_df = pd.read_excel(welcome_files[0])
# '고유번호' 컬럼을 'mb_sn'으로 변경
base_df.rename(columns={'고유번호': 'mb_sn'}, inplace=True)
# 나머지 Welcome 파일들 통합
```

### 2단계: Quickpoll 파일 통합 (테스트)
```python
# 처음 5개 파일만 테스트하여 안정성 확인
test_files = quickpoll_files[:5]
```

### 3단계: Quickpoll 파일 통합 (전체)
```python
# 나머지 30개 파일 처리
remaining_files = quickpoll_files[5:]
```

## 🛠️ 주요 기능

### 메모리 효율성
- 각 파일 처리 후 메모리 정리 (`del` 명령)
- `.copy()` 사용으로 불필요한 메모리 참조 방지
- 단계적 처리로 메모리 부족 방지

### 에러 핸들링
- `try-except` 블록으로 파일 읽기 오류 처리
- 오류 발생 시 해당 파일을 건너뛰고 계속 진행
- 상세한 오류 메시지 출력

### 진행상황 모니터링
- 파일별 진행률 표시 `[1/35]`, `[2/35]` 등
- 파일 크기와 메모리 사용량 표시
- 5개 파일마다 전체 진행률 출력

## 📊 데이터 처리 특징

### 컬럼 처리
- **공통 정보 컬럼**: `['구분', 'mb_sn', '성별', '나이', '지역', '설문일시']`
- **설문 답변 컬럼**: 파일명을 접미사로 추가하여 고유성 확보
- **예시**: `Q1_250106`, `Q2_250106` 등

### 병합 방식
- **Outer Join**: 모든 패널 데이터 보존
- **중복 컬럼 정리**: `_x`, `_y` 컬럼을 하나로 통합
- **메모리 최적화**: 필요한 컬럼만 선택하여 병합

## 🚀 사용 방법

### 1. 환경 설정
```bash
# conda 환경 활성화
conda activate pannel

# 필요한 패키지 설치
pip install -r requirements.txt
```

### 2. 노트북 실행
1. **커널 선택**: `Python (pannel)` 커널 사용
2. **단계별 실행**: 
   - Welcome 파일 통합
   - Quickpoll 파일 테스트 (5개)
   - Quickpoll 파일 전체 처리 (30개)
3. **결과 확인**: 통합된 데이터 크기 및 정보 확인

### 3. 결과 저장
```python
# 통합된 데이터를 CSV 파일로 저장
output_path = '../data/processed/01_consolidated_data.csv'
base_df.to_csv(output_path, index=False, encoding='utf-8-sig')
```

## 📈 예상 결과

### 데이터 크기
- **Welcome 통합 후**: 약 35,240개 행, 26개 열
- **Quickpoll 통합 후**: 약 35,240개 행, 수백 개 열 (설문 응답 포함)

### 처리 시간
- **Welcome 파일**: 1-2분
- **Quickpoll 테스트**: 2-3분
- **Quickpoll 전체**: 10-15분

## ⚠️ 주의사항

### 메모리 관리
- 대용량 데이터 처리 시 메모리 사용량 모니터링 필요
- 커널 종료 시 conda 환경 `pannel` 사용 확인

### 파일 형식
- Excel 파일의 헤더 위치가 다를 수 있음
- Welcome: header=0, Quickpoll: header=1

### 에러 처리
- 파일 읽기 실패 시 해당 파일 건너뛰기
- 진행상황을 통해 문제 파일 식별 가능

## 🔍 문제 해결

### 커널 종료 문제
1. **커널 변경**: `Python (pannel)` 사용
2. **테스트 모드**: 처음 5개 파일만 처리
3. **메모리 정리**: 각 파일 처리 후 `del` 명령

### 파일 읽기 오류
1. **에러 핸들링**: `try-except` 블록 사용
2. **진행상황 모니터링**: 문제 파일 식별
3. **단계적 처리**: 안정성 확인 후 전체 처리

## 📝 요구사항

### Python 패키지
```
pandas>=2.0.0
numpy>=1.24.0
openpyxl>=3.1.0
xlrd>=2.0.0
jupyter>=1.0.0
ipykernel>=6.25.0
```

### 시스템 요구사항
- **메모리**: 최소 8GB RAM 권장
- **저장공간**: 데이터 크기에 따라 충분한 여유공간 필요
- **Python**: 3.8 이상

## 📞 지원

문제가 발생하면 다음을 확인하세요:
1. conda 환경 `pannel` 활성화 상태
2. 필요한 패키지 설치 여부
3. 파일 경로 및 권한 확인
4. 메모리 사용량 모니터링

---

**프로젝트 완료일**: 2025년 1월
**데이터 소스**: Welcome 2개 파일, Quickpoll 35개 파일
**통합 결과**: 단일 통합 데이터셋 생성
