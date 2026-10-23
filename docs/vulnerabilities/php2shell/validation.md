# PHP2Shell · roteiro de validação

[← Caso](README.md)

## Evidência disponível

**Realizado nesta inclusão:** conferência de integridade do snapshot, parsing XML/YAML, inventário de IDs, referências locais e fixtures sintéticas. **Pendente:** execução no `wazuh-analysisd`, `wazuh-logtest`, SCA e pipeline de alertas. Teste estrutural não valida a semântica do motor Wazuh.

Para repetir a verificação estática, com Python e PyYAML instalados, execute da raiz:

```bash
python tests/php2shell/check_static.py
```

## Preparação do laboratório

1. Registrar versões de manager, agente, ruleset, sistema, Apache e pacote PHP; usar ambiente descartável com dados sintéticos.
2. Conferir [proveniência e licença](../../../vendor/php2shell/README.md); reservar IDs e fazer backup de regras/decoders/configuração antes da instalação manual.
3. Inspecionar os arquivos do snapshot. A configuração Apache com cookies não deve ser habilitada automaticamente.
4. Colocar regras e decoders nas respectivas pastas customizadas do manager. Validar a configuração com `/var/ossec/bin/wazuh-analysisd -t` antes de qualquer reinício.
5. Validar os decoders e regras no `/var/ossec/bin/wazuh-logtest`. Registrar a saída completa, SID final, nível e campos; não confiar somente em grep de sucesso.
6. Depois dos testes locais, validar coleta → análise → alerta → indexação com eventos sintéticos; conferir redaction, archives e permissões.

## Fixtures sem exploração

O arquivo [fixtures.json](../../../tests/php2shell/fixtures.json) contém linhas de log sintéticas, não requisições nem payloads de exploração. Enviar cada `log` individualmente ao logtest. Não misturar estes testes independentes com testes de frequência.

| Teste | Expectativa no motor |
|---|---|
| Multipart chunked sintético | Regra 100130 |
| Cookie sintético percentual | Regra 100131 |
| Multipart com comprimento definido | Não disparar 100130/100131 |
| PHPSESSID normal | Não disparar 100130/100131 |
| Percentual em outro cookie | Não disparar 100131 |

Expectativas são critérios a verificar, não resultados observados aqui. Para casos negativos, outras regras nativas podem produzir resultado.

## Casos adicionais obrigatórios

- OOM isolado e repetido: mesmo IP e IPs diferentes; confirmar campo `srcip` e SID final.
- HTTP 500: abaixo, no limite e acima da frequência; dentro e fora da janela; documentar comportamento real do contador.
- Segfaults sintéticos: validar parsing e correlação sem derrubar workers.
- Cabeçalhos com aspas escapadas, IPv6, proxy e formato diferente: identificar falhas de parsing.
- HTTP/2: registrar a lacuna da regra 100130, sem esperar equivalência com chunked HTTP/1.1.
- SCA: pacote corrigido/não corrigido; pacote ausente; PHP CLI ausente; overrides; plataforma fora do escopo. Não executar remediação automaticamente.
- Patch + troca de serialize handler em runtime: revisar separadamente o comunicado de 23/10; não interpretar score SCA como encerramento.

## Aceite e rollback

Guardar por caso: entrada, saída, versão, responsável, data, decisão e limitações. Promover para laboratório validado somente após execução reproduzível. Para rollback, restaurar os arquivos de backup, remover apenas os arquivos introduzidos por esta instalação, validar configuração e recarregar os serviços afetados conforme o procedimento local. Não apagar evidência de incidente durante rollback.
