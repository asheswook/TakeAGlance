import csv
  
def csv_to_dict(): #csv data 전체를 디셔너리에 담음.
    csv_data={}
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader: # row는 list형태로 저장되어 있음.
            if not bool(row) or row==['img_label','img_path']:
                continue
            else:
                csv_data[row[0]]=row[1]
                
    
    return csv_data

def adding_data_to_csv(new_row: list):
    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(new_row)
        else:
            csvfile.write('\n')
            writer.writerow(new_row)
    
    csv_to_dict()

def save_data_to_csv(img_label, img_path): # 이름 좀 잘못 지었는데...
    new_row=[img_label, img_path]
    adding_data_to_csv(new_row)
        

def csv_data_visualization():
    trs=[]
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        num=0
        for row in csv_reader:
            if not row:
                continue
            if num==0:
                num+=+1 # csv의 head를 출력 안 하기 위함.
                continue
            href = '{{url_for(static, filename={})}}'.format(row[1])
            tr_=f'<tr><th scope=row>{num}</th><td>{row[0]}</td><td>{row[1]}</td></tr>' # 그냥 파일 이름이 보임.
            #tr_ = f'<tr><th scope=row>{num}</th><td>{row[0]}</td><td><a href="{{url_for(static, filename={row[1]})}}">{row[1]}</a></td></tr>'

            trs.append(tr_)
            num+=+1
    
    trs=' '.join(trs)
    return trs


def vs_in_csv_confirm(vs_row: list, csv_data: dict): # vs 데이터가 csv에 있는지 확인 후 처리.
    # csv data에 vs_data가 있는지 확인
    if vs_row[0] not in list(csv_data.keys()) or vs_row[1] not in list(csv_data.values()): # vs 데이터가 존재하지 않을 때
        adding_data_to_csv(vs_row)
    else:# 데이터가 존재할 때
        print(csv_data)
        print(csv_data[vs_row[0]], 'add_csv')
            

        
    
    

            
