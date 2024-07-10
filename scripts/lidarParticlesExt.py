from TDStoreTools import StorageManager
import TDFunctions as TDF

_PANELS = [op.PARTICLES]

class lidarParticlesExt:
	"""
	lidarParticlesExt description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.panels = _PANELS
	
	def findExternalOps(self):
		tox = op.PROJ.findChildren(type=COMP)
		external = [ t for t in tox if t.par.externaltox != '' ]
		return external

	def SaveExternalizedTox(self):
		ext = self.findExternalOps()
		for op in ext:
			op.save(op.par.externaltox.eval())

	def SimulateClick(self, u, v):
		for panel in self.panels:
			panel.click(u, v)
			print(f'clicked {panel.name} at ({u},{v})')
  