# Roteiro da semana · Stories SALL Loja e SALL Outlet · 05 a 11/10/2026

Guia único para postar a semana inteira: o que vai ao ar em cada dia, em que ordem, com qual figurinha, e quais regras valem.
Arquivos: `out/stories/2026-10-DD/<marca>/NN.png` no branch `claude/festive-archimedes-8te3o5`.

---

## 1. Regras que valem todos os dias

**Marcas**
| | SALL Loja · @sallloja10 | SALL Outlet · @sall.outlet.10 |
|---|---|---|
| Vende | itens e contas de Roblox (Blox Fruits, Steal a Brainrot) | roupas, tênis, chuteiras e variedade. **Nada de Roblox** |
| Série fixa | POV (pedido confirmado → processando 94% → entrega concluída → já é seu) | "Chegou na Outlet" + "esse ou esse?" |
| Assinatura | SALL. Seu upgrade começa aqui. | SALL Outlet — exclusividade e estilo. |
| Link | sallloja.com | salloutlet.com |
| Cor de destaque (provisória) | azul #4C7DFF | dourado #C6A15B |

Fundo #0F0F10, texto #F5F4EF, fonte Liberation Sans Bold. A paleta é provisória e está registrada no voice.md.

**Nunca**
- Inventar preço, desconto, prazo de entrega, quantidade de produtos ou depoimento.
- Prometer velocidade de entrega (nada de "entrega na hora" ou "entrega rápida").
- Citar número de produtos sem confirmação do dono.
- Afirmar que algo "acabou de chegar" sem item confirmado.
- Usar imagem de banco, ilustração ou produto genérico no lugar do real.
- Misturar assinatura ou CTA entre as marcas.

**Formato de cada dia**
- Tela 1 é gancho (pergunta, contraste ou número real), pontuado pelo `hookscore.py`.
- No máximo 4 telas por marca. Pelo menos 1 figurinha interativa por dia.
- A última tela tem figurinha de **link** (nunca link escrito). Exceção: quarta, que fecha com o repost.
- Imagem 1080x1920. Nada nos 250 px de cima nem nos 340 px de baixo. Fonte ≥ 48 px, até ~15 palavras por tela.
- O retângulo pontilhado marca onde colar a figurinha no app. A figurinha cobre o texto de guia.
- SALL Loja: no máximo **2 enquetes na semana** (sexta e domingo).

**Fotos**
- Suba como `assets/stories/2026-10-DD/<marca>/NN.jpg` (NN = número da tela). Antes de gerar cada dia, faço `git pull` e uso a foto que estiver lá.
- Sem foto, a tela sai só com tipografia e cor. Até agora, **todas** as telas da semana saíram assim, porque nenhuma foto foi enviada.

---

## 2. Dia a dia

### Segunda 05 → postada na terça 06
Arquivos: `2026-10-05/`

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | POV: O ITEM QUE FALTAVA NO SEU ROBLOX. (78) | — |
| Loja | 02 | PEDIDO CONFIRMADO. / processando… 94% | Controle deslizante "Quanto você quer esse item?" |
| Loja | 03 | ENTREGA CONCLUÍDA. / item recebido ✓ | — |
| Loja | 04 | JÁ É SEU. / assinatura | Link → sallloja.com |
| Outlet | 01 | VOCÊ AINDA NÃO VIU O QUE CHEGOU NA OUTLET. (87) | — |
| Outlet | 02 | CHEGOU NA OUTLET. | — |
| Outlet | 03 | OLHA O DETALHE. | Controle deslizante "Quanto você quer?" |
| Outlet | 04 | GARANTE O SEU. / assinatura | Link → salloutlet.com |

### Terça 06
Sem conteúdo próprio: neste dia vão ao ar os stories de segunda.

### Quarta 07 · post novo no feed (repost)
Arquivos: `2026-10-07/` (o PNG 02 é só referência).

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | VOCÊ JOGA ROBLOX SEM ESSE ITEM? / post novo no feed (84) | — |
| Loja | 02 | repost do **reel corrigido**, feito pelo Instagram com fundo de cor | Controle deslizante "Esse item no seu inventário?" |
| Outlet | 01 | VOCÊ AINDA JOGA DE CHUTEIRA GASTA? / post novo no feed (81) | — |
| Outlet | 02 | repost do reel Nike, feito pelo Instagram com fundo de cor | Enquete "Você joga em campo ou society?" |

Como fazer o repost: abra o reel → enviar → "Adicionar ao story" → cor de fundo, texto e figurinha no app.

### Quinta 08
Arquivos: `2026-10-08/`

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | POV: SEU ROBLOX SEM ESSE ITEM FICOU NO PASSADO. (87) | — |
| Loja | 02 | PEDIDO CONFIRMADO. / processando… 94% | Controle deslizante "Nível de vontade:" |
| Loja | 03 | ENTREGA CONCLUÍDA. / item recebido ✓ | — |
| Loja | 04 | JÁ É SEU. / assinatura | Link → sallloja.com |

**SALL Outlet: escolha uma versão na hora de postar**
- **Com foto** em `assets/stories/2026-10-08/salloutlet/` → pasta `salloutlet/`, 4 telas: "VOCÊ AINDA NÃO VIU ISSO DE PERTO NA OUTLET." (87) → "DE PERTO." → "O DETALHE FAZ O ESTILO." + controle deslizante "Combina com você?" → "GARANTE O SEU." + link.
- **Sem foto** → pasta `salloutlet-sem-foto/`, 3 telas:

| Tela | Texto | Figurinha |
|---|---|---|
| 01 | O QUE FALTA NO SEU ESTILO? (52) | — |
| 02 | VOCÊ DECIDE. | Enquete "Tênis ou chuteira: o que falta no seu estilo?" |
| 03 | SALL OUTLET / exclusividade e estilo. | Link → salloutlet.com |

### Sexta 09 · plano B (itens reais não confirmados)
Arquivos: `2026-10-09/sallloja/` e `2026-10-09/salloutlet/`

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | BLOX FRUITS OU STEAL A BRAINROT? / você só pode escolher um. (65) | — |
| Loja | 02 | QUAL VOCÊ JOGA MAIS? | **Enquete 1/2** "Qual você joga mais?" Blox Fruits x Steal a Brainrot |
| Loja | 03 | GARANTE O SEU. / assinatura | Link → sallloja.com |
| Outlet | 01 | VOCÊ NÃO PODE FICAR SEM ALGO NOVO NA OUTLET. (87) | — |
| Outlet | 02 | VOCÊ DECIDE. | Controle deslizante "Quanto você quer algo novo?" |
| Outlet | 03 | GARANTE O SEU. / assinatura | Link → salloutlet.com |

Se os itens reais chegarem a tempo, use as pastas `sallloja-com-enquete/` e `salloutlet-com-enquete/`. Os itens são digitados na enquete, dentro do app.

### Sábado 10 · caixa de perguntas
Arquivos: `2026-10-10/`

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | AINDA NÃO ACHOU SEU ITEM DE ROBLOX? / você manda. (100) | — |
| Loja | 02 | PEDE AQUI. | Caixa de perguntas "Qual item você quer ver na SALL?" |
| Loja | 03 | SALL. / Seu upgrade começa aqui. | Link → sallloja.com |
| Outlet | 01 | AINDA NÃO ACHOU NA OUTLET? / você manda. (100) | — |
| Outlet | 02 | PEDE AQUI. | Caixa de perguntas "O que você quer ver chegando?" |
| Outlet | 03 | SALL OUTLET / exclusividade e estilo. | Link → salloutlet.com |

### Domingo 11 · fechamento (PNGs ainda não gerados)
Como sexta vai ao ar no plano B, não existe "item mais votado" nem "produto mais votado". O domingo usa a **versão B**, sem resultado:

| Marca | Tela | Texto | Figurinha |
|---|---|---|---|
| Loja | 01 | POV: O ITEM QUE VOCÊ ESCOLHEU NO ROBLOX JÁ É SEU. (81) | — |
| Loja | 02 | PEDIDO CONFIRMADO. / processando… 94% | **Enquete 2/2** "Garante o seu hoje?" Sim x Ainda não |
| Loja | 03 | ENTREGA CONCLUÍDA. / item recebido ✓ | — |
| Loja | 04 | JÁ É SEU. / assinatura | Link → sallloja.com |
| Outlet | 01 | AINDA NÃO ACHOU NA OUTLET? | — |
| Outlet | 02 | DE PERTO. | Controle deslizante "Esse vai pro seu look?" |
| Outlet | 03 | GARANTE O SEU. / assinatura | Link → salloutlet.com |

A tela 01 da Outlet no domingo repete o gancho de sábado. Vale decidir antes de gerar se é melhor trocar.

---

## 3. O que mudou no feed nesta semana

| Post | Antes | Depois |
|---|---|---|
| Reel SALL Loja, cartão 0:02.5 | ACABOU DE CHEGAR, MANO. | OLHA ISSO, MANO. |
| Reel SALL Loja, cartão 0:04.5 | PREÇO NO SITE. ENTREGA NA HORA. | PREÇO E DETALHES NO SITE. |
| Reel SALL Loja, cartão 0:07.5 | 45 PRODUTOS NO SITE. | (removido) |
| Legenda do reel SALL Loja | Item de Roblox novo acabou de chegar na SALL… | O item que faltava no seu Roblox. Garante o seu pelo link na bio. |
| Carrossel SALL Loja | entrega rápida · 45 produtos | sem prazo e sem número |
| Carrossel SALL Outlet | 43 produtos | sem número |

O MP4-guia do reel corrigido está em `out/reels/sallloja-roblox-corrigido.mp4`. É só a camada de texto, para usar no CapCut sobre a gravação real. Se a gravação for enviada para `assets/reels/sallloja-roblox-corrigido/`, eu monto os cartões por cima.

---

## 4. Pendências

1. **Domingo 11:** gerar os PNGs (versão B), depois de aprovar a tela 01 da Outlet.
2. **Etapa 4:** checklist de postagem por dia. Este roteiro já cobre a ordem das telas e as figurinhas.
3. **Etapa 5:** registrar os stories no log, atualizar o voice.md com as correções permanentes (sem prazo de entrega, sem número de produtos sem confirmação, Outlet sem Roblox) e fazer merge no `main`.
4. **Fotos reais:** nenhuma foi enviada até agora. Quando chegarem, gero de novo o dia correspondente.
5. **Cores oficiais:** a paleta atual é provisória.

---

## 5. Como gerar de novo

```bash
git pull
python3 tools/stories/render.py tools/stories/specs/2026-10-DD.json   # stories do dia
python3 tools/reels/render_reel.py tools/reels/specs/sallloja-roblox.json  # MP4-guia do reel
```

O texto de cada tela fica em `tools/stories/specs/2026-10-DD.json`. Para corrigir uma palavra, edite o arquivo e rode de novo.
