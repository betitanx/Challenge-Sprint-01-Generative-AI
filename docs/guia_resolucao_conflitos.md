# Guia rápido de resolução de conflitos (GitHub)

Este PR pode acusar conflito em `README.md` e `notebooks/sprint1_genai_fundamentos.ipynb` quando a branch base recebeu alterações paralelas.

## Passo a passo recomendado (linha de comando)

1. Atualize referências remotas:

```bash
git fetch origin
```

2. Vá para a branch do PR:

```bash
git checkout work
```

3. Faça rebase com a branch base (ex.: `main`):

```bash
git rebase origin/main
```

4. Resolva conflitos arquivo a arquivo:

- `README.md`: manter conteúdo mais recente e preservar seção de execução/validação.
- `notebooks/sprint1_genai_fundamentos.ipynb`: preferir versão mais recente e reexecutar notebook para validar células.

5. Após resolver:

```bash
git add README.md notebooks/sprint1_genai_fundamentos.ipynb
git rebase --continue
```

6. Valide:

```bash
python3 -m json.tool notebooks/sprint1_genai_fundamentos.ipynb >/dev/null
python3 scripts/validate_synthetic_data.py
```

7. Atualize o PR:

```bash
git push --force-with-lease
```

## Observação

Se preferir evitar conflito no notebook, use `nbdime` para merge orientado a células.
