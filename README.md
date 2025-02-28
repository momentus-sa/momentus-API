<<<<<<< HEAD
![CAPA - GITHUB](https://github.com/user-attachments/assets/9f65d5a1-9604-4685-aa7d-2ecfe42bef73)

<h1 align="center">momentus</h1>

## Descrição

A momentus-API é a base que alimenta a plataforma Momentus, permitindo a criação, gestão e participação em eventos de forma eficiente e escalável. Desenvolvida com um backend robusto em Python utilizando Flask e banco de dados PostgreSQL, a API fornece endpoints seguros para operações como cadastro de eventos, gerenciamento de usuários, controle de ingressos e interações entre participantes e organizadores.
Com suporte a autenticação JWT, arquitetura RESTful e documentação clara, a momentus-API facilita a integração com diferentes front-ends e serviços externos.

Projetada para ser escalável e flexível, a API permite que organizadores tenham controle total sobre seus eventos, enquanto os participantes desfrutam de uma experiência fluida e intuitiva.

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas: [Git](https://git-scm.com), [Python](https://nodejs.org/pt), [PostgreSQL](https://www.postgresql.org/). Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com) Todas as instruções de comandos são para windows.

### Iniciando o servidor
- Clone este repositório

```
git clone https://github.com/momentus-sa/momentus-API.git
```

- Acesse a pasta no terminal/CMD

```
cd momentus-API
```

Crie um ambiente virtual python

```
python -m venv .venv
```

- Ative o ambiente virtual

```
./.venv/Scripts/activate.ps1
```

- Instale as dependências

```
pip install -r requirements.txt
```

- A seguir você precisará criar o arquivo `.env` e configurar seu banco de dados conforme o arquivo `.venv template`.

- Em seguida, basta executar no terminal

```
python app.py
```

- O servidor inciará na porta:5000: [http://localhost:3000](http://127.0.0.1:5000)

⚠️ Observação

Não compreendo muito bem o porquê, mas isso parece estar relacionado ao **PYTHONPATH**.  
O código só funciona corretamente quando executado com:  

```
python -m app
```


No meu computador eu fiz alguma configuração para corrigir isso, mas não lembro exatamente o que era.
De qualquer forma, funciona. 🚀


## Documentação
Caso queira aprender sobre os endpoints da momentus-API e como usá-la, verifique a documentação no postman:

#### 📖[Momentus-API-Docs](https://web.postman.co/documentation/35177931-5ca99b43-d556-4fb0-a3f2-b646031b96e5/publish?workspaceId=b1ff0c41-aba9-41a0-852f-c0cca414eaaf)


## Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

### Para o back-end:
- [Python](https://www.python.org)
- [PostgreSQL](https://www.postgresql.org)
- [Flask](https://flask.palletsprojects.com/en/stable/)

## Funcionalidades implementadas e futuras
- 🗸 Criar e acessar perfil próprio
- 🗸 Interface para participantes
- 🗸 Painel administrativo para organizadores
- 🗸 Cadastro de informações sobre eventos
- 🗸 Cronograma do evento
- 🗸 Visualizar eventos
- 🗸 Tipos de ingresso e quantidade de participantes
- 🗸 Gerenciamento de equipe e tarefas atribuídas aos membros
- 🗸 Exibição de informações detalhadas sobre o evento, como descrição, cronograma, local, ingressos disponíveis, e links para confirmação de presença
- ⌛ Ferramentas de análise em tempo real
- ⌛ Relatórios de vendas e feedback do público
- ⌛ Módulo para gestão da equipe organizadora, fornecedores e patrocínios
- ⌛ Emissão de confirmações de ingressos digitais (QR Codes)
- ⌛ Comunicação integrada com a equipe organizadora (chat, notificações)
- ⌛ Sistema de envio de e-mails e notificações push para participantes

## Autores
<table>
  <tr>
    <td align="center"><a href="https://github.com/lars-brg"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118675951?v=4" width="100px;" alt=""/><br /><sub><b>Lara Braga</b></sub></a><br />🖱
    <td align="center"><a href="https://github.com/RyamLael"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/128926385?v=4" width="100px;" alt=""/><br /><sub><b>Ryam Lael Oliveira</b></sub></a><br />🖱
    <td align="center"><a href="https://github.com/Miguel-Edson"><img style="border-radius: 50%;" src="https://media.licdn.com/dms/image/v2/D4D03AQFtILnptJjTyA/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1713018411022?e=1746057600&v=beta&t=2RPrLkepgdsXLmUjYzZOcYfZMQzqH1_FQ5KFw5_Zuis" width="100px;" alt=""/><br /><sub><b>Miguel Edson Ramos</b></sub></a><br />🖱
    <td align="center"><a href="https://github.com/YanMarcelo"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/128822295?v=4" width="100px;" alt=""/><br /><sub><b>Yan Marcelo</b></sub></a><br />🖱
  </tr>
</table>

<h4 align="start"> 
🚧 Em construção... 🚧  
</h4>
gi
