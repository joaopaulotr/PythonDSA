# Importação de bibliotecas necessárias
import re
import pandas as pd
from datetime import datetime

# Caminho do arquivo exportado do WhatsApp
arquivo = r"C:\PythonDSA\ProjetoAnaliseWpp\_chat.txt"  # Substitua pelo caminho do seu arquivo

padroes = [
    r"^\[(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}:\d{2})\s*[AP]M\] (.*?): (.*)",  # Novo formato com segundos e AM/PM
    r"^\[(\d{2}/\d{2}/\d{2,4}), (\d{2}:\d{2}(?::\d{2})?)\] (.*?): (.*)",  # Formato com colchetes
    r"^(\d{2}/\d{2}/\d{2,4}), (\d{2}:\d{2}(?::\d{2})?) - (.*?): (.*)",  # Formato com hífen
    r"^(\d{2}/\d{2}/\d{2,4}), (\d{1,2}:\d{2} (?:AM|PM)) - (.*?): (.*)",  # Formato com AM/PM e hífen
    r"^\[(\d{2}/\d{2}/\d{2,4}), (\d{1,2}:\d{2} (?:AM|PM))\] (.*?): (.*)",  # Formato com AM/PM e colchetes
]

def is_inicio_mensagem(linha):
    return any(re.match(p, linha) for p in padroes)

def extrair_info(linha):
    for padrao in padroes:
        match = re.match(padrao, linha)
        if match:
            return match.groups()
    return None

# Processamento do arquivo de mensagens
mensagens = []
msg_atual = {'data': '', 'hora': '', 'autor': '', 'mensagem': ''}

with open(arquivo, 'r', encoding='utf-8') as f:
    for linha in f:
        linha = linha.strip()
        if is_inicio_mensagem(linha):
            if msg_atual['mensagem']:
                mensagens.append(msg_atual)
            info = extrair_info(linha)
            if info:
                data, hora, autor, texto = info
                try:
                    if "AM" in hora or "PM" in hora:
                        hora_obj = datetime.strptime(hora, "%I:%M %p")
                        hora = hora_obj.strftime("%H:%M")
                except:
                    pass
                msg_atual = {'data': data, 'hora': hora, 'autor': autor, 'mensagem': texto}
        else:
            msg_atual['mensagem'] += ' ' + linha

# Adiciona a última mensagem
if msg_atual['mensagem']:
    mensagens.append(msg_atual)

# Criação do DataFrame
df = pd.DataFrame(mensagens)

if df.empty:
    print("Nenhuma mensagem encontrada.")
    exit()

# Conversão e extração de dados
df['data_hora'] = pd.to_datetime(df['data'] + ' ' + df['hora'], dayfirst=True, errors='coerce')
df.dropna(subset=['data_hora'], inplace=True)
df['dia'] = df['data_hora'].dt.date
df['hora_hh'] = df['data_hora'].dt.hour
df['tamanho_msg'] = df['mensagem'].astype(str).apply(len)

# Estatísticas principais
total_msgs = len(df)
por_autor = df['autor'].value_counts()
media_tam = df['tamanho_msg'].mean()
media_dia_total = df.groupby('dia').size().mean()
inicio = df['data_hora'].min().date()
fim = df['data_hora'].max().date()

# Médias por autor
media_dia_autor = df.groupby(['autor', 'dia']).size().unstack(fill_value=0).mean()
media_geral_autor = media_dia_autor.mean()
participacao_pct = (por_autor / total_msgs * 100).round(2)

# Horário mais ativo por autor
horario_top = df.groupby('autor')['hora_hh'].agg(lambda x: x.value_counts().idxmax())

# Duelo entre os dois mais ativos
top2 = por_autor.head(2)
duelo = df[df['autor'].isin(top2.index)].groupby(['dia', 'autor']).size().unstack(fill_value=0)
vitorias = {top2.index[0]: 0, top2.index[1]: 0, 'Empates': 0}
for _, row in duelo.iterrows():
    a = int(row.get(top2.index[0], 0))
    b = int(row.get(top2.index[1], 0))
    if a > b:
        vitorias[top2.index[0]] += 1
    elif b > a:
        vitorias[top2.index[1]] += 1
    else:
        vitorias['Empates'] += 1

total_duelos = sum(vitorias.values())
pct_1 = (vitorias[top2.index[0]] / total_duelos) * 100
pct_2 = (vitorias[top2.index[1]] / total_duelos) * 100
pct_empate = (vitorias['Empates'] / total_duelos) * 100

# Exibição dos resultados
print("\n📊 ESTATÍSTICAS RESUMIDAS")
print(f"Mensagens totais: {total_msgs}")
print(f"Período: {inicio} até {fim}")
print(f"Média mensagens/dia: {media_dia_total:.2f}")
print(f"Média de mensagens por dia (por autor): {media_geral_autor:.2f}")
print(f"Média caracteres/mensagem: {media_tam:.2f}")

print("\n👤 TOP PARTICIPANTES:")
for autor, qtd in por_autor.items():
    print(f"- {autor}: {qtd} msgs ({participacao_pct[autor]}%)")

print("\n🕐 Horário mais ativo:")
for autor, hora in horario_top.items():
    print(f"- {autor}: {hora}h")

print("\n⚔️ DUELO ENTRE OS 2 MAIORES PARTICIPANTES:")
print(f"{top2.index[0]} venceu {pct_1:.1f}% dos dias")
print(f"{top2.index[1]} venceu {pct_2:.1f}% dos dias")
print(f"Empates: {pct_empate:.1f}% dos dias")
