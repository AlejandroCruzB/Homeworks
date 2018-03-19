# -*- coding: utf-8 -*-
#!/usr/bin/python

from datetime import date, datetime
hoy = datetime.now().strftime

print "Fecha y hora actual: Estamos a", hoy("%d-%m-%Y " + "y son las " + "%H:%M:%S")
