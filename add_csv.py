import csv

def save_data_to_csv(img_label, img_path):
    new_row=[img_label, img_path]
    with open('data.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(new_row)
        csvfile.close()
        

def reading_csv_Data():
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
            href = '{{url_for(\'static\', filename={})}}'.format(row[1])
            #tr_=f'<tr><th scope=row>{num}</th><td>{row[0]}</td><td<a href={row[1]}>{row[1]}</a></td></tr>'
            tr_ = f'<tr><th scope=row>{num}</th><td>{row[0]}</td><td><a href="{{url_for(static, filename={row[1]})}}">{row[1]}</a></td></tr>'

            trs.append(tr_)
            num+=+1
    
    trs=' '.join(trs)
    return trs
    
    