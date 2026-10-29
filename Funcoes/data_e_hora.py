# Para trabalhar com ferramentas de Data e Hora é necessário importar uma biblioteca

import datetime
import calendar

# Necessário criar lista para escrever por extenso pois não puxa de alguma biblioteca os nomes pré-existentes
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembbro', 'Dezembro']
dias_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
# Python trabalha com padrão americano de data AAAA/MM/DD

# 21/12/2024
data = datetime.date(2024, 12, 21)

print(data)

hoje = datetime.date.today()

print(hoje)
print(hoje.strftime("%d/%m/%Y")) 
print(f'São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}') # '{meses[hoje.month - 1]}' pois não existe mês 0, se iniciando em 1

# Utilidades da biblioteca calendar 
print(f'2024 é Bissexto: {calendar.isleap(2024)}') # Definir se o ano é bissexto ou não

print(f'E qual o úliumo dia do mês? {calendar.monthrange(2026, 10)[1]}') # Mostra o último dia do mês