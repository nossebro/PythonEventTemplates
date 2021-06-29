#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import ast
import logging
logger = logging.getLogger(__name__)

def CreateEventData(x, y, LiteralEval=False):
	z = dict()
	for i in x:
		if i in y and y[i]:
			z[i] = y[i]
			if LiteralEval:
				try:
					z[i] = ast.literal_eval(y[i])
				except:
					continue
		else:
			logger.debug("Key {0} does not exist".format(i))
			continue
	return z
