"""
akkalet is a tiny little framework based on gevent to simulate concepts in akka.
which can make concurrency simple.

it supports:
  1. actors
  2. routers
"""

from minakka import message
from . import route, message, actorsystem