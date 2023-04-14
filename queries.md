-- Quantos alunos não quiseram declarar a cor/raça em 2020 (Entenda a opção “não declarado” nessa pergunta)?
select count(tp_cor_raca) from enem where tp_cor_raca = 0;

-- pesquisa somente pra entender a estrutura da tabela nesse campo de estado
select sg_uf_esc from enem where sg_uf_esc like 'RS';

-- Qual é o número de alunos do Sexo Feminino que estudaram em escola no estado de São Paulo?
select count(*) from enem where tp_sexo = 'F' and sg_uf_esc like 'SP';

-- Quantos alunos do sexo feminino que estudaram em escola no estado do Rio Grande do Sul possuem EXATAMENTE uma geladeira em casa?
select count(*) from enem where tp_sexo = 'F' and sg_uf_esc like 'RS' and q012 = 'B';

-- Qual é o segundo estado brasileiro (considere a coluna SG_UF_ESC) em que estudaram mais alunos no ENEM 2020?
-- select count(*) as poderosissimo_ninja, sg_uf_esc from enem group by sg_uf_esc order by poderosissimo_ninja DESC;
select count(sg_uf_esc) as poderosissimo_ninja, sg_uf_esc from enem group by sg_uf_esc order by poderosissimo_ninja DESC;

-- Qual é o estado brasileiro (considere a coluna SG_UF_ESC) possui o menor número de alunos cuja mãe possui ensino superior completo?
-- select count(*) as poderosissimo_ninja, sg_uf_esc from enem where q002 = 'F' group by sg_uf_esc order by poderosissimo_ninja ASC;
select count(sg_uf_esc) as poderosissimo_ninja, sg_uf_esc from enem where q002 = 'F' group by sg_uf_esc order by poderosissimo_ninja ASC;

-- Qual é o segundo estado brasileiro (considere a coluna SG_UF_ESC) que possui o maior número de pessoas na faixa “entre 26 e 30 anos”?
-- select count(*) as poderosissimo_ninja, sg_uf_esc from enem where tp_faixa_etaria = 11 group by sg_uf_esc order by poderosissimo_ninja DESC; 
select count(sg_uf_esc) as poderosissimo_ninja, sg_uf_esc from enem where tp_faixa_etaria = 11 group by sg_uf_esc order by poderosissimo_ninja DESC; 

-- Qual é o estado brasileiro (considere a coluna SG_UF_ESC) que possui o TERCEIRO maior número de alunos cuja residência possui PELO MENOS 2 banheiros?
select count(sg_uf_esc) as poderosissimo_ninja, sg_uf_esc from enem where q008 = 'C' group by sg_uf_esc order by poderosissimo_ninja DESC;

-- Quantos alunos do sexo feminino se autodeclararam pretos?
select count(*) from enem where tp_sexo = 'F' and tp_cor_raca = 2;

-- Quantos alunos estrangeiros fizeram o ENEM 2020?
select count(*) from enem where tp_nacionalidade = 3;

-- Qual é a diferença da nota média em matemática dos alunos que estudaram o ensino médio em escola pública e em escola privada?
select AVG(nu_nota_mt) from enem where tp_escola = 2; -- particular codigo 2 499.52498038446413
select AVG(nu_nota_mt) from enem where tp_escola = 3; -- particular codigo 3 610.6393569797274


-- Qual é o estado brasileiro (considere a coluna SG_UF_ESC) que possui o maior número de alunos do sexo feminino indígenas?
select count(SG_UF_ESC) as indigenas, SG_UF_ESC from enem where tp_sexo = 'F' and tp_cor_raca = 5 group by SG_UF_ESC order by indigenas DESC;

-- Qual é a diferença entre o número de alunos cujo pai possui pós-graduação completa e o número de alunos cuja mãe possui pós-graduação completa?
select count(*) from enem where q002 = 'G'; -- mãe 434437
select count(*) from enem where q001 = 'G'; -- pai 239720

-- Quantos alunos cuja residência possui ATÉ 2 carros estudaram na região NORDESTE do Brasil?
-- Maranhão, São Luís; 
-- Piauí, Teresina; 
-- Ceará, Fortaleza; 
-- Rio Grande do Norte, Natal; 
-- Paraíba, João Pessoa; 
-- Pernambuco, Recife; 
-- Alagoas, Maceió; 
-- Sergipe, Aracaju; 
-- Bahia, Salvador.
select count(*) from enem where q010 in ('B', 'C') and  SG_UF_ESC in ('MA', 'PI', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'BA');

-- Quantos alunos que estudaram em escolas em zona rural possuem internet em casa?
select count(*) from enem where tp_localizacao_esc = 2 and q025 = 'B';

-- Qual é o nome do município que contém a SEGUNDA maior quantidade total de inscritos no ENEM 2020?
select count(no_municipio_esc) as contagem_municipio, no_municipio_esc from enem group by no_municipio_esc order by contagem_municipio DESC;
