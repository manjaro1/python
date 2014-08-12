import pg
import database as d
from function import *
from datetime import date, timedelta

tabla = 'evaluaciones'
campos='id_usuario,eval_peso,fecha_peso,eval_estatura,eval_presion,fecha_sistolica,eval_glucosa,fecha_glucosa'
db = d.Database(tabla,'',campos)
where = " where fecha_peso is not null and fecha_sistolica is not null and fecha_glucosa is not null"
respuesta = db.get(where)
if(respuesta == True):
	#print db.numfilas
	total= db.numfilas
	
	for i in range(total):
		#print db.rows[i]['fecha_peso']
		nivel_peso = '';
		if(isinstance(db.rows[i]['eval_peso'],int)):
			nivel_peso = db.rows[i]['eval_peso']
			fecha_peso = db.rows[i]['fecha_peso']
			id_usuario = db.rows[i]['id_usuario']
			row_mantto = plan_mantto('1',nivel_peso,fecha_peso[0:10],id_usuario)
			print str(id_usuario)+' peso'+row_mantto
			#if(row_mantto!=False):
			#	a='test'
		if(isinstance(db.rows[i]['eval_presion'],int)):	
			fechapresion  = db.rows[i]['fecha_sistolica']	
			nivel_presion = db.rows[i]['eval_presion']	
			row_mantto    = plan_mantto('3',nivel_presion,fechapresion[0:10],id_usuario)
			print str(id_usuario)+' presion'+row_mantto

		if(isinstance(db.rows[i]['eval_glucosa'],int)):
			fechaglucosa  = db.rows[i]['fecha_glucosa']
			nivel_glucosa = db.rows[i]['eval_glucosa']
			row_mantto    = plan_mantto('4',nivel_glucosa,fechaglucosa[0:10],id_usuario)
			print str(id_usuario)+' glucosa'+row_mantto