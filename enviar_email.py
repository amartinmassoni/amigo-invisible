#!/usr/bin/python3

import smtplib
import email.mime.text


def enviar_email(from_addr,
                 to_addrs,
                 subject,
                 body="",
                 cc_addrs=None,
                 cco_addrs=None,
                 text_type='plain',
                 server="localhost",
                 auth=None):
    """
       Envia un email desde una direccion a una lista de receptores
         from_addr = direccion de email del emisor
         to_addrs  = lista de direcciones de email de los receptores
         subject   = asunto del mensaje
         body      = cuerpo del mensaje (def. "")
         cc_addrs  = lista de direcciones email en copia (def. None)
         cco_addrs = lista de direcciones email en copia oculta (def. None)
         text_type = tipo de texto del mensaje (por defecto plain)
         server    = servidor SMTP que recibe el mensaje (def. localhost)
         auth      = autenticacion basica SMTP (usuario,password) (def. None)
    """
    msg = email.mime.text.MIMEText(body, text_type)
    msg['From'] = from_addr
    msg['To'] = ",".join(to_addrs)
    if cc_addrs:
        msg['Cc'] = ",".join(cc_addrs)
    msg['Subject'] = subject

    srv = smtplib.SMTP(server)
    if auth:
        srv.login(*auth)
    srv.sendmail(from_addr=from_addr,
                 to_addrs=to_addrs + (cc_addrs or []) + (cco_addrs or []),
                 msg=msg.as_string())
    srv.quit()
