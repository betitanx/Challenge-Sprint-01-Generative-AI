import csv
from pathlib import Path

CSV_PATH = Path('data/synthetic_motor_records.csv')


def to_float(v):
    try:
        return float(v)
    except ValueError:
        return None


def main():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f'Arquivo não encontrado: {CSV_PATH}')

    with CSV_PATH.open('r', encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))

    errors = []

    if len(rows) != 200:
        errors.append(f'Quantidade de registros esperada: 200, encontrada: {len(rows)}')

    required_cols = {
        'record_id', 'timestamp', 'motor_id', 'rpm', 'temperature_c', 'vibration_mm_s',
        'current_a', 'fault_label', 'severity', 'work_order', 'maintenance_report',
        'model', 'temperature', 'top_p', 'prompt_template', 'validation_status'
    }
    missing = required_cols - set(rows[0].keys() if rows else [])
    if missing:
        errors.append(f'Colunas ausentes: {sorted(missing)}')

    temp_values, vib_values, approved_count = [], [], 0
    for i, row in enumerate(rows, start=1):
        temp = to_float(row['temperature_c'])
        vib = to_float(row['vibration_mm_s'])
        curr = to_float(row['current_a'])
        status = row['validation_status']

        if temp is None or not (30 <= temp <= 130):
            errors.append(f'Linha {i}: temperatura inválida ({row["temperature_c"]}).')
        else:
            temp_values.append(temp)

        if vib is None or not (0.5 <= vib <= 20):
            errors.append(f'Linha {i}: vibração inválida ({row["vibration_mm_s"]}).')
        else:
            vib_values.append(vib)

        if curr is None or not (10 <= curr <= 120):
            errors.append(f'Linha {i}: corrente inválida ({row["current_a"]}).')

        if status not in {'aprovado', 'revisar'}:
            errors.append(f'Linha {i}: validation_status inválido ({status}).')
        if status == 'aprovado':
            approved_count += 1

    if errors:
        print('❌ Validação falhou:')
        for e in errors[:20]:
            print(f'- {e}')
        if len(errors) > 20:
            print(f'- ... e mais {len(errors) - 20} erros')
        raise SystemExit(1)

    print('✅ Validação concluída com sucesso!')
    print(f'- Registros: {len(rows)}')
    print(f"- Taxa 'aprovado': {approved_count/len(rows):.2%}")
    print(f"- Temperatura média: {sum(temp_values)/len(temp_values):.2f} °C")
    print(f"- Vibração média: {sum(vib_values)/len(vib_values):.2f} mm/s")


if __name__ == '__main__':
    main()
