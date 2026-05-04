# Prompt Guide — Motores Elétricos Industriais

## 1) Critérios de seleção de modelos

| Critério | Peso | Pergunta |
|---|---:|---|
| Raciocínio técnico | 0.35 | Explica causa-raiz e plano de ação? |
| Custo computacional | 0.25 | Custo por 1M tokens / latência aceitável? |
| Multilíngue PT/EN | 0.20 | Mantém terminologia técnica consistente? |
| Execução local/API | 0.20 | Suporta Colab local ou requer API? |

Modelos avaliados: **GPT-4.1-mini**, **Llama 3.1 8B Instruct**, **Gemma 2 9B IT**, **Qwen2.5 7B Instruct**.

Decisão sugerida para a sprint:
- **Primário (API): GPT-4.1-mini** para qualidade em diagnóstico e instruções.
- **Secundário (local/Colab): Llama 3.1 8B** para geração em lote com menor custo.
- **Validação cruzada** com Gemma/Qwen em amostras críticas.

## 2) Templates por tarefa

### 2.1 Interpretação de sensores (zero-shot)
```text
Você é um analista de confiabilidade industrial.
Entrada: {json_sensores}
Tarefa: classifique estado do motor (normal/alerta/crítico), explique em 3 bullets e proponha 2 ações.
Responda em JSON com campos: estado, causas, acoes, confianca.
```

### 2.2 Diagnóstico de falhas (few-shot)
Use 2-3 exemplos com pares `sinais -> diagnóstico` antes do caso alvo.

### 2.3 Geração de instruções (CoT)
Estratégia: pedir raciocínio interno estruturado por etapas e retornar somente conclusão operacional.

### 2.4 Tradução técnica PT/EN (role-play)
```text
Atue como engenheiro de manutenção bilíngue (PT/EN).
Mantenha unidades SI e traduza sem alterar grandezas.
```

## 3) Rubrica de avaliação de respostas

- **Acurácia factual (0-5):** aderência a manual/catálogo técnico.
- **Completude (0-5):** cobre causa, evidência e ação.
- **Consistência terminológica (0-5):** padronização PT/EN e unidades.

Score final = `0.5*acurácia + 0.3*completude + 0.2*consistência`.

## 4) Controle de geração sintética

- Temperatura baixa (0.2–0.4) para relatórios críticos.
- `top_p` 0.85–0.95 para diversidade controlada.
- Saída obrigatória em schema tabular com metadados de prompt.
- Regras de validação:
  - temperatura de operação plausível (30–130 °C),
  - vibração plausível (0.5–20 mm/s),
  - coerência entre diagnóstico e severidade.
