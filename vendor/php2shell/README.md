# PHP2Shell · snapshot de terceiros

[Caso e análise](../../docs/vulnerabilities/php2shell/README.md) · [Validação](../../docs/vulnerabilities/php2shell/validation.md)

- **Autor:** Kislley Rodrigues (m0us3r).
- **Origem:** https://github.com/mym0us3r/PHP2Shell-Detection-with-Wazuh
- **Commit:** `17253b3185380956e4fc0aade158f8001793e2c5`.
- **Licença:** [MIT](LICENSE), preservada integralmente.
- **Integridade:** [manifest.json](manifest.json), com SHA de blob Git por arquivo.
- **Modificações nos artefatos:** nenhuma. Documentação e testes deste repositório ficam separados.

| Artefato | Função |
|---|---|
| [Regras](rules/php2shell_rules.xml) | Seis regras para sintomas e precondições |
| [Decoders](decoders/php2shell_decoders.xml) | Três blocos de parsing do log customizado |
| [Apache LogFormat](apache/php2shell-logformat.conf) | Coleta de metadados HTTP; grava cookies completos |
| [SCA](sca/php2shell_cve_2026_109618_109619.yml) | Cinco checks específicos de Ubuntu/PHP/mod_php |

**Não instalar automaticamente.** Ler o caso antes: cookies nos logs, escopo restrito de SCA, possíveis colisões de IDs e alteração de orientação PHP em 23/10 afetam o uso. A descrição de upstream de que um prefixo de cookie não conteria informação sensível não é garantia adotada por esta curadoria.

Para atualizar: revisar o diff upstream, obter um commit imutável, preservar licença, substituir artefatos de forma consistente, atualizar manifest e repetir validação. Não atualizar apenas a SCA ou um decoder sem revisar suas dependências.

O README upstream e suas screenshots não foram copiados. Consulte as evidências do autor no commit fixado; a execução no ambiente local permanece pendente.
