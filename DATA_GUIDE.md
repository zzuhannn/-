# 데이터 파일 관리 가이드

## 📁 데이터 파일 구조

```
data/
├── raw/           # 원본 데이터 (GitHub에 업로드 안함)
│   ├── Welcome/   # Welcome Excel 파일들
│   └── Quickpoll/ # Quickpoll Excel 파일들
├── processed/     # 처리된 데이터 (GitHub에 업로드 안함)
│   └── *.csv     # 통합된 CSV 파일들
└── sample/        # 샘플 데이터 (GitHub에 업로드)
    └── sample_data.csv
```

## 🚫 GitHub에 올리지 않는 파일들

### 이유:
- **대용량 파일**: GitHub 파일 크기 제한 (100MB)
- **저장소 크기**: 클론 속도 저하
- **보안**: 민감한 개인정보 포함 가능

### 제외되는 파일들:
- `data/raw/*.xlsx` - 원본 Excel 파일들
- `data/processed/*.csv` - 통합된 대용량 CSV 파일들
- `*.xlsx` - 모든 Excel 파일

## ✅ GitHub에 올리는 파일들

### 포함되는 파일들:
- `data/sample/*.csv` - 샘플 데이터 (1000행 이하)
- `notebooks/*.ipynb` - Jupyter 노트북
- `requirements.txt` - Python 패키지 목록
- `README.md` - 프로젝트 설명
- `DATA_GUIDE.md` - 데이터 관리 가이드

## 🔧 데이터 접근 방법

### 로컬에서 데이터 사용:
```python
# 원본 데이터 경로
raw_data_path = '../data/raw/'

# 처리된 데이터 경로  
processed_data_path = '../data/processed/01_consolidated_data.csv'
```

### 샘플 데이터 사용:
```python
# 샘플 데이터 경로
sample_data_path = '../data/sample/sample_data.csv'
```

## 📊 데이터 크기 정보

- **원본 파일**: 37개 Excel 파일
- **통합 데이터**: 36,113명 × 67개 컬럼
- **파일 크기**: 약 50-100MB (CSV)

## 🔒 데이터 보안

- 개인정보가 포함된 데이터는 GitHub에 업로드하지 않음
- 로컬에서만 데이터 처리 및 분석
- 공개용 샘플 데이터만 GitHub에 업로드

## 📝 사용 방법

1. **로컬에서 데이터 다운로드**
2. **노트북 실행하여 데이터 통합**
3. **분석 결과만 GitHub에 업로드**
4. **샘플 데이터로 코드 테스트**

---

**주의**: 실제 데이터는 GitHub에 업로드하지 마세요!
