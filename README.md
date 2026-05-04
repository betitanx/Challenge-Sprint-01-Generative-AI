# Sprint 1 — Fundamentos de IA Generativa para Domínio Industrial

Este repositório contém os artefatos da Sprint 1 com foco em:
- estudo comparativo de arquiteturas generativas;
- engenharia de prompts para motores elétricos industriais;
- geração e validação de dados sintéticos rotulados.

## Estrutura

- `notebooks/sprint1_genai_fundamentos.ipynb`: notebook executável com todo o fluxo da sprint.
- `data/synthetic_motor_records.csv`: 200 registros sintéticos com metadados de geração e validação.
- `docs/prompt_guide.md`: guia reutilizável de prompts e critérios de seleção de modelos.
- `scripts/generate_synthetic_data.py`: gerador determinístico do dataset sintético.
- `scripts/validate_synthetic_data.py`: validações automáticas de qualidade e schema do dataset.

## Como reproduzir

1. Abra o notebook no Colab.
2. Execute as células de setup e geração.
3. Ajuste modelo/API key conforme disponibilidade.

## Existe alguma aplicação para testar?

Nesta sprint **não há aplicação web** (frontend/backend) para execução de interface.
Os testes aqui são de **pipeline de dados e qualidade dos artefatos**.

### Testes recomendados

```bash
python3 scripts/generate_synthetic_data.py
python3 scripts/validate_synthetic_data.py
python3 -m json.tool notebooks/sprint1_genai_fundamentos.ipynb >/dev/null
```

Esses comandos validam:
- geração dos 200 registros;
- schema, faixas físicas e consistência básica dos dados sintéticos;
- integridade do notebook (`.ipynb`) em formato JSON.
