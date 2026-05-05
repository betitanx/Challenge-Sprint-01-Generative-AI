# Checklist de Entrega — Sprint 1

## Referência do formato exigido

1. Notebook Colab `sprint1_genai_fundamentos.ipynb` com:
   - estudo comparativo de modelos,
   - biblioteca de prompts implementada,
   - pipeline de geração de dados sintéticos executado/documentado.
2. Arquivo JSON ou CSV com dados sintéticos + metadados (`prompt`, `modelo`, `temperatura`, `validação`).
3. Documento com prompt guide + critérios de seleção de modelos.

## Verificação dos artefatos atuais

### 1) Notebook Colab
- Arquivo presente: `notebooks/sprint1_genai_fundamentos.ipynb` ✅
- Contém seção de comparativo de arquiteturas/modelos ✅
- Contém biblioteca de prompts (zero-shot, few-shot, CoT, role-play) ✅
- Contém carga e checagens do dataset sintético ✅

### 2) Dataset sintético (CSV/JSON)
- Arquivo presente: `data/synthetic_motor_records.csv` ✅
- Quantidade mínima: 200 registros (201 linhas com cabeçalho) ✅
- Campos de metadados incluídos:
  - `prompt_template` ✅
  - `model` ✅
  - `temperature` ✅
  - `top_p` ✅
  - `validation_status` ✅

### 3) Prompt guide e critérios de seleção
- Arquivo presente: `docs/prompt_guide.md` ✅
- Critérios de seleção documentados ✅
- Templates reutilizáveis documentados ✅
- Rubrica de avaliação (acurácia, completude, consistência) ✅

## Observações de qualidade (recomendadas para melhorar nota)

- O comparativo de arquiteturas no notebook está funcional, mas pode ficar mais forte incluindo tabela quantitativa de custo/latência por modelo e benchmark factual por tarefa.
- Para validação estatística avançada, adicionar comparação de distribuição com dados reais (quando disponíveis) usando teste KS/PSI.
- Para auditoria, versionar também um `data/synthetic_motor_records.json` opcional com o mesmo conteúdo do CSV.

## Conclusão

Pelo formato exigido, a entrega atual está **completa** para submissão da Sprint 1.  
As observações acima são melhorias incrementais para robustez e avaliação máxima.
