#!/usr/bin/python
import MySQLdb
import smtplib
from Querys import Querys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def getconection():
    # Open database connection
    db = MySQLdb.connect("server", "user", "password", "db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    return cursor


def sendmail(body=''):
    fromaddr = "From Addres to use in relay SMTP"
    toaddr = ['email1@domain','email2@domain'] # Recipient List to report
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ''.join(toaddr)
    msg['Subject'] = "Subject email here"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtpserver',25) #host smtp and port (25 default text-plain port)
	#server.starttls() uncomment for send email on TSL encryption 
    server.login(fromaddr, "passwordSMTP")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def getdata():
    try:
        cursor = getconection()
    except Exception as e:
        return "Fallo de conexion a la base de datos "+e.message

    leads = {}
    oportunidades = {}
    try:
        #Recojo el dicionario de Consultas
        sql=Querys.sql

        # Obtengo todos los leads validos
        cursor.execute(sql["LMercado"])
        leads["Mercado"] = cursor.fetchone()[0]

        # Obtengo Leads Contactados

        cursor.execute(sql["LContactados"])
        leads["Contactados"] = cursor.fetchone()[0]

        # Obtengo Leads No Contactados

        cursor.execute(sql["LNoContactados"])
        leads["NoContactados"] = cursor.fetchone()[0]

        # Obtengo Leads IntentandoContactar

        cursor.execute(sql["LIntentandoContactar"])
        leads["IntentandoContactar"] = cursor.fetchone()[0]

        # Obtengo Leads Cold

        cursor.execute(sql["LCold"])
        leads["Cold"] = cursor.fetchone()[0]

        # Obtengo Leads Contact in Future

        cursor.execute(sql["LContactFuture"])
        leads["ContactFuture"] = cursor.fetchone()[0]

        # Obtengo Leads Hot

        cursor.execute(sql["LHot"])
        leads["Hot"] = cursor.fetchone()[0]

        # Obtengo Leads Hot

        cursor.execute(sql["LJunk"])
        leads["Junk"] = cursor.fetchone()[0]

        # Obtengo Leads PreQualified

        cursor.execute(sql["LPreQualified"])
        leads["PreQualified"] = cursor.fetchone()[0]

        # Obtengo Leads Qualified

        cursor.execute(sql["LQualified"])
        leads["Qualified"] = cursor.fetchone()[0]


        # Obtengo Leads Warm

        cursor.execute(sql["LWarm"])
        leads["Warm"] = cursor.fetchone()[0]

        # Obtengo Leads Lost

        cursor.execute(sql["LLost"])
        leads["Lost"] = cursor.fetchone()[0]

        # Obtengo Leads WaitResponse

        cursor.execute(sql["LWaitResponse"])
        leads["WaitResponse"] = cursor.fetchone()[0]


        # Obtengo todas las oportunidades

        cursor.execute(sql["OMercado"])

        oportunidades["Mercado"]=cursor.fetchone()[0]

        # Oportunidades Dormidas

        cursor.execute(sql["ODormidas"])

        oportunidades["Dormidas"] = cursor.fetchone()[0]

        # Oportunidades Negociando/Revisando

        cursor.execute(sql["ONegociando"])

        oportunidades["Negociando"] = cursor.fetchone()[0]

        # Oportunidades Closed/Won

        cursor.execute(sql["OCerradasWon"])

        oportunidades["CerradasWon"] = cursor.fetchone()[0]

        # Oportunidades Closed/Lost

        cursor.execute(sql["OCerradasLost"])

        oportunidades["CerradasLost"] = cursor.fetchone()[0]


    except Exception as e:
        cursor.close()
        return "Fallo en la obtencion de datos: \n"+e.message


    cursor.close()
    body = "Fecha: "+str(datetime.now())+"\n\nLEADS: \n-------------\n"+"Leads totales: "+str(leads["Mercado"])+"\n"\
            "Contactados: "+str(leads["Contactados"])+"\n"\
            "Intentando Contactar: "+str(leads["IntentandoContactar"])+"\n"\
            "Cold : "+str(leads["Cold"])+"\n"\
            "Contact in Future: "+str(leads["ContactFuture"])+"\n"\
            "Hot: "+str(leads["Hot"])+"\n"\
            "Junk Lead: "+str(leads["Junk"])+"\n"\
            "Pre Qualifed: "+str(leads["PreQualified"])+"\n"\
            "Qualifed: "+str(leads["Qualified"])+"\n"\
            "Warm: "+str(leads["Warm"])+"\n"\
            "Lost: "+str(leads["Lost"])+"\n"\
            "Esperando Respuesta: "+str(leads["WaitResponse"])+"\n"\
            "No Contactados: "+str(leads["NoContactados"])+"\n-----------\n"\
            "OPORTUNIDADES: "+"\n-----------\n"+"Oportunidades Totales: "+str(oportunidades["Mercado"])+"\n"\
            "Dormidas: "+str(oportunidades["Dormidas"])+"\n"\
            "Negocionado/Revision: "+str(oportunidades["Negociando"])+"\n" \
            "Cerradas Ganadas: " + str(oportunidades["CerradasWon"]) + "\n" \
            "Cerradas Perdidas: " + str(oportunidades["CerradasLost"]) + "\n" \

    return body


if __name__ == '__main__':
    sendmail(body=getdata())
    print(getdata())
