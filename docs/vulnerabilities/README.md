![Vulnerability Intelligence](../../assets/vulnerabilities.svg)

[← Início](../../README.md) · [Detection Engineering](../detection.md)

# Vulnerability Intelligence & CVE Detection

Trilha 04: transformar advisories em inventário de exposição, hipóteses de hunting, sinais de detecção e evidências de remediação.

| Camada | Evidência | O que não comprova |
|---|---|---|
| Exposição | Pacote, fornecedor, SAPI, configuração e alcance de rede | Exploração ou comprometimento |
| Tentativa / sintomas | Eventos HTTP e erros correlacionados | Que o atacante executou código |
| Comportamento posterior | Processos, arquivos, conexões e contexto | Qual CVE originou a atividade |
| Remediação | Pacote corrigido, serviço recarregado e verificação operacional | Ausência de comprometimento anterior |

## Catálogo

| Caso | CVEs | Pacote | Estado |
|---|---|---|---|
| [PHP2Shell](php2shell/README.md) | CVE-2026-109618 / CVE-2026-109619 | 6 regras, 3 decoders, 5 checks SCA e LogFormat de terceiros | Snapshot revisado estaticamente; execução local no Wazuh pendente |

## Padrão para novos casos

Cada entrada deve conter: advisory primário; data da revisão; versões e backports; escopo de plataforma; fontes e licença; matriz sinal → inferência → falso positivo; pré-requisitos de coleta; fixtures; evidências de teste; mitigação; rollback e responsável pela revisão.

Estados: **referenciado → revisão estática → validado em laboratório → validado no ambiente**. Não promover automaticamente por popularidade, CVSS ou screenshots de terceiros.

O módulo nativo de Vulnerability Detection e uma política SCA não são a mesma coisa. A presença de um CVE neste catálogo não garante sua disponibilidade no feed do Wazuh. Confirme inventário, versão do feed e resultados no ambiente; use SCA para verificações específicas de postura, sem interpretar score como probabilidade de segurança.
