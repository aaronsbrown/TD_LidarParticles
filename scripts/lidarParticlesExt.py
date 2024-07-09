from TDStoreTools import StorageManager
import TDFunctions as TDF

class lidarParticlesExt:
	"""
	lidarParticlesExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def findExternalOps(self):
		tox = op.PROJ.findChildren(type=COMP)
		external = [ t for t in tox if t.par.externaltox != '' ]
		return external

	def SaveExternalizedTox(self):
		ext = self.findExternalOps()
		for op in ext:
			op.save(op.par.externaltox.eval())
