
# 🏥 Alura – Sistema Inteligente de Diagnóstico Médico

O **Alura** é um sistema inteligente desenvolvido para auxiliar no diagnóstico de doenças comuns em Angola, analisando **sintomas e sinais vitais** dos pacientes. A plataforma identifica a gravidade do quadro clínico com base no **Protocolo de Manchester** e usa **Machine Learning** e **Análise de Dados** para melhorar a eficiência na tomada de decisão.

> Desenvolvido por **Anabelmo Feijo** no âmbito de um projeto académico com impacto na saúde pública em Angola.

---

## 🎯 Objetivo

Permitir que pacientes insiram seus **sintomas** e **dados vitais**, e receberem um **diagnóstico automatizado** com indicação de possíveis doenças e seu estado (alerta ou positivo), além da gravidade do quadro clínico.

---

## 🧠 Doenças Suportadas

Atualmente, o sistema está treinado para identificar as seguintes **6 doenças mais comuns em Angola**:

- HIV
- Paludismo
- Febre Amarela
- Febre Tifoide
- Tuberculose
- Hepatite B
- Doenças Cardíacas

---

## 🔍 Como funciona

### Identificação da doença:
- O sistema analisa os **sintomas selecionados** e os **dados vitais** do paciente.
- Segundo orientação médica:
  - **2 a 4 sintomas** da mesma doença → ⚠️ *Doença em Alerta*
  - **Mais de 4 sintomas** → ✅ *Doença Positiva*

### Página de Diagnóstico:
Ao pressionar "**+Informações**", o paciente é redirecionado para uma página com:
- Diagnóstico detalhado
- Doenças detectadas
- Estado da doença
- Gravidade com base no **Protocolo de Manchester**:

| Cor      | Nível de Urgência  |
|----------|--------------------|
| 🔵 Azul   | Não urgente        |
| 🟢 Verde  | Pouco urgente      |
| 🟡 Amarelo| Urgente            |
| 🟠 Laranja| Muito urgente      |
| 🔴 Vermelho| Emergência        |

---

## 🏗 Estrutura do Projeto (Arquitetura MVC)

```
/alura_backend
│
├── app/
│   ├── __init__.py               # Inicializa Flask
│   ├── config.py                 # Configurações (BD, chave secreta)
│
│   ├── models/                   # MODELS (estrutura do banco de dados)
│   │   ├── user.py
│   │   ├── patient.py
│   │   ├── symptoms.py
│   │   ├── vitals.py
│   │   └── diagnosis.py
│
│   ├── controllers/              # CONTROLLERS (lógica do sistema)
│   │   ├── auth_controller.py
│   │   ├── patient_controller.py
│   │   ├── diagnosis_controller.py
│   │   └── ml_controller.py
│
│   ├── routes/                   # VIEWS (rotas)
│   │   ├── auth_routes.py
│   │   ├── patient_routes.py
│   │   └── diagnosis_routes.py
│
│   ├── services/                 # Funções auxiliares
│   │   └── utils.py              # Código Manchester etc.
│
│   └── ml/                       # Machine Learning (modelo e processamento)
│       ├── model.h5              # Modelo treinado (TensorFlow)
│       └── preprocess.py         # Pré-processamento
│
├── run.py                        # Arquivo principal para executar o app
├── requirements.txt              # Dependências do projeto
└── README.md                     # Este documento
```

---

## 🤖 Machine Learning

Usamos **TensorFlow** para treinar o modelo responsável por prever doenças com base nos dados do paciente.

- Tipo recomendado: **Classificação Multiclasse**
- Modelo salvo em: `ml/model.h5`
- Script de pré-processamento em: `ml/preprocess.py`

### Por que usar ML?

- Detectar padrões invisíveis para humanos
- Classificar sintomas em tempo real
- Melhorar o diagnóstico automatizado com mais precisão

---

## 📊 Análise de Dados

Usada para:
- Avaliar relações entre sintomas e doenças
- Explorar correlações entre sinais vitais e doenças
- Melhorar a curadoria dos dados que alimentam o modelo de ML

Bibliotecas utilizadas:
- `pandas`
- `numpy`
- `matplotlib` (opcional)
- `seaborn` (opcional)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/alura_backend.git
cd alura_backend
```

2. Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate       # Linux/macOS
venv\Scripts\activate        # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o servidor Flask:

```bash
python run.py
```

---

## 📄 Arquivo `.gitignore`

Certifique-se de incluir:

```
venv/
__pycache__/
*.pyc
*.sqlite3
*.pyo
model.h5
.env
```

---

## 📚 Requisitos

- Python 3.9+
- Flask
- Flask SQLAlchemy
- TensorFlow
- Pandas
- NumPy

---

## 🧑‍💻 Autor

Desenvolvido por **Anabelmo Feijo**

---

## 📃 Licença

Projeto licenciado sob os termos da **MIT License**.

---
