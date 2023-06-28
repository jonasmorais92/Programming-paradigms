from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg = MIMEMultipart()
texto = 'Estou enviando um texpo por python'

senha = 'SUA SENHA'
msg['From'] = 'SEU @gmail.com'
msg['to'] = 'EMAIL DESTINO'
msg['Suject'] = 'Teste Python'

msg.attach(MIMEText(texto, 'plain'))

server = smtplib.SMTP('smtp.gmail.com: 587')
server.starttls()

#Login na conta para envio
server.login(msg['From'], senha)

#envio da mensagem
server.sendmail(msg['From'], msg['To'], msg.as_string())

#encerramento do servidor
server.quit()

print('Mensagem enviada com sucesso')