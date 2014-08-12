# -*- coding: utf-8 -*-
import pg
import sys

class Database:
	tabla = {'nombre':'','id':'','campos':[]}
	
	def __init__(self,tabla,id_,campos):
		self.tabla['nombre'] = tabla
		self.tabla['id'] = id_
		self.tabla['campos'] = campos
		try:
			self.conexion = pg.connect('zbeltia', '127.0.0.1', 5432, None, None, 'postgres', 'abc1234')
			#self.conexion = pg.connect('db_zbeltia', '127.0.0.1', 5432, None, None, 'postgres', 'postgres')
			#self.conexion = pg.connect('db_zbeltia', '192.168.40.13', 5432, None, None, 'zbeltia2ngn', 'demozb3lt142')
		except:
			return False
	
	def agregar(self,values):
		conn = self.conexion
		sentencia = "INSERT INTO "+self.tabla['nombre']+"("+self.tabla['campos']+") VALUES("+values+")"				
		#print sentencia
		try:
			resultado=conn.query(sentencia)
			conn.close()
			return True
		except:
			return False		
	
	def add(self,values,returning):
		conn = self.conexion
		sentencia = "INSERT INTO "+self.tabla['nombre']+"("+self.tabla['campos']+") VALUES("+values+")" + returning
		try:
			resultado=conn.query(sentencia)
			self.row = resultado.dictresult()
			conn.close()
			return True
		except:
			return False
		
	def modificar(self,datos,where):
		conn = self.conexion	
		sentencia = "UPDATE "+self.tabla['nombre']+ " SET " + datos + where
		try:
			resultado=conn.query(sentencia)
			conn.close()			
			return True
		except:
			return False
	
	def eliminar(self,where):
		conn = self.conexion		
		sentencia = "DELETE FROM "+self.tabla['nombre'] + where
		try:
			resultado=conn.query(sentencia)
			conn.close()
			return True
		except:
			return False
	
	def consultar(self,where):
		conn = self.conexion
		exito = False
		sentencia = "SELECT * FROM "+ self.tabla['nombre'] + where
		try:
			resultado=conn.query(sentencia)
			conn.close()
			if resultado.ntuples() > 0:
				exito = True
		except:
			exito = False
		return exito
	
	def get(self,where):
		conn = self.conexion	
		sentencia = "SELECT "+self.tabla['campos']+" FROM "+ self.tabla['nombre'] + where
		try:
			resultado=conn.query(sentencia)
			conn.close()
			if resultado.ntuples() > 0:
				self.rows = resultado.dictresult()
				self.numfilas= resultado.ntuples()
				return True
			else:
				return False
		except:
			return False		
	def getqry(self,sentencia):
		conn = self.conexion	
		try:
			resultado=conn.query(sentencia)
			conn.close()
			if resultado.ntuples() > 0:
				self.rows = resultado.dictresult()
				return True
			else:
				return False
		except:
			return False	
