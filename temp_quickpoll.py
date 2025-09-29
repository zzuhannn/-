# --- 1단계: 모든 파일에서 고유한 패널 ID(mb_sn) 전체 명단 만들기 ---
print("--- 1단계: 전체 패널 마스터 명단 생성 시작 ---")
all_panel_ids = set()

for file in all_files:
    try:
        # 💡 header=1을 가정하고, '고유번호' 또는 'mb_sn' 컬럼만 읽어옵니다.
        # Welcome 파일에 대한 예외 처리를 추가합니다.
        header_row = 0 if 'Welcome' in file else 1
        df_id = pd.read_excel(file, header=header_row)
        
        if '고유번호' in df_id.columns:
            all_panel_ids.update(df_id['고유번호'].dropna().unique())
        elif 'mb_sn' in df_id.columns:
            all_panel_ids.update(df_id['mb_sn'].dropna().unique())
            
    except Exception as e:
        print(f"  [경고] {os.path.basename(file)} 파일 처리 중 오류: {e}")

# 고유한 ID 목록으로 최종 기준이 될 base_df 생성
base_df = pd.DataFrame(list(all_panel_ids), columns=['mb_sn'])
print(f"--- 마스터 명단 생성 완료! 총 고유 패널 수: {len(base_df)}명 ---")

# --- 2단계: 마스터 명단에 파일별 정보 채워넣기 (Left Join) ---
print("\n--- 2단계: 파일별 정보 병합 시작 ---")
welcome_files = glob.glob(os.path.join(base_path, 'Welcome/*.xlsx'))
quickpoll_files = glob.glob(os.path.join(base_path, 'Quickpoll/*.xlsx'))

# 먼저 Welcome 파일(핵심 인구통계 정보)을 병합합니다.
for file in welcome_files:
    print(f"병합 중: {os.path.basename(file)}")
    temp_df = pd.read_excel(file) # Welcome은 header가 첫 줄에 있다고 가정
    base_df = pd.merge(base_df, temp_df, on='mb_sn', how='left')

# 다음으로 Quickpoll 파일을 병합합니다.
common_info_cols = ['구분', 'mb_sn', '성별', '나이', '지역', '설문일시']
for file in quickpoll_files:
    filename = os.path.basename(file).split('.')[0]
    print(f"병합 중: {filename}.xlsx")
    temp_df = pd.read_excel(file, header=1)
    
    if '고유번호' in temp_df.columns:
        temp_df.rename(columns={'고유번호': 'mb_sn'}, inplace=True)
    
    if 'mb_sn' in temp_df.columns:
        answer_cols = [col for col in temp_df.columns if col not in common_info_cols]
        rename_dict = {col: f"{col}_{filename}" for col in answer_cols}
        temp_df.rename(columns=rename_dict, inplace=True)
        unique_answer_cols = list(rename_dict.values())
        merge_target_df = temp_df[['mb_sn'] + unique_answer_cols]
        base_df = pd.merge(base_df, merge_target_df, on='mb_sn', how='left')
    
    # 메모리 정리
    del temp_df
    gc.collect()

print("\n🎉 최종 데이터 통합 완료!")
print(f"최종 데이터 크기: {base_df.shape[0]}개의 행, {base_df.shape[1]}개의 열")
