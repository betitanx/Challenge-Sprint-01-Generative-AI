import csv, random, datetime

random.seed(42)

def pick_fault(temp, vib, current):
    if temp > 95 and vib > 8:
        return "Sobreaquecimento com desalinhamento"
    if current > 85:
        return "Sobrecorrente por atrito mecânico"
    if vib > 10:
        return "Desbalanceamento de rotor"
    return "Operação normal"

rows=[]
start=datetime.datetime(2026,1,1)
for i in range(200):
    ts = start + datetime.timedelta(hours=i*6)
    motor_id=f"MTR-{1000+i%25:04d}"
    rpm=random.randint(1200,3600)
    temp=round(random.uniform(45,110),1)
    vib=round(random.uniform(1.2,12.5),2)
    curr=round(random.uniform(15,95),1)
    fault=pick_fault(temp,vib,curr)
    sev = "alta" if fault!="Operação normal" and (temp>90 or vib>9 or curr>80) else ("média" if fault!="Operação normal" else "baixa")
    wo=f"WO-{20260000+i:08d}"
    report=(
        f"Inspeção do motor {motor_id}: temperatura {temp}°C, vibração {vib} mm/s, corrente {curr} A. "
        f"Diagnóstico: {fault}. Ação recomendada: {'realinhar e lubrificar' if fault!='Operação normal' else 'manter monitoramento padrão'}."
    )
    rows.append({
        "record_id": i+1,
        "timestamp": ts.isoformat(),
        "motor_id": motor_id,
        "rpm": rpm,
        "temperature_c": temp,
        "vibration_mm_s": vib,
        "current_a": curr,
        "fault_label": fault,
        "severity": sev,
        "work_order": wo,
        "maintenance_report": report,
        "model": random.choice(["gpt-4.1-mini","llama-3.1-8b-instruct","gemma-2-9b-it"]),
        "temperature": random.choice([0.2,0.4,0.7]),
        "top_p": random.choice([0.85,0.9,0.95]),
        "prompt_template": random.choice(["zero_shot_diag_v1","few_shot_os_v2","cot_analysis_v1","roleplay_engineer_v1"]),
        "validation_status": "aprovado" if fault=="Operação normal" or random.random()>0.06 else "revisar"
    })

with open('data/synthetic_motor_records.csv','w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)

print('generated',len(rows))
