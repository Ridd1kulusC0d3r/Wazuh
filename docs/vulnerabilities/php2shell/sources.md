# Fontes e proveniência

[← Caso PHP2Shell](README.md)

Consultadas em **23/10/2026**. Fontes mutáveis podem receber revisões; reavaliar o caso após novos advisories.

## Fontes primárias

| Fonte | Papel |
|---|---|
| [PHP advisory 21/10](https://www.php.net/archive/2026.php#2026-10-21-5) | CVEs e versões corrigidas |
| [PHP pré-anúncio 20/10](https://www.php.net/archive/2026.php#2026-10-20-1) | CVSS v4.0 9.2 |
| [PHP arquivo atualizado em 23/10](https://www.php.net/archive/2026.php) | Aviso adicional de session upload progress |
| [Wiz Research](https://www.wiz.io/blog/php2shell-php-rce) | Pesquisa original e sinais observáveis |
| [Calif Research](https://calif.io/php2shell/) | Análise técnica da família de falhas |
| [Sintaxe de regras Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html) | Revisão de XML e correlação |
| [Sintaxe de decoders Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/decoders.html) | Parsing e campos |
| [Políticas customizadas SCA](https://documentation.wazuh.com/current/user-manual/capabilities/sec-config-assessment/creating-custom-policies.html) | Postura e checks |
| [ATT&CK T1190](https://attack.mitre.org/techniques/T1190/) | Exploração de aplicação exposta como contexto analítico |

## Referências complementares

| Fonte | Decisão de inclusão |
|---|---|
| [mym0us3r / PHP2Shell Detection](https://github.com/mym0us3r/PHP2Shell-Detection-with-Wazuh/blob/17253b3185380956e4fc0aade158f8001793e2c5/README.md) | Snapshot dos artefatos com licença MIT, autoria e hashes; validação do autor não equivale a validação local |
| [Sigma experimental de rjmendez](https://github.com/rjmendez/phpup-2026/blob/0ac08879909344fb14ffd915f59519b1612ef35e/rules/sigma/phpup2026-process-spawn.yml) | Referência linkada; não copiada nem convertida automaticamente |
| [Elastic Security Labs](https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection) | Referência de cobertura comportamental pós-exploração |
| [AWS WAF](https://aws.amazon.com/pt/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/) | Mitigação complementar e limites de inspeção |

## Comunidade e plataforma

[Wazuh Ambassador Program](https://wazuh.com/ambassadors-program/) · [Wazuh](https://wazuh.com/)

O projeto upstream identifica Kislley Rodrigues como Wazuh Ambassador. Essa afiliação pertence ao autor citado; não implica afiliação ou endosso deste repositório. Links de comunidade não são evidência técnica de eficácia.
