# -*- coding: utf-8 -*-
from .component import *
from .linear_layout import *


class Panel(Component):

	def __init__(self, style=None):
		super(Panel, self).__init__(style=style)
		self.children = []
		self.layout = LinearLayout()

	def addComp(self, comp):
		comp.parent = self
		self.children.append(comp)
		if comp not in self.system.components:
			return self.system.addComp(comp)
		return comp

	def update(self):
		Component.update(self)

		if self.layout is not None:
			self.layout.reset()

			for comp in self.children:
				self.layout.apply(comp)
