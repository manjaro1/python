import datetime
import database as d
def sumafecha(fecha,dias_repeticion):

	fecha      = fecha
	Date       = datetime.datetime.strptime(fecha, "%Y-%m-%d")
	EndDate    = str(Date + datetime.timedelta(days=dias_repeticion))[0:10]
	a          = datetime.datetime.strptime(EndDate, "%Y-%m-%d").date()
	fechaactual= datetime.datetime.strptime(str(datetime.datetime.today())[0:10], "%Y-%m-%d").date()
	return int((a-fechaactual).days)	

def plan_mantto(tipo_medicion,nivel_medicion,fecha,id_usuario):
	
	where_mantto  = " where medicion="+tipo_medicion+" and evaluacion="+ str(nivel_medicion) + ""
	mantto        = d.Database('plan_mantto_general','','dias_repeticion')
	row_mantto    = mantto.get(where_mantto)
	if(row_mantto==True):
		dias= mantto.rows[0]['dias_repeticion']
		
		atrasoMedicion='0'
		sumfec=sumafecha(fecha,dias)
		if(sumfec<0):
			atrasoMedicion='1'

		#print str(id_usuario)+'*'+str(atrasoMedicion)
		return  atrasoMedicion
	else:
		return false;	